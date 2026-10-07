# -*- coding: utf-8 -*-
from base import head, page, ic

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
    hero = '<img class="hero" src="img/ico_22.png" style="right:34px;top:96px;width:215px" alt="">'
    body = head('V', 'Atención y <em>restablecimiento</em> de derechos',
                '¿Qué hacemos cuando hay una alerta, amenaza o vulneración?', hero)

    body += '''<div class="pop" style="position:absolute;left:34px;top:288px;font-size:14.5px;font-weight:700;color:var(--gd)">Ruta de actuación en cinco pasos <span style="font-weight:600;font-size:12px;color:var(--muted)">· con el caso de Tania</span></div>'''
    x = 34
    for i, (nom, icono, col, tint, preg, txt) in enumerate(PASOS, 1):
        body += f'''
<div class="card" style="left:{x}px;top:314px;width:143px;height:192px;padding:0;overflow:hidden">
  <div style="background:{col};color:#fff;padding:9px 10px 8px;display:flex;align-items:center;gap:7px">
    <div style="font-family:Poppins;font-weight:800;font-size:19px;line-height:1">{i}</div>
    <div style="font-size:13px;font-weight:800;line-height:1.1;flex:1">{nom}</div>{ic(icono,20)}
  </div>
  <div style="padding:9px 10px 8px">
    <div style="font-size:11.8px;font-weight:800;color:{col};line-height:1.2;margin-bottom:6px">{preg}</div>
    <p style="font-size:11.3px;line-height:1.33">{txt}</p>
  </div>
  <div style="position:absolute;left:0;right:0;bottom:0;height:5px;background:{tint}"></div>
</div>'''
        x += 151.25

    body += f'''
<div class="card tint-pu" style="left:34px;top:520px;width:748px;height:84px;padding:10px 15px;display:flex;gap:13px;align-items:center">
  <div class="hex hx-pu" style="width:46px;height:52px">{ic('chat',24)}</div>
  <div><h3 style="color:var(--pu);margin-bottom:2px">Cuando no es claro si hay violencia: las «áreas grises»</h3>
  <p style="font-size:12px;color:var(--ink)">¿Qué elementos dificultan establecerlo? ¿Qué nos da más certezas? En el caso de Tania ayudaron <b>el análisis en equipo, la visita al hogar, la caracterización familiar y escuchar a la niña</b>.</p></div>
</div>'''

    body += f'''
<div class="card tint-g" style="left:34px;top:618px;width:366px;height:176px;padding:11px 15px">
  <h3>{ic('shield',19)} ¿Qué es restablecer derechos?</h3>
  <p style="font-size:12px">La protección integral incluye <b>«la seguridad de su restablecimiento inmediato»</b> (Ley 1098, art. 7). Para la niña o el niño víctima, se promueve su <b>recuperación física y psicológica y su reintegración social</b> (Convención, art. 39).</p>
  <p style="font-size:11.4px;margin-top:6px;color:var(--gd);font-weight:700">En el ICBF se tramita por el PARD: 10.034 procesos de 0 a 5 años activos en mayo de 2024.</p>
</div>
<div class="card tint-bl" style="left:414px;top:618px;width:368px;height:176px;padding:11px 15px">
  <h3 style="color:var(--blue)">{ic('users',19)} Corresponsabilidad: nadie actúa solo</h3>
  <p style="font-size:12px">La <b>familia, la sociedad y el Estado</b> son corresponsables del cuidado y la protección (art. 10). Cualquier persona puede exigir el cumplimiento y restablecimiento de los derechos, y el Estado tiene la <b>responsabilidad inexcusable de actuar oportunamente</b> (art. 11).</p>
  <p style="font-size:11.2px;margin-top:5px;color:var(--muted)">Ley 1098 de 2006</p>
</div>'''

    body += f'''
<div class="card" style="left:34px;top:808px;width:748px;height:92px;background:var(--gd);color:#fff;padding:12px 18px;display:flex;gap:16px;align-items:center">
  <div class="hex" style="width:52px;height:58px;background:#fff;color:var(--gd)">{ic('phone',27)}</div>
  <div style="flex:1">
    <div class="pop" style="font-size:15px;font-weight:800;color:#fff;line-height:1.2">¿Conoces un caso o necesitas orientación? Línea 141 del ICBF</div>
    <p style="color:#e3f1d6;font-size:12.2px;margin-top:3px">Gratuita, atiende las 24 horas, todos los días. Reporta maltrato infantil, violencia sexual u otras situaciones que amenacen los derechos de niñas, niños y adolescentes.</p>
  </div>
  <div class="num" style="color:#fff;font-size:40px">141</div>
</div>
<div class="card tint-or" style="left:34px;top:914px;width:748px;height:80px;padding:10px 16px;display:flex;gap:14px;align-items:center">
  <img src="img/ico_20.png" style="width:84px;height:58px;object-fit:contain;flex:none" alt="">
  <div><h3 style="color:#9a6310;margin-bottom:2px">Compromisos del fortalecimiento técnico</h3>
  <p style="font-size:12px;color:var(--ink)"><b>1.</b> Leer el Lineamiento técnico y el Protocolo de actuaciones. <b>2.</b> Replicar el fortalecimiento con las EAS (acta y evidencia fotográfica).</p></div>
</div>
<div class="src" style="bottom:6px;padding-top:4px"><b>Fuentes:</b> ICBF Regional Antioquia, presentación «Prevención de violencias», 2024 (diap. 13, 18-25, 29); Ley 1098 de 2006, arts. 7, 10 y 11; Ley 12 de 1991 (Convención), art. 19.2 y 39; ICBF, Línea 141. PARD: Proceso Administrativo de Restablecimiento de Derechos. UDS: Unidad de Servicio; EAS: entidad administradora del servicio.</div>'''
    return page(body, 'V')
