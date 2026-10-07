# -*- coding: utf-8 -*-
from base import head, page, ic

NORMAS = [
    ('Constitución Política', 'art. 44', 'scale', 'hx-gd',
     '«Los derechos de los niños prevalecen sobre los derechos de los demás.»'),
    ('Convención sobre los Derechos del Niño', 'Ley 12/1991, art. 19', 'shield', 'hx-bl',
     'Protección contra toda forma de perjuicio o abuso, descuido, malos tratos o explotación.'),
    ('Código de Infancia y Adolescencia', 'Ley 1098/2006, art. 7', 'heart', 'hx-pk',
     'Protección integral: reconocer, garantizar, prevenir vulneraciones y restablecer derechos.'),
    ('De Cero a Siempre', 'Ley 1804/2016, art. 1', 'sprout', 'hx-g',
     'Política de Estado para el desarrollo integral de la primera infancia.'),
]

PRINCIPIOS = [('No discriminación', 'art. 2'), ('Interés superior', 'art. 3'),
              ('Supervivencia y desarrollo', 'art. 6'), ('Participación', 'art. 12')]

NIVELES = [
    ('Sociedad', '#cfe0f3', 'var(--blue)',
     'Desigualdad económica y de género, pobreza, redes de seguridad débiles, normas legales y culturales que apoyan la violencia.'),
    ('Comunidad', '#c9e6e8', 'var(--tl)',
     'Concentración de pobreza, niveles altos de delincuencia, desempleo, servicios inadecuados, políticas institucionales débiles.'),
    ('Relaciones interpersonales', '#d8ecc9', 'var(--g)',
     'Prácticas de crianza deficientes, conflicto violento entre los padres, nivel socioeconómico bajo de la familia.'),
    ('Individual', '#f7cfdd', 'var(--pk)',
     'Edad, discapacidad, experiencia de maltrato infantil, historia de comportamiento violento, abuso de alcohol o sustancias.'),
]


def rings():
    return '''<svg width="212" height="204" viewBox="0 0 250 240" style="flex:none">
  <circle cx="125" cy="120" r="116" fill="#cfe0f3"/>
  <circle cx="125" cy="120" r="90" fill="#c9e6e8"/>
  <circle cx="125" cy="120" r="64" fill="#d8ecc9"/>
  <circle cx="125" cy="120" r="38" fill="#f7cfdd"/>
  <g font-family="Poppins,Nunito,sans-serif" font-weight="700" text-anchor="middle" fill="#0f3b34">
    <text x="125" y="23" font-size="11.5" fill="#0b4a8f">1 · Sociedad</text>
    <text x="125" y="49" font-size="11.5" fill="#1f7f8a">2 · Comunidad</text>
    <text x="125" y="75" font-size="10.5" fill="#2f7a1a">3 · Relaciones</text>
    <text x="125" y="119" font-size="10.5" fill="#b8325f">4 · Niña</text>
    <text x="125" y="132" font-size="10.5" fill="#b8325f">o niño</text>
  </g>
</svg>'''


