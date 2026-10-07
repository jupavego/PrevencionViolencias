# -*- coding: utf-8 -*-
from base import head, page, ic

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

GENERO = ['Violencias contra las mujeres', 'Obstétrica', 'Feminicidio', 'Matrimonio temprano',
          'Violencias en el conflicto', 'Económica y patrimonial', 'Mutilación genital femenina']

EFECTOS = [
    ('Tristeza y estados emocionales intensos', '#fff3a8', -2),
    ('Ansiedad y depresión', '#bfe9f0', 1.5),
    ('Conductas agresivas con otras personas', '#ffd2a8', -1),
    ('Baja autoestima e inseguridad', '#f7c6d9', 2),
    ('Problemas de comportamiento', '#d6efb0', -1.5),
    ('No saber controlar sus emociones', '#fff3a8', 1),
    ('Dificultad para relacionarse', '#bfe9f0', -2),
    ('Bajo rendimiento académico', '#f7c6d9', 1.5),
    ('Aislamiento, rechazo o agresión', '#d6efb0', -1),
    ('Retroceso en su desarrollo', '#ffd2a8', 2),
    ('Riesgo de ser adultos violentos', '#fff3a8', -1.5),
]


def html():
    hero = '<img class="hero" src="img/kid_11.png" style="right:30px;top:84px;width:214px" alt="">'
    body = head('II', 'Las <em>violencias</em> y su incidencia en la vida de niñas y niños',
                '¿Qué son y qué efectos producen?', hero)

    # Fila A
    chips = ''.join(f'<span class="pill" style="background:#fff;border:1.5px solid #cfe3bf">{t}</span>'
                    for t in ['Acción', 'Omisión', 'Abuso', 'Uso de la fuerza o del poder', 'Amenazas'])
    body += f'''
<div class="card tint-g" style="left:34px;top:290px;width:480px;height:146px">
  <h3>{ic('book',19)} ¿Qué entendemos por violencia?</h3>
  <p style="font-size:13px;color:var(--ink);line-height:1.4">Toda acción u omisión, abuso, uso de la fuerza o del poder, o amenaza, que <b>produce daño</b>, afecta la integridad personal y el desarrollo integral de niñas y niños, o puede llegar a <b>causarles la muerte</b>.</p>
  <div style="display:flex;flex-wrap:wrap;gap:5px;margin-top:9px">{chips}</div>
</div>
<div class="card" style="left:528px;top:290px;width:254px;height:68px;padding:9px 14px;display:flex;gap:10px;align-items:center">
  <div class="hex hx-g" style="width:38px;height:42px">{ic('home',20)}</div>
  <div><h3 style="margin:0 0 2px;font-size:13px">¿Dónde ocurre?</h3><p style="font-size:11.8px">En diferentes ámbitos: familiar, educativo y otros.</p></div>
</div>
<div class="card" style="left:528px;top:368px;width:254px;height:68px;padding:9px 14px;display:flex;gap:10px;align-items:center">
  <div class="hex hx-gd" style="width:38px;height:42px">{ic('users',20)}</div>
  <div><h3 style="margin:0 0 2px;font-size:13px">¿Quién la ejerce?</h3><p style="font-size:11.8px">Padres, representantes legales o cualquier otra persona.</p></div>
</div>'''

    # Fila B: formas
    body += '''<div class="pop" style="position:absolute;left:34px;top:448px;font-size:15px;font-weight:700;color:var(--gd)">Formas en que se expresa la violencia contra niñas y niños</div>'''
    x = 34
    for nombre, icono, hx, col, desc in FORMAS:
        body += f'''
<div class="card" style="left:{x}px;top:474px;width:177px;height:182px;border-top:5px solid {col};text-align:left">
  <div class="hex {hx}" style="width:40px;height:45px;margin-bottom:6px">{ic(icono,23)}</div>
  <h3 style="font-size:13.4px;margin-bottom:5px;color:var(--ink)">{nombre}</h3>
  <p style="font-size:12px">{desc}</p>
</div>'''
        x += 190

    # Fila C: género
    gchips = ''.join(f'<span class="pill" style="background:#fff;color:var(--pu);border:1.5px solid #d9c9ea">{g}</span>' for g in GENERO)
    body += f'''
<div class="card tint-pu" style="left:34px;top:668px;width:748px;height:92px;padding:11px 16px">
  <h3 style="color:var(--pu);margin-bottom:6px">{ic('gender',19)} Violencias basadas en género: también afectan a niñas y niños</h3>
  <div style="display:flex;flex-wrap:wrap;gap:5px">{gchips}</div>
</div>'''

    # Fila D: efectos
    notes = ''
    for t, c, r in EFECTOS:
        notes += f'<div style="background:{c};padding:5px 9px;border-radius:5px;font-size:11.6px;font-weight:700;color:#3a3a2a;line-height:1.2;transform:rotate({r}deg);box-shadow:0 3px 7px rgba(0,0,0,.12)">{t}</div>'
    body += f'''
<div class="card" style="left:34px;top:774px;width:748px;height:166px;padding:12px 16px">
  <h3>{ic('layers',19)} ¿Cómo afecta la violencia a niñas y niños? <span style="font-weight:600;color:var(--muted);font-size:12px">· voces de los equipos técnicos</span></h3>
  <div style="display:flex;flex-wrap:wrap;gap:10px 9px;margin-top:12px">{notes}</div>
</div>'''

    # Fila E
    body += f'''
<div class="card tint-or" style="left:34px;top:952px;width:748px;height:44px;padding:8px 16px;display:flex;align-items:center;gap:12px">
  <div class="hex hx-or" style="width:34px;height:38px">{ic('shield',19)}</div>
  <p style="font-size:12.2px;color:var(--ink)"><b>Derecho a la integridad personal:</b> niñas, niños y adolescentes tienen derecho a ser protegidos contra todas las acciones o conductas que causen muerte, daño o sufrimiento físico, sexual o psicológico. <span style="color:var(--muted)">(Ley 1098 de 2006, art. 18)</span></p>
</div>
<div class="src" style="bottom:6px;padding-top:4px"><b>Fuentes:</b> ICBF Regional Antioquia, presentación «Prevención de violencias», 2024 (diap. 10, 15-17); Ley 1098 de 2006, arts. 18 y 20. Los efectos recogen aportes de los equipos técnicos de la presentación.</div>'''
    return page(body, 'II')
