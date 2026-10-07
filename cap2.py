# -*- coding: utf-8 -*-
from base import head, page, ic, recordar

FORMAS = [
    ('Violencia física', 'alert', 'hx-or', 'var(--or)',
     'Acciones o conductas que causan <b>daño o sufrimiento físico</b>.'),
    ('Violencia psicológica', 'crack', 'hx-pu', 'var(--pu)',
     '<b>Castigo, humillación o abuso psicológico</b> que daña lo emocional.'),
    ('Violencia sexual', 'shield', 'hx-pk', 'var(--pk)',
     '<b>Abuso sexual</b>, actos sexuales abusivos, violación y explotación sexual.'),
    ('Omisión, negligencia o abandono', 'hourglass', 'hx-tl', 'var(--tl)',
     '<b>Descuido, omisión o trato negligente</b>; abandono físico, emocional y psicoafectivo.'),
]

# Agrupación propia para facilitar la lectura (las siete expresiones son las de la presentación)
GENERO = [
    ('Contra niñas y mujeres', ['Violencias contra las mujeres', 'Feminicidio', 'Obstétrica', 'Mutilación genital femenina']),
    ('Uniones y relaciones', ['Matrimonio temprano']),
    ('Contexto y recursos', ['Violencias en el conflicto', 'Económica y patrimonial']),
]

EFECTOS = [
    ('Tristeza y emociones intensas', '#fff3a8', -2),
    ('Ansiedad y depresión', '#bfe9f0', 1.5),
    ('Conductas agresivas', '#ffd2a8', -1),
    ('Baja autoestima e inseguridad', '#f7c6d9', 2),
    ('Dificultad para relacionarse', '#d6efb0', -1.5),
    ('Aislamiento, rechazo o agresión', '#bfe9f0', 1),
    ('Bajo rendimiento académico', '#fff3a8', -2),
    ('Retroceso en su desarrollo', '#ffd2a8', 2),
    ('Riesgo de ser adultos violentos', '#f7c6d9', -1),
]


def html():
    hero = '<img class="hero" src="img/kid_11.png" style="right:30px;top:80px;width:204px" alt="">'
    body = head('II', 'Las violencias y su incidencia',
                'Un golpe, una palabra o una omisión: toda <em>violencia</em> produce daño en niñas y niños',
                '¿Qué son y qué efectos producen?', hero)

    # Fila A
    chips = ''.join(f'<span class="pill" style="background:#fff;border:1.5px solid #cfe3bf;font-size:11px;padding:3px 8px">{t}</span>'
                    for t in ['Acción', 'Omisión', 'Abuso', 'Uso de la fuerza o del poder', 'Amenazas'])
    body += f'''
<div class="card tint-g" style="left:34px;top:290px;width:480px;height:146px">
  <h3>{ic('book',19)} ¿Qué entendemos por violencia?</h3>
  <p style="font-size:13.2px;color:var(--ink);line-height:1.4">Toda acción u omisión, abuso, uso de la fuerza o del poder, o amenaza, que <b>produce daño</b>, afecta la integridad personal y el desarrollo integral de niñas y niños, o puede llegar a <b>causarles la muerte</b>.</p>
  <div style="display:flex;flex-wrap:wrap;gap:4px;margin-top:8px">{chips}</div>
</div>
<div class="card" style="left:528px;top:290px;width:254px;height:68px;padding:9px 14px;display:flex;gap:10px;align-items:center">
  <div class="hex hx-g" style="width:38px;height:42px">{ic('home',20)}</div>
  <div><h3 style="margin:0 0 2px;font-size:13.4px">¿Dónde ocurre?</h3><p style="font-size:12.2px">En diferentes ámbitos: familiar, educativo y otros.</p></div>
</div>
<div class="card" style="left:528px;top:368px;width:254px;height:68px;padding:9px 14px;display:flex;gap:10px;align-items:center">
  <div class="hex hx-gd" style="width:38px;height:42px">{ic('users',20)}</div>
  <div><h3 style="margin:0 0 2px;font-size:13.4px">¿Quién la ejerce?</h3><p style="font-size:12.2px">Padres, representantes legales o cualquier otra persona.</p></div>
</div>'''

    # Fila B: formas
    body += '''<div class="pop" style="position:absolute;left:34px;top:446px;font-size:15px;font-weight:700;color:var(--gd)">Formas en que se expresa la violencia contra niñas y niños</div>'''
    x = 34
    for nombre, icono, hx, col, desc in FORMAS:
        body += f'''
<div class="card" style="left:{x}px;top:472px;width:177px;height:188px;border-top:5px solid {col};text-align:left">
  <div class="hex {hx}" style="width:40px;height:45px;margin-bottom:6px">{ic(icono,22)}</div>
  <h3 style="font-size:13.2px;margin-bottom:5px;color:var(--ink)">{nombre}</h3>
  <p style="font-size:12.4px">{desc}</p>
</div>'''
        x += 190

    # Fila C: género, agrupado
    cols = ''
    for tit, items in GENERO:
        ch = ''.join(f'<span class="pill" style="background:#fff;color:var(--pu);border:1.5px solid #d9c9ea;font-size:11.6px;margin:0 4px 4px 0">{g}</span>' for g in items)
        cols += f'<div style="flex:{1.5 if len(items) > 2 else 1}"><div style="font-size:10.8px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:#5a3a82;margin-bottom:4px">{tit}</div>{ch}</div>'
    body += f'''
<div class="card tint-pu" style="left:34px;top:670px;width:748px;height:112px;padding:10px 16px">
  <h3 style="color:var(--pu);margin-bottom:6px">{ic('gender',19)} Violencias basadas en género: también afectan a niñas y niños</h3>
  <div style="display:flex;gap:18px">{cols}</div>
</div>'''

    # Fila D: efectos
    notes = ''
    for t, c, r in EFECTOS:
        notes += f'<div style="background:{c};padding:5px 10px;border-radius:5px;font-size:12px;font-weight:700;color:#33332a;line-height:1.2;transform:rotate({r}deg);box-shadow:0 3px 7px rgba(0,0,0,.12)">{t}</div>'
    body += f'''
<div class="card" style="left:34px;top:794px;width:748px;height:136px;padding:11px 16px">
  <h3>{ic('layers',19)} ¿Cómo afecta la violencia a niñas y niños? <span style="font-weight:600;color:var(--muted);font-size:12px">· voces de los equipos técnicos</span></h3>
  <div style="display:flex;flex-wrap:wrap;gap:9px 9px;margin-top:9px">{notes}</div>
</div>'''

    # Fila E
    body += f'''
{recordar(942, 'No hace falta ver un golpe para que haya violencia: la humillación, la omisión y la negligencia también hieren. <small>Ley 1098 de 2006, art. 18: derecho a ser protegidos contra todo daño o sufrimiento físico, sexual o psicológico.</small>', 66)}
<div class="src" style="bottom:6px;padding-top:4px"><b>Fuentes:</b> ICBF Regional Antioquia, presentación «Prevención de violencias», 2024 (diap. 10, 15-17); Ley 1098 de 2006, arts. 18 y 20. Los efectos recogen aportes de los equipos técnicos de la presentación; la agrupación de las violencias basadas en género es una organización para facilitar la lectura.</div>'''
    return page(body, 'II')
