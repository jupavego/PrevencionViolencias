# -*- coding: utf-8 -*-
from base import head, page, ic, recordar

PASOS = [
    ('Identificación', 'eye', 'var(--or)', '#fdf0dc', '¿Qué observamos o conocemos?',
     'Cambios en la niña o el niño: más silenciosa, sin ganas de jugar, misma ropa, vuelve a orinarse.'),
    ('Notificación', 'bell', 'var(--blue)', '#e3edf8', '¿Qué comunicamos y a quién?',
     'La agente educativa notifica a la coordinadora o representante legal de la UDS.'),
    ('Análisis', 'search', 'var(--gd)', '#e6f1dc', '¿Qué información nos permite comprender?',
     'El equipo interdisciplinario analiza en conjunto: visita al hogar, familia, salud y lo que dice la niña.'),
    ('Activar', 'bolt', 'var(--pu)', '#eee6f6', '¿Qué actuación corresponde?',
     'Se activan las actuaciones del Protocolo ante alertas de amenaza, vulneración o inobservancia de derechos.'),
    ('Seguimiento', 'loop', 'var(--pk)', '#fbe4ec', '¿Qué verificamos después?',
     'Observación posterior para constatar que las acciones se cumplen y que la niña o el niño está protegido.'),
]


def html():
    hero = '<img class="hero" src="img/ico_22.png" style="right:30px;top:100px;width:208px" alt="">'
    body = head('V', 'Atención y restablecimiento de derechos',
                'Cinco pasos convierten una <em>alerta</em> en protección',
                '¿Qué hacemos cuando hay una alerta, amenaza o vulneración?', hero)

    body += '''<div class="pop" style="position:absolute;left:34px;top:262px;font-size:14.5px;font-weight:700;color:var(--gd)">Ruta de actuación en cinco pasos <span style="font-weight:700;font-size:12px;color:var(--muted)">· con el caso de Tania</span></div>'''
    x = 34
    for i, (nom, icono, col, tint, preg, txt) in enumerate(PASOS, 1):
        body += f'''
<div class="card" style="left:{x}px;top:288px;width:143px;height:206px;padding:0;overflow:hidden">
  <div style="background:{col};color:#fff;padding:9px 10px 8px;display:flex;align-items:center;gap:7px">
    <div style="font-family:Poppins;font-weight:800;font-size:19px;line-height:1">{i}</div>
    <div style="font-size:13px;font-weight:800;line-height:1.1;flex:1">{nom}</div>{ic(icono,20)}
  </div>
  <div style="padding:9px 10px 8px">
    <div style="font-size:12.2px;font-weight:800;color:{col};line-height:1.2;margin-bottom:6px">{preg}</div>
    <p style="font-size:11.8px;line-height:1.34">{txt}</p>
  </div>
  <div style="position:absolute;left:0;right:0;bottom:0;height:5px;background:{tint}"></div>
</div>'''
        x += 151.25

    body += f'''
<div class="card tint-pu" style="left:34px;top:504px;width:748px;height:72px;padding:10px 15px;display:flex;gap:13px;align-items:center">
  <div class="hex hx-pu" style="width:46px;height:52px">{ic('chat',24)}</div>
  <div><h3 style="color:var(--pu);margin-bottom:2px">Cuando no es claro si hay violencia: las «áreas grises»</h3>
  <p style="font-size:12.4px;color:var(--ink)">¿Qué elementos dificultan establecerlo? ¿Qué nos da más certezas? En el caso de Tania ayudaron <b>el análisis en equipo, la visita al hogar, la caracterización familiar y escuchar a la niña</b>.</p></div>
</div>'''

    body += f'''
<div class="card tint-g" style="left:34px;top:586px;width:366px;height:152px;padding:11px 15px">
  <h3>{ic('shield',19)} ¿Qué es restablecer derechos?</h3>
  <p style="font-size:12.4px">La protección integral incluye <b>«la seguridad de su restablecimiento inmediato»</b> (Ley 1098, art. 7). Para la niña o el niño víctima, se promueve su <b>recuperación física y psicológica y su reintegración social</b> (Convención, art. 39).</p>
  <p style="font-size:11.8px;margin-top:6px;color:var(--gd);font-weight:800">En el ICBF se tramita por el PARD: 10.034 procesos de 0 a 5 años activos en mayo de 2024.</p>
</div>
<div class="card tint-bl" style="left:414px;top:586px;width:368px;height:152px;padding:11px 15px">
  <h3 style="color:var(--blue)">{ic('users',19)} Corresponsabilidad: nadie actúa solo</h3>
  <p style="font-size:12.4px">La <b>familia, la sociedad y el Estado</b> son corresponsables del cuidado y la protección (art. 10). Cualquier persona puede exigir el cumplimiento y restablecimiento de los derechos, y el Estado tiene la <b>responsabilidad inexcusable de actuar oportunamente</b> (art. 11).</p>
  <p style="font-size:11.4px;margin-top:5px;color:var(--muted)">Ley 1098 de 2006</p>
</div>'''

    def canal(icono, titulo, cuerpo, destacado=False):
        bg = '#fff' if not destacado else '#fff'
        return f'''<div style="background:{bg};border-radius:12px;padding:6px 10px;display:flex;gap:8px;align-items:flex-start">
  <div style="color:#e0507c;flex:none;margin-top:1px">{ic(icono,17)}</div>
  <div><div style="font-size:11.4px;font-weight:800;color:var(--gd);line-height:1.15">{titulo}</div>
  <div style="font-size:11.8px;font-weight:700;color:var(--ink);line-height:1.28">{cuerpo}</div></div></div>'''

    body += f'''
<div class="card" style="left:34px;top:748px;width:748px;height:176px;background:var(--gd);color:#fff;padding:11px 16px">
  <div style="display:flex;align-items:center;gap:12px;margin-bottom:7px">
    <div class="hex" style="width:40px;height:45px;background:#fff;color:var(--gd)">{ic('phone',22)}</div>
    <div style="flex:1"><div class="pop" style="font-size:15px;font-weight:800;color:#fff;line-height:1.15">¿Conoces un caso o necesitas orientación?</div>
    <div style="color:#e3f1d6;font-size:11.8px">Para reportar una presunta amenaza o vulneración de derechos de niñas, niños y adolescentes. <b style="color:#fff">24 horas, todos los días.</b></div></div>
    <div class="num" style="color:#fff;font-size:38px">141</div>
    <button class="noexp" type="button" onclick="abrirReporteDesdeInfografia()"
      style="flex:none;border:0;cursor:pointer;background:#e0507c;color:#fff;font:800 12.5px Poppins,Nunito,sans-serif;border-radius:14px;padding:8px 13px;line-height:1.2;box-shadow:0 4px 0 rgba(0,0,0,.2)">{ic('heart',17)}<br>Informar<br>un caso</button>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6px">
    {canal('phone','Línea gratuita nacional','01 8000 91 8080')}
    {canal('chat','WhatsApp','320 239 1685 · 320 293 1320 · 320 865 5450')}
    {canal('pin','Chat y web','www.icbf.gov.co · o en persona, en los puntos de atención al ciudadano del ICBF')}
    {canal('heart','Línea 155 · violencias de género contra niñas y mujeres','Orientación gratuita · Consejería Presidencial para la Equidad de la Mujer')}
  </div>
</div>
{recordar(934, 'Si ves una señal de alerta, no la guardes: notifícala. <small>Cualquier persona puede exigir que se restablezcan los derechos de una niña o un niño (Ley 1098, art. 11).</small>', 60)}
<div class="src" style="bottom:6px;padding-top:4px"><b>Fuentes:</b> ICBF Regional Antioquia, presentación «Prevención de violencias», 2024 (diap. 13, 18-25); Ley 1098 de 2006, arts. 7, 10 y 11; Ley 12 de 1991 (Convención), arts. 19 y 39; ICBF, canales de atención (Línea 141, WhatsApp, línea nacional 01 8000 91 8080); Consejería Presidencial para la Equidad de la Mujer (Línea 155). PARD: Proceso Administrativo de Restablecimiento de Derechos. UDS: Unidad de Servicio.</div>'''
    return page(body, 'V').replace('</body>', '<script src="reportar.js"></script></body>')
