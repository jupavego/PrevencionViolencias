# -*- coding: utf-8 -*-
from base import head, page, ic

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
    ('Momento 1', 'Acción sin vulneración', 'hx-g', 'var(--g)',
     'Promover derechos y fortalecer los entornos como garantes: familia, UDS y comunidad.'),
    ('Momento 2', 'Ante riesgo de vulneración', 'hx-or', 'var(--or)',
     'Identificar riesgos, dar seguimiento a las alertas y acercarse al contexto de niñas y niños.'),
    ('Momento 3', 'Ante la vulneración', 'hx-pk', 'var(--pk)',
     'Analizar, hacer seguimiento y ajustar de forma permanente las acciones de prevención.'),
]


def html():
    hero = ('<img class="hero" src="img/kid_21.png" style="right:30px;top:86px;width:190px" alt="">'
            '<img class="hero" src="img/kid_10.png" style="right:200px;top:154px;width:128px" alt="">')
    body = head('IV', 'Orientaciones para la <em>prevención</em>',
                '¿Qué hacemos antes de que la violencia ocurra o se agrave?', hero)

    body += f'''
<div class="card tint-g" style="left:34px;top:298px;width:748px;height:92px;display:flex;gap:14px;align-items:center">
  <div class="hex hx-g" style="width:52px;height:58px">{ic('shield',27)}</div>
  <div><h3 style="margin-bottom:3px">¿Qué es prevenir?</h3>
  <p style="font-size:12.8px;color:var(--ink)">Conjunto de medidas y acciones, individuales, colectivas o institucionales, para <b>identificar amenazas, fortalecer capacidades y reducir riesgos y vulnerabilidades</b>, evitando hechos que afecten la protección integral y la garantía de derechos.</p></div>
</div>
<div class="pop" style="position:absolute;left:34px;top:402px;font-size:14.5px;font-weight:700;color:var(--gd)">Cinco orientaciones para prevenir las violencias en primera infancia</div>'''

    y = 428
    for i, (tit, icono, hx, desc) in enumerate(ORIENT, 1):
        body += f'''
<div class="card" style="left:34px;top:{y}px;width:748px;height:54px;padding:6px 14px;display:flex;align-items:center;gap:12px">
  <div class="hex {hx}" style="width:38px;height:43px;font-size:16px">{i}</div>
  <div class="hex {hx}" style="width:30px;height:34px;opacity:.85">{ic(icono,16)}</div>
  <div style="width:228px;font-size:12.8px;font-weight:800;color:var(--ink);line-height:1.18">{tit}</div>
  <div style="flex:1;font-size:11.5px;line-height:1.3;color:var(--ink2)">{desc}</div>
</div>'''
        y += 60

    body += '''<div class="pop" style="position:absolute;left:34px;top:736px;font-size:14.5px;font-weight:700;color:var(--gd)">Tres momentos de la prevención</div>'''
    x = 34
    for m, nom, hx, col, txt in MOMENTOS:
        body += f'''
<div class="card" style="left:{x}px;top:762px;width:240px;height:114px;padding:10px 13px;border-left:5px solid {col}">
  <div style="font-size:10.8px;font-weight:800;letter-spacing:.07em;color:{col};text-transform:uppercase">{m}</div>
  <h3 style="font-size:13.4px;margin:2px 0 5px;color:var(--ink)">{nom}</h3>
  <p style="font-size:11.6px">{txt}</p>
</div>'''
        x += 254

    body += f'''
<div class="card tint-tl" style="left:34px;top:888px;width:366px;height:108px;padding:10px 14px">
  <h3 style="color:var(--tl)">{ic('home',19)} Entornos protectores: familia y UDS</h3>
  <p style="font-size:11.7px">La familia debe <b>proteger a niñas y niños</b> de actos que amenacen su vida, dignidad o integridad, y <b>cualquier forma de violencia en la familia debe ser sancionada</b> (Ley 1098, art. 39). Las UDS lo fortalecen con cuidadores y agentes educativos.</p>
</div>
<div class="card tint-or" style="left:414px;top:888px;width:368px;height:108px;padding:10px 14px">
  <h3 style="color:#9a6310">{ic('spark',19)} Habilidades para la Vida y la Paz</h3>
  <p style="font-size:11.7px">Apuesta estratégica de ICBF en primera infancia: <b>educación inicial</b> en el marco de la atención integral, <b>cuidado sensible y amoroso</b>, desarrollo socioemocional y fortalecimiento técnico de los equipos.</p>
</div>
<div class="src" style="bottom:6px;padding-top:4px"><b>Fuentes:</b> ICBF Regional Antioquia, presentación «Prevención de violencias», 2024 (diap. 4-6, 23, 26); Plan Nacional de Acción contra la Violencia 2021-2024 (§5.3, definición de prevención del ICBF); Ley 1098 de 2006, arts. 39 y 44; ICBF, Estrategia «Construyendo Juntos Entornos Protectores».</div>'''
    return page(body, 'IV')
