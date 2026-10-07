# -*- coding: utf-8 -*-
from base import head, page, ic, recordar

NORMAS = [
    ('Constitución Política', 'art. 44', 'scale', 'hx-gd',
     '«Los derechos de los niños prevalecen sobre los derechos de los demás.»'),
    ('Convención sobre los Derechos del Niño', 'Ley 12/1991, art. 19', 'shield', 'hx-bl',
     'Protege contra perjuicio, abuso, descuido, malos tratos y explotación.'),
    ('Código de Infancia y Adolescencia', 'Ley 1098/2006, art. 7', 'heart', 'hx-pk',
     'Protección integral: reconocer, garantizar, prevenir y restablecer.'),
    ('De Cero a Siempre', 'Ley 1804/2016, art. 1', 'sprout', 'hx-g',
     'Política de Estado para el desarrollo integral de la primera infancia.'),
]

PRINCIPIOS = [('No discriminación', 'art. 2'), ('Interés superior', 'art. 3'),
              ('Supervivencia y desarrollo', 'art. 6'), ('Participación', 'art. 12')]

NIVELES = [
    ('Sociedad', 'var(--blue)',
     'Desigualdad económica y de género, pobreza, redes de seguridad débiles, normas legales y culturales que apoyan la violencia.'),
    ('Comunidad', 'var(--tl)',
     'Concentración de pobreza, niveles altos de delincuencia, desempleo, servicios inadecuados, políticas institucionales débiles.'),
    ('Relaciones interpersonales', 'var(--g)',
     'Prácticas de crianza deficientes, conflicto violento entre los padres, nivel socioeconómico bajo de la familia.'),
    ('Individual', 'var(--pk)',
     'Edad, discapacidad, experiencia de maltrato infantil, historia de comportamiento violento, abuso de alcohol o sustancias.'),
]


def rings():
    return '''<svg width="176" height="169" viewBox="0 0 250 240" style="flex:none">
  <circle cx="125" cy="120" r="116" fill="#cfe0f3"/>
  <circle cx="125" cy="120" r="90" fill="#c9e6e8"/>
  <circle cx="125" cy="120" r="64" fill="#d8ecc9"/>
  <circle cx="125" cy="120" r="38" fill="#f7cfdd"/>
  <g font-family="Poppins,Nunito,sans-serif" font-weight="700" text-anchor="middle">
    <text x="125" y="23" font-size="12" fill="#0b4a8f">1 · Sociedad</text>
    <text x="125" y="49" font-size="12" fill="#1f7f8a">2 · Comunidad</text>
    <text x="125" y="75" font-size="11" fill="#2f7a1a">3 · Relaciones</text>
    <text x="125" y="119" font-size="11" fill="#b8325f">4 · Niña</text>
    <text x="125" y="132" font-size="11" fill="#b8325f">o niño</text>
  </g>
</svg>'''


