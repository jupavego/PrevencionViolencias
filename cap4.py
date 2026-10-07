# -*- coding: utf-8 -*-
from base import head, page, ic, recordar

ORIENT = [
    ('Promoción de relaciones de cuidado', 'heart', 'hx-g',
     '<b>Cuidado sensible y amoroso:</b> interacciones cotidianas que protegen y favorecen el desarrollo socioemocional.'),
    ('Desnaturalización de las violencias', 'eye', 'hx-or',
     'Dejar de ver como «normal» el castigo o la humillación. En el caso: <i>«la niña está muy malcriada porque el padre la trata muy suavecito»</i>.'),
    ('Gestión de riesgos y detección de situaciones de violencia', 'search', 'hx-tl',
     'Identificar riesgos y señales de alerta a tiempo. Las instituciones educativas deben establecer la <b>detección oportuna</b> (Ley 1098, art. 44).'),
    ('Reducción de los efectos de las violencias en las trayectorias de vida', 'sprout', 'hx-pu',
     '<b>Minimizar el impacto</b> y atenuar las consecuencias de las vulneraciones, para que no marquen el desarrollo.'),
    ('Atención y restablecimiento de derechos', 'shield', 'hx-pk',
     'Cuando ya hay una vulneración: <b>activar la ruta de actuación</b> y garantizar el restablecimiento (capítulo V).'),
]

MOMENTOS = [
    ('Momento 1', 'Acción sin vulneración', 'var(--g)',
     'Promover derechos y fortalecer los entornos como garantes: familia, UDS y comunidad.'),
    ('Momento 2', 'Ante riesgo de vulneración', 'var(--or)',
     'Identificar riesgos, dar seguimiento a las alertas y acercarse al contexto de niñas y niños.'),
    ('Momento 3', 'Ante la vulneración', 'var(--pk)',
     'Analizar, hacer seguimiento y ajustar de forma permanente las acciones de prevención.'),
]


def html():
    hero = ('<img class="hero" src="img/kid_21.png" style="right:26px;top:90px;width:182px" alt="">'
            '<img class="hero" src="img/kid_10.png" style="right:200px;top:150px;width:116px" alt="">')
    body = head('IV', 'Orientaciones para la prevención',
                'Prevenir es <em>actuar antes</em>: cinco orientaciones y tres momentos',
                '¿Qué hacemos antes de que la violencia ocurra o se agrave?', hero)

    body += f'''
<div class="card tint-g" style="left:34px;top:284px;width:748px;height:84px;display:flex;gap:14px;align-items:center;padding:10px 16px">
  <div class="hex hx-g" style="width:50px;height:56px">{ic('shield',26)}</div>
  <div><h3 style="margin-bottom:3px">¿Qué es prevenir?</h3>
  <p style="font-size:12.8px;color:var(--ink)">Conjunto de medidas y acciones, individuales, colectivas o institucionales, para <b>identificar amenazas, fortalecer capacidades y reducir riesgos y vulnerabilidades</b>, evitando hechos que afecten la protección integral y la garantía de derechos.</p></div>
</div>
<div class="pop" style="position:absolute;left:34px;top:378px;font-size:14.5px;font-weight:700;color:var(--gd)">Cinco orientaciones para prevenir las violencias en primera infancia</div>'''

    y = 404
    for i, (tit, icono, hx, desc) in enumerate(ORIENT, 1):
        body += f'''
<div class="card" style="left:34px;top:{y}px;width:748px;height:52px;padding:5px 14px;display:flex;align-items:center;gap:12px">
  <div class="hex {hx}" style="width:36px;height:41px;font-size:16px">{i}</div>
  <div class="hex {hx}" style="width:28px;height:32px;opacity:.85">{ic(icono,15)}</div>
  <div style="width:228px;font-size:12.8px;font-weight:800;color:var(--ink);line-height:1.18">{tit}</div>
  <div style="flex:1;font-size:11.8px;line-height:1.3;color:var(--ink2)">{desc}</div>
</div>'''
        y += 57

    body += '''<div class="pop" style="position:absolute;left:34px;top:700px;font-size:14.5px;font-weight:700;color:var(--gd)">Tres momentos de la prevención</div>'''
    x = 34
    for m, nom, col, txt in MOMENTOS:
        body += f'''
<div class="card" style="left:{x}px;top:726px;width:240px;height:100px;padding:9px 13px;border-left:5px solid {col}">
  <div style="font-size:11px;font-weight:800;letter-spacing:.07em;color:{col};text-transform:uppercase">{m}</div>
  <h3 style="font-size:13.6px;margin:2px 0 4px;color:var(--ink)">{nom}</h3>
  <p style="font-size:11.8px">{txt}</p>
</div>'''
        x += 254

    body += f'''
<div class="card tint-tl" style="left:34px;top:838px;width:366px;height:92px;padding:9px 14px">
  <h3 style="color:var(--tl);margin-bottom:4px">{ic('home',19)} Entornos protectores: familia y UDS</h3>
  <p style="font-size:11.8px">La familia debe <b>proteger a niñas y niños</b> de actos que amenacen su vida, dignidad o integridad; <b>toda violencia en la familia debe ser sancionada</b> (Ley 1098, art. 39).</p>
</div>
<div class="card tint-or" style="left:414px;top:838px;width:368px;height:92px;padding:9px 14px">
  <h3 style="color:#8a5410;margin-bottom:4px">{ic('spark',19)} Habilidades para la Vida y la Paz</h3>
  <p style="font-size:11.8px">Apuesta de ICBF en primera infancia: <b>educación inicial</b>, <b>cuidado sensible y amoroso</b> y desarrollo socioemocional, con equipos técnicos fortalecidos.</p>
</div>
{recordar(940, 'Prevenir no es esperar a que ocurra: es cuidar con sensibilidad, dejar de normalizar el castigo y detectar a tiempo.', 58)}
<div class="src" style="bottom:6px;padding-top:4px"><b>Fuentes:</b> ICBF Regional Antioquia, presentación «Prevención de violencias», 2024 (diap. 4-6, 23, 26); Plan Nacional de Acción contra la Violencia 2021-2024 (§5.3, definición de prevención del ICBF); Ley 1098 de 2006, arts. 39 y 44; ICBF, Estrategia «Construyendo Juntos Entornos Protectores».</div>'''
    return page(body, 'IV')
