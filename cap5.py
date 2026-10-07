# -*- coding: utf-8 -*-
from base import head, page, ic, recordar

PASOS = [
    ('Detección', 'eye', 'var(--or)', '#fdf0dc', '¿Qué observamos o conocemos?',
     'Cualquier persona o institución puede detectar y reportar. En el caso: más silenciosa, sin ganas de jugar, misma ropa, vuelve a orinarse.'),
    ('Notificación', 'bell', 'var(--blue)', '#e3edf8', '¿Qué comunicamos y a quién?',
     'La agente educativa notifica a la coordinadora o representante legal de la UDS.'),
    ('Análisis', 'search', 'var(--gd)', '#e6f1dc', '¿Qué información nos permite comprender?',
     'El equipo interdisciplinario analiza en conjunto: visita al hogar, familia, salud y lo que dice la niña.'),
    ('Activar', 'bolt', 'var(--pu)', '#eee6f6', '¿Qué actuación corresponde?',
     'Se activan las actuaciones del Protocolo ante alertas de amenaza, vulneración o inobservancia de derechos.'),
    ('Seguimiento', 'loop', 'var(--pk)', '#fbe4ec', '¿Qué verificamos después?',
     'Observación posterior para constatar que las acciones se cumplen y que la niña o el niño está protegido, con valoración del sector Salud.'),
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
<div class="card tint-pu" style="left:34px;top:502px;width:748px;height:66px;padding:8px 15px;display:flex;gap:13px;align-items:center">
  <div class="hex hx-pu" style="width:46px;height:52px">{ic('chat',24)}</div>
  <div><h3 style="color:var(--pu);margin-bottom:2px">Cuando no es claro si hay violencia: las «áreas grises»</h3>
  <p style="font-size:12.4px;color:var(--ink)">¿Qué elementos dificultan establecerlo? ¿Qué nos da más certezas? En el caso de Tania ayudaron <b>el análisis en equipo, la visita al hogar, la caracterización familiar y escuchar a la niña</b>.</p></div>
</div>'''

    chips = ''.join(
        f'<span style="display:inline-block;background:#fff;border:1.5px solid #cfe3bf;border-radius:99px;padding:1px 8px;margin:0 3px 3px 0;font-size:10.6px;font-weight:700;color:var(--ink2);line-height:1.25">{t}</span>'
        for t in ['Salud (IPS y PIC)', 'Unidades de servicio (CDI, jardines privados)', 'Instituciones educativas', 'Fiscalía (CAIVAS / CAVIF)',
                  'Inspección de Policía', 'Policía de Infancia y Adolescencia', 'Líneas psicosociales o jurídicas',
                  'Organizaciones comunitarias', 'Comunidad en general'])
    body += f'''
<div class="card tint-g" style="left:34px;top:578px;width:474px;height:172px;padding:11px 15px">
  <h3 style="margin-bottom:4px">{ic('users',19)} ¿Quién puede detectar y reportar?</h3>
  <p style="font-size:12px;margin-bottom:6px"><b>Cualquier persona, organización o institución</b>: la familia, la sociedad y el Estado son corresponsables de la protección (Ley 1098, arts. 10 y 11).</p>
  <div>{chips}</div>
</div>
<div class="card tint-bl" style="left:522px;top:578px;width:260px;height:172px;padding:11px 13px">
  <h3 style="color:var(--blue);margin-bottom:4px">{ic('doc',19)} Para reportar, ten a la mano</h3>
  <p style="font-size:11.4px;margin-bottom:4px">Datos mínimos para activar la ruta a tiempo:</p>
  <ul style="list-style:none;font-size:11.4px;font-weight:700;color:var(--ink);line-height:1.28;margin-bottom:5px">
    <li>• Nombre y documento de la niña o el niño</li>
    <li>• Nombre de papá, mamá o cuidador/a</li>
    <li>• Dirección o teléfono de contacto</li>
  </ul>
  <div style="background:#fff;border-radius:10px;padding:4px 8px;font-size:10.8px;font-weight:700;color:#8a2a52;line-height:1.25">{ic('heart',14)} Siempre con <b>valoración de profesionales de Salud</b> (afectaciones físicas y psicológicas).</div>
</div>'''

    def canal(icono, titulo, cuerpo, destacado=False):
        bg = '#fff' if not destacado else '#fff'
        return f'''<div style="background:{bg};border-radius:12px;padding:6px 10px;display:flex;gap:8px;align-items:flex-start">
  <div style="color:#e0507c;flex:none;margin-top:1px">{ic(icono,17)}</div>
  <div><div style="font-size:11.4px;font-weight:800;color:var(--gd);line-height:1.15">{titulo}</div>
  <div style="font-size:11.8px;font-weight:700;color:var(--ink);line-height:1.28">{cuerpo}</div></div></div>'''

    body += f'''
<div class="card" style="left:34px;top:760px;width:748px;height:166px;background:var(--gd);color:#fff;padding:11px 16px">
  <div style="display:flex;align-items:center;gap:12px;margin-bottom:7px">
    <div class="hex" style="width:40px;height:45px;background:#fff;color:var(--gd)">{ic('phone',22)}</div>
    <div style="flex:1"><div class="pop" style="font-size:15px;font-weight:800;color:#fff;line-height:1.15">¿Conoces un caso o necesitas orientación?</div>
    <div style="color:#e3f1d6;font-size:11.8px">Para reportar una presunta amenaza o vulneración de derechos. <b style="color:#fff">24 horas, todos los días.</b></div></div>
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
{recordar(934, 'Si ves una señal de alerta, no la guardes: notifícala. <small>Cualquier persona puede exigir que se restablezcan los derechos de una niña o un niño (Ley 1098, art. 11).</small>', 58)}
<div class="src" style="bottom:6px;padding-top:4px"><b>Fuentes:</b> ICBF Regional Antioquia, presentación «Prevención de violencias», 2024 (diap. 18-25); ruta de actuación, paso «Detección» (contenido aportado por el equipo); Ley 1098 de 2006, arts. 10 y 11; Ley 12 de 1991, art. 19; ICBF, canales de atención; Consejería Presidencial para la Equidad de la Mujer (Línea 155). PIC: Plan de Intervenciones Colectivas. UDS: Unidad de Servicio.</div>'''
    return page(body, 'V').replace('</body>', '<script src="reportar.js"></script></body>')