def html():
    hero = '<img class="hero" src="img/ico_11.png" style="right:44px;top:98px;width:210px" alt="">'
    body = head('III', '<em>Enfoques</em> y modelo de análisis',
                '¿Cómo comprendemos lo que observamos y cómo abordamos la prevención?', hero)

    # A: marco normativo
    cols = ''
    for nom, ref, icono, hx, txt in NORMAS:
        cols += f'''<div style="flex:1;display:flex;gap:8px;min-width:0">
  <div class="hex {hx}" style="width:34px;height:38px;margin-top:2px">{ic(icono,18)}</div>
  <div><div style="font-size:12px;font-weight:800;color:var(--ink);line-height:1.15">{nom}</div>
  <div style="font-size:10.6px;font-weight:700;color:var(--g);margin:1px 0 3px">{ref}</div>
  <p style="font-size:11px;line-height:1.3">{txt}</p></div></div>'''
    body += f'''
<div class="card tint-g" style="left:34px;top:246px;width:748px;height:152px;padding:11px 15px">
  <h3 style="margin-bottom:8px">{ic('book',19)} Marco normativo: de la Constitución a la primera infancia</h3>
  <div style="display:flex;gap:12px">{cols}</div>
</div>'''

    # B: principios
    pr = ''
    for i, (n, a) in enumerate(PRINCIPIOS, 1):
        pr += f'''<div style="flex:1;display:flex;align-items:center;gap:8px;background:#fff;border-radius:14px;padding:6px 10px;box-shadow:0 4px 12px rgba(15,59,52,.06)">
  <div class="hex hx-gd" style="width:28px;height:31px;font-size:13px">{i}</div>
  <div><div style="font-size:12.4px;font-weight:800;color:var(--ink);line-height:1.1">{n}</div><div style="font-size:10.6px;color:var(--muted);font-weight:700">{a}</div></div></div>'''
    body += f'''
<div style="position:absolute;left:34px;top:410px;width:748px;display:flex;align-items:center;gap:10px">
  <div class="pop" style="font-size:13px;font-weight:700;color:var(--gd);width:128px;line-height:1.15">Cuatro principios de la Convención</div>
  <div style="flex:1;display:flex;gap:8px">{pr}</div>
</div>'''

    # C: enfoques
    enf = [
        ('Derechos y protección integral', 'ico_11.png', 'Reconoce a niñas y niños como <b>sujetos titulares de derechos</b>: promover el desarrollo integral, prevenir su vulneración, garantizar y restablecer.', 'tint-g', 'var(--gd)'),
        ('Diferencial', 'ico_10.png', 'Reconoce las <b>diferencias y particularidades</b> sociales y culturales (edad, etnia, discapacidad, territorio) y exige acciones afirmativas.', 'tint-bl', 'var(--blue)'),
        ('Género', None, 'Permite <b>promover equidad entre géneros</b>: las expectativas de género marcan la experiencia de la infancia.', 'tint-pu', 'var(--pu)'),
    ]
    x = 34
    pop = '''<div class="pop" style="position:absolute;left:34px;top:476px;font-size:13.5px;font-weight:700;color:var(--gd)">Tres enfoques para comprender y actuar</div>'''
    body += pop
    for nom, img, txt, tint, col in enf:
        art = (f'<img src="img/{img}" style="width:88px;height:60px;object-fit:contain;flex:none" alt="">' if img else
               f'<div class="hex hx-pu" style="width:56px;height:62px">{ic("gender",30)}</div>')
        body += f'''
<div class="card {tint}" style="left:{x}px;top:500px;width:240px;height:140px;padding:10px 13px">
  <div style="display:flex;align-items:center;gap:8px;margin-bottom:5px">{art}<h3 style="margin:0;font-size:13.4px;color:{col};flex:1">{nom}</h3></div>
  <p style="font-size:11.6px">{txt}</p>
</div>'''
        x += 254

    # D: modelo socio-ecológico
    leg = ''
    for n, bg, col, fac in NIVELES:
        leg += f'''<div style="display:flex;gap:9px;align-items:flex-start">
  <div style="width:12px;height:12px;border-radius:50%;background:{col};margin-top:3px;flex:none"></div>
  <div style="font-size:11.5px"><span style="font-size:12.2px;font-weight:800;color:{col}">{n}.</span> <span style="font-size:11.5px;color:var(--ink2);line-height:1.3">{fac}</span></div></div>'''
    body += f'''
<div class="card" style="left:34px;top:652px;width:748px;height:246px;padding:11px 15px">
  <h3 style="margin-bottom:4px">{ic('layers',19)} Modelo socio-ecológico: la violencia se explica en varios niveles a la vez</h3>
  <div style="display:flex;gap:16px;align-items:center">
    {rings()}
    <div style="flex:1;display:flex;flex-direction:column;gap:5px;line-height:1.28">
      <div style="font-size:11.4px;font-weight:700;color:var(--muted)">Ejemplos de factores de riesgo por nivel</div>
      {leg}
      <div style="font-size:11.2px;color:var(--gd);font-weight:700;background:var(--gx);border-radius:10px;padding:5px 9px">Cada nivel también tiene factores protectores: prevenir es actuar en todos.</div>
    </div>
  </div>
</div>'''

    # E: caso Tania
    body += f'''
<div class="card tint-or" style="left:34px;top:908px;width:748px;height:92px;padding:9px 14px">
  <h3 style="margin-bottom:5px;color:#9a6310">{ic('search',18)} Aplicado al caso de Tania (3 años): ¿cómo distinguimos lo que vemos?</h3>
  <div style="display:flex;gap:10px">
    <div style="flex:1;background:#fff;border-radius:10px;padding:5px 9px"><b style="font-size:11.4px;color:var(--pk)">Señales de alerta</b><p style="font-size:10.8px;line-height:1.28">Más silenciosa, pocas ganas de jugar, misma ropa, vuelve a orinarse.</p></div>
    <div style="flex:1;background:#fff;border-radius:10px;padding:5px 9px"><b style="font-size:11.4px;color:var(--tl)">Factores de riesgo</b><p style="font-size:10.8px;line-height:1.28">Poco tiempo con el padre, abuela hostil, red de apoyo lejana, controles de salud pendientes.</p></div>
    <div style="flex:1;background:#fff;border-radius:10px;padding:5px 9px"><b style="font-size:11.4px;color:var(--pu)">Lo que cambia el análisis</b><p style="font-size:10.8px;line-height:1.28">La niña dice que no quiere vivir con su abuela porque le grita.</p></div>
  </div>
</div>
<div class="src" style="bottom:6px;padding-top:4px"><b>Fuentes:</b> Constitución Política de 1991, art. 44; Ley 12 de 1991 (Convención, arts. 2, 3, 6, 12 y 19); Ley 1098 de 2006, art. 7; Ley 1804 de 2016, art. 1; ICBF, Política Nacional de Infancia y Adolescencia 2018-2030 (§4); Plan Nacional de Acción contra la Violencia 2021-2024 (§5.2, modelo OMS/INSPIRE); presentación ICBF 2024 (caso de Tania).</div>'''
    return page(body, 'III')
