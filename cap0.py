# -*- coding: utf-8 -*-
"""Portada resumen de los cinco capítulos."""
from base import page, ic, CSS  # noqa: F401

CAPS = [
    ('I', 'Contexto y situación de las violencias', '¿Qué está pasando?', 'chart', 'hx-g', 'var(--g)', '#f1f7ea',
     ['<b>10.034</b> procesos de niñas y niños de 0 a 5 años activos en el PARD (mayo 2024).',
      'La <b>omisión o negligencia</b> es el motivo del 51 % de los ingresos.',
      '<b>41,5 %</b> de las personas de 18 a 24 años reportó violencia antes de los 18 (EVCNNA 2018).']),
    ('II', 'Las violencias y su incidencia', '¿Qué son y qué efectos producen?', 'alert', 'hx-or', 'var(--or)', '#fdf0dc',
     ['Toda acción u omisión, uso de la fuerza o del poder, o amenaza que <b>produce daño</b>.',
      'Formas: <b>física, psicológica, sexual</b> y omisión, negligencia o abandono.',
      'Afecta las emociones, las relaciones y el desarrollo de niñas y niños.']),
    ('III', 'Enfoques y modelo de análisis', '¿Cómo comprendemos lo que observamos?', 'layers', 'hx-bl', 'var(--blue)', '#e3edf8',
     ['Niñas y niños son <b>sujetos titulares de derechos</b>: enfoques de derechos, diferencial y de género.',
      'El <b>modelo socio-ecológico</b> lee los riesgos en cuatro niveles: sociedad, comunidad, relaciones e individuo.']),
    ('IV', 'Orientaciones para la prevención', '¿Qué hacemos antes de que ocurra o se agrave?', 'sprout', 'hx-tl', 'var(--tl)', '#e0f1f2',
     ['<b>Cinco orientaciones:</b> relaciones de cuidado, desnaturalizar las violencias, gestionar riesgos, reducir efectos y restablecer derechos.',
      'Tres momentos: sin vulneración, ante riesgo y ante la vulneración.']),
    ('V', 'Atención y restablecimiento', '¿Qué hacemos ante una alerta o vulneración?', 'shield', 'hx-pk', 'var(--pk)', '#fbe4ec',
     ['Ruta en cinco pasos: <b>identificar, notificar, analizar, activar y hacer seguimiento</b>.',
      'Restablecer derechos es corresponsabilidad de familia, sociedad y Estado. <b>Línea 141</b> del ICBF.']),
]


def html():
    body = '''
<div class="dhex" style="right:-18px;top:-26px;width:110px;height:122px;background:#e3efd8;border:none;opacity:1"></div>
<div class="dhex" style="right:80px;top:-34px;width:60px;height:66px"></div>
<div class="hdr">
  <img class="l1" src="img/logo-icbf.png" alt="ICBF Bienestar Familiar">
  <div class="sep"></div>
  <img class="l2" src="img/logo-bello.png" alt="Alcaldía de Bello">
  <div class="org"><b>Regional Antioquia</b>Prevención de violencias · Primera infancia</div>
</div>
<div class="ttl" style="width:500px">
  <span class="chip">GUÍA RÁPIDA · 5 CAPÍTULOS</span>
  <h1 style="font-size:31px;margin:9px 0 7px">Prevención de <em>violencias</em> contra niñas y niños en primera infancia</h1>
  <div class="q">Del contexto a la acción: lo esencial de cada capítulo</div>
  <div class="bar"></div>
</div>
<img class="hero" src="img/kid_01.png" style="right:196px;top:104px;width:150px" alt="">
<img class="hero" src="img/kid_21.png" style="right:30px;top:86px;width:182px" alt="">
'''
    y = 306
    for rom, tit, preg, icono, hx, col, tint, pts in CAPS:
        lis = ''.join(f'<li style="margin-bottom:2px">{p}</li>' for p in pts)
        body += f'''
<div class="card" style="left:34px;top:{y}px;width:748px;height:100px;padding:0;overflow:hidden;display:flex">
  <div style="width:176px;background:{tint};padding:11px 12px;display:flex;flex-direction:column;justify-content:center;gap:5px;position:relative">
    <div style="display:flex;align-items:center;gap:8px">
      <div class="hex {hx}" style="width:44px;height:50px;font-size:17px">{rom}</div>
      <div style="color:{col}">{ic(icono,26)}</div>
    </div>
    <div style="font-family:Poppins;font-weight:700;font-size:12.4px;line-height:1.15;color:var(--ink)">{tit}</div>
  </div>
  <div style="flex:1;padding:9px 16px 8px 16px;border-left:4px solid {col}">
    <div class="pop" style="font-size:13.4px;font-weight:700;color:{col};margin-bottom:3px">{preg}</div>
    <ul style="list-style:none;padding:0">{lis.replace('<li ', '<li class="m" ')}</ul>
  </div>
</div>'''
        y += 108

    flow = ''
    labels = [('Contexto', 'hx-g'), ('Violencias', 'hx-or'), ('Análisis', 'hx-bl'), ('Prevención', 'hx-tl'), ('Actuación', 'hx-pk')]
    for i, (l, hx) in enumerate(labels):
        flow += f'''<div style="display:flex;flex-direction:column;align-items:center;gap:3px;width:78px">
  <div class="hex {hx}" style="width:36px;height:41px;font-size:13px">{i + 1}</div>
  <div style="font-size:11.2px;font-weight:800;color:var(--ink)">{l}</div></div>'''
        if i < 4:
            flow += '<div style="color:#9db98f;font-weight:800;margin-top:-14px">›</div>'

    body += f'''
<div class="card tint-g" style="left:34px;top:856px;width:462px;height:140px;padding:11px 14px">
  <h3>{ic('heart',19)} Un solo propósito: la protección integral</h3>
  <div style="display:flex;align-items:center;justify-content:space-between">{flow}</div>
  <p style="font-size:11.4px;margin-top:8px">Familia, sociedad y Estado son <b>corresponsables</b> del cuidado y la protección de niñas y niños (Ley 1098 de 2006, art. 10).</p>
</div>
<div class="card" style="left:510px;top:856px;width:272px;height:140px;background:var(--gd);color:#fff;padding:12px 16px">
  <div style="display:flex;align-items:center;gap:10px">
    <div class="hex" style="width:44px;height:50px;background:#fff;color:var(--gd)">{ic('phone',23)}</div>
    <div class="num" style="font-size:44px;color:#fff">141</div>
  </div>
  <div class="pop" style="font-size:13px;font-weight:700;margin-top:6px;line-height:1.2">Línea del ICBF · gratuita · 24 horas</div>
  <p style="color:#e3f1d6;font-size:11.2px;margin-top:2px;line-height:1.3">Reporta o pide orientación ante cualquier situación que amenace a una niña o un niño.</p>
</div>
<div class="src" style="bottom:6px;padding-top:4px"><b>Resumen de:</b> ICBF Regional Antioquia, presentación «Prevención de violencias», 2024; Ley 1098 de 2006; Ley 12 de 1991; Plan Nacional de Acción contra la Violencia 2021-2024; Política Nacional de Infancia y Adolescencia 2018-2030. Detalle y fuentes en cada capítulo.</div>'''
    css_extra = '<style>.m{font-size:11.6px;line-height:1.3;color:var(--ink2);padding-left:11px;position:relative}.m:before{content:"";position:absolute;left:0;top:6px;width:5px;height:5px;border-radius:50%;background:#9db98f}</style>'
    return page(body, 'portada').replace('</head>', css_extra + '</head>').replace('Capítulo portada · ', 'Portada · ')
