// Función de Vercel: recibe el formulario "Informar un caso" y lo envía por correo con Resend.
// Variables de entorno (se configuran en Vercel, nunca en el código):
//   RESEND_API_KEY  clave de Resend (obligatoria)
//   REPORT_TO       destinatario(s), separados por coma. Por defecto, el correo de prueba.
//   RESEND_FROM     remitente. Por defecto onboarding@resend.dev (modo de pruebas de Resend).
//   REPORT_MODE     "prod" quita la etiqueta [PRUEBA] del asunto.

const DEFAULT_TO = 'juan.velasquezg@icbf.gov.co';
const hits = new Map(); // limitador simple por IP (se reinicia cuando la función se "enfría")

const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const clip = (s, n) => String(s ?? '').trim().slice(0, n);

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') return res.status(405).json({ ok: false, error: 'Método no permitido' });

  const ip = String(req.headers['x-forwarded-for'] || '').split(',')[0].trim() || 'x';
  const now = Date.now();
  const recent = (hits.get(ip) || []).filter((t) => now - t < 10 * 60 * 1000);
  if (recent.length >= 5) return res.status(429).json({ ok: false, error: 'Demasiados envíos. Intenta de nuevo en unos minutos.' });

  let b = req.body;
  if (typeof b === 'string') { try { b = JSON.parse(b); } catch { b = {}; } }
  b = b || {};

  if (b.web) return res.status(200).json({ ok: true }); // campo trampa para bots: se ignora en silencio

  const relato = clip(b.relato, 3000);
  if (relato.length < 20) return res.status(400).json({ ok: false, error: 'Cuéntanos un poco más de lo que ocurre (mínimo 20 caracteres).' });
  if (b.acepto !== true) return res.status(400).json({ ok: false, error: 'Debes aceptar el aviso para enviar el formulario.' });

  const key = process.env.RESEND_API_KEY;
  if (!key) return res.status(503).json({ ok: false, error: 'El envío todavía no está configurado. Por favor llama a la Línea 141.' });

  const d = {
    rol: clip(b.rol, 60) || 'No indicado',
    lugar: clip(b.lugar, 160) || 'No indicado',
    cuando: clip(b.cuando, 120) || 'No indicado',
    nombre: clip(b.nombre, 120) || 'No indicado',
    contacto: clip(b.contacto, 160) || 'No indicado',
  };
  const fila = (k, v) => `<tr><td style="padding:6px 10px;background:#f3f6ee;font-weight:700;vertical-align:top;white-space:nowrap">${k}</td><td style="padding:6px 10px">${esc(v)}</td></tr>`;
  const html = `<div style="font-family:Arial,sans-serif;max-width:640px">
    <h2 style="color:#1d6a3a;margin:0 0 8px">Nuevo reporte desde las infografías de prevención de violencias</h2>
    <p style="color:#555;margin:0 0 12px">Enviado el ${esc(new Date().toLocaleString('es-CO', { timeZone: 'America/Bogota' }))} (hora de Colombia).</p>
    <table style="border-collapse:collapse;width:100%;border:1px solid #dfe6d6">
      ${fila('Quién informa', d.rol)}${fila('Lugar / municipio', d.lugar)}${fila('Cuándo', d.cuando)}
      ${fila('Nombre (opcional)', d.nombre)}${fila('Contacto (opcional)', d.contacto)}
    </table>
    <h3 style="color:#1d6a3a;margin:16px 0 6px">Relato</h3>
    <div style="white-space:pre-wrap;border-left:4px solid #5aa832;padding:6px 12px;background:#fafaf5">${esc(relato)}</div>
    <p style="color:#777;font-size:12px;margin-top:16px">La persona aceptó el aviso de que este formulario no es un canal de atención inmediata.</p>
  </div>`;

  const to = (process.env.REPORT_TO || DEFAULT_TO).split(',').map((s) => s.trim()).filter(Boolean);
  const prueba = process.env.REPORT_MODE === 'prod' ? '' : '[PRUEBA] ';
  try {
    const r = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        from: process.env.RESEND_FROM || 'onboarding@resend.dev',
        to,
        subject: `${prueba}Reporte de un caso · Prevención de violencias`,
        html,
        ...(d.contacto.includes('@') ? { reply_to: d.contacto } : {}),
      }),
    });
    if (!r.ok) {
      console.error('Resend', r.status); // no se registra el contenido del reporte
      return res.status(502).json({ ok: false, error: 'No pudimos enviar el mensaje. Por favor llama a la Línea 141.' });
    }
  } catch (e) {
    console.error('Resend fetch falló');
    return res.status(502).json({ ok: false, error: 'No pudimos enviar el mensaje. Por favor llama a la Línea 141.' });
  }
  recent.push(now); hits.set(ip, recent);
  return res.status(200).json({ ok: true });
};