def html():
    hero = '<img class="hero" src="img/ico_11.png" style="right:44px;top:98px;width:200px" alt="">'
    body = head('III', 'Enfoques y modelo de análisis',
                'La violencia tiene varias causas: por eso se analiza en <em>cuatro niveles</em>',
                '¿Cómo comprendemos lo que observamos?', hero)

    # A: marco normativo
    cols = ''
    for nom, ref, icono, hx, txt in NORMAS:
        cols += f'''<div style="flex:1;display:flex;gap:8px;min-width:0">
  <div class="hex {hx}" style="width:34px;height:38px;margin-top:2px">{ic(icono,18)}</div>
  <div><div style="font-size:12.2px;font-weight:800;color:var(--ink);line-height:1.15">{nom}</div>
  <div style="font-size:11px;font-weight:800;color:var(--gd);margin:1px 0 3px">{ref}</div>
  <p style="font-size:11.6px;line-height:1.3">{txt}</p></div></div>'''
    body += f'''
<div class="card tint-g" style="left:34px;top:250px;width:748px;height:150px;padding:11px 15px">
  <h3 style="margin-bottom:8px">{ic('book',19)} Marco normativo: de la Constitución a la primera infancia</h3>
  <div style="display:flex;gap:12px">{cols}</div>
</div>'''

    # B: principios
    pr = ''
    for i, (n, a) in enumerate(PRINCIPIOS, 1):
        pr += f'''<div style="flex:1;display:flex;align-items:center;gap:8px;background:#fff;border-radius:14px;padding:5px 10px;box-shadow:0 4px 12px rgba(15,59,52,.06)">
  <div class="hex hx-gd" style="width:28px;height:31px;font-size:13px">{i}</div>
  <div><div style="font-size:12.4px;font-weight:800;color:var(--ink);line-height:1.1">{n}</div><div style="font-size:11px;color:var(--muted);font-weight:700">{a}</div></div></div>'''
    body += f'''
<div style="position:absolute;left:34px;top:410px;width:748px;display:flex;align-items:center;gap:10px">
  <div class="pop" style="font-size:13px;font-weight:700;color:var(--gd);width:128px;line-height:1.15">Cuatro principios de la Convención</div>
  <div style="flex:1;display:flex;gap:8px">{pr}</div>
</div>'''

    # C: enfoques
    enf = [
        ('Enfoque de derechos', 'ico_11.png', 'Niñas y niños son <b>sujetos titulares de derechos</b>: se promueve su desarrollo y se previene su vulneración.', 'tint-g', 'var(--gd)'),
        ('Enfoque diferencial', 'ico_10.png', 'Reconoce las <b>diferencias sociales y culturales</b> (edad, etnia, discapacidad, territorio) y exige acciones afirmativas.', 'tint-bl', 'var(--blue)'),
        ('Enfoque de género', None, 'Promueve la <b>equidad entre géneros</b>: las expectativas de género marcan la infancia y las violencias.', 'tint-pu', 'var(--pu)'),
    ]
    x = 34
    for nom, img, txt, tint, col in enf:
        art = (f'<img src="img/{img}" style="width:78px;height:54px;object-fit:contain;flex:none" alt="">' if img else
               f'<div class="hex hx-pu" style="width:48px;height:54px;flex:none">{ic("gender",26)}</div>')
        body += f'''
<div class="card {tint}" style="left:{x}px;top:472px;width:240px;height:130px;padding:9px 13px">
  <div style="display:flex;align-items:center;gap:8px;margin-bottom:4px">{art}<h3 style="margin:0;font-size:13.8px;color:{col};flex:1">{nom}</h3></div>
  <p style="font-size:11.8px">{txt}</p>
</div>'''
        x += 254

    # D: modelo socio-ecológico
    leg = ''
    for n, col, fac in NIVELES:
        leg += f'''<div style="display:flex;gap:9px;align-items:flex-start">
  <div style="width:12px;height:12px;border-radius:50%;background:{col};margin-top:3px;flex:none"></div>
  <div style="font-size:11.8px"><span style="font-size:12.4px;font-weight:800;color:{col}">{n}.</span> <span style="color:var(--ink2);line-height:1.28">{fac}</span></div></div>'''
    body += f'''
<div class="card" style="left:34px;top:614px;width:748px;height:212px;padding:11px 15px">
  <h3 style="margin-bottom:4px">{ic('layers',19)} Modelo socio-ecológico: la violencia se explica en varios niveles a la vez</h3>
  <div style="display:flex;gap:16px;align-items:center">
    {rings()}
    <div style="flex:1;display:flex;flex-direction:column;gap:6px;line-height:1.28">
      <div style="font-size:11.6px;font-weight:800;color:var(--muted)">Ejemplos de factores de riesgo por nivel</div>
      {leg}
    </div>
  </div>
</div>'''

    # E: caso Tania
    body += f'''
<div class="card tint-or" style="left:34px;top:836px;width:748px;height:94px;padding:9px 14px">
  <h3 style="margin-bottom:5px;color:#8a5410">{ic('search',18)} Aplicado al caso de Tania (3 años): ¿cómo distinguimos lo que vemos?</h3>
  <div style="display:flex;gap:10px">
    <div style="flex:1;background:#fff;border-radius:10px;padding:5px 9px"><b style="font-size:11.8px;color:#b8325f">Señales de alerta</b><p style="font-size:11.4px;line-height:1.28">Más silenciosa, pocas ganas de jugar, misma ropa, vuelve a orinarse.</p></div>
    <div style="flex:1;background:#fff;border-radius:10px;padding:5px 9px"><b style="font-size:11.8px;color:var(--tl)">Factores de riesgo</b><p style="font-size:11.4px;line-height:1.28">Poco tiempo con el padre, abuela hostil, red de apoyo lejana.</p></div>
    <div style="flex:1;background:#fff;border-radius:10px;padding:5px 9px"><b style="font-size:11.8px;color:var(--pu)">Lo que cambia el análisis</b><p style="font-size:11.4px;line-height:1.28">La niña dice que no quiere vivir con su abuela porque le grita.</p></div>
  </div>
</div>
{recordar(940, 'Una señal aislada no explica una situación: se interpreta en su contexto, en equipo y escuchando a la niña o al niño. <small>Cada nivel también tiene factores protectores: prevenir es actuar en todos.</small>', 64)}
<div class="src" style="bottom:6px;padding-top:4px"><b>Fuentes:</b> Constitución Política (art. 44); Ley 12 de 1991 (Convención); Ley 1098 de 2006 (art. 7); Ley 1804 de 2016; ICBF, Política Nacional de Infancia y Adolescencia 2018-2030; Plan Nacional de Acción contra la Violencia 2021-2024 (modelo OMS/INSPIRE); presentación ICBF 2024 (caso de Tania).</div>'''
    return page(body, 'III')
