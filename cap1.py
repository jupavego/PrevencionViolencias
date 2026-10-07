# -*- coding: utf-8 -*-
from base import head, page, ic

BARS = [  # (etiqueta, valor, %, clase)
    ('Omisión o negligencia', 5117, '51,0', 'a'),
    ('Falta absoluta o temporal de responsables', 2200, '21,9', 'b'),
    ('Violencia sexual', 1066, '10,6', 'v'),
    ('Abandono (con o sin discapacidad)', 410, '4,1', 'a'),
    ('Violencia física', 214, '2,1', 'v'),
    ('Violencia psicológica', 131, '1,3', 'v'),
]
COL = {'a': 'var(--g)', 'b': 'var(--tl)', 'v': 'var(--pk)'}


def fmt(n):
    return f'{n:,}'.replace(',', '.')


def bars_html():
    mx = 5117
    out = ''
    for lab, val, pct, k in BARS:
        w = max(val / mx * 100, 2.2)
        out += f'''<div style="display:flex;align-items:center;gap:8px;height:23px">
  <div style="width:176px;font-size:11.6px;font-weight:700;color:var(--ink2);line-height:1.1">{lab}</div>
  <div style="flex:1;background:#eef2e9;border-radius:6px;height:15px"><div style="width:{w}%;height:15px;border-radius:6px;background:{COL[k]}"></div></div>
  <div style="width:78px;text-align:right;font-size:12px;font-weight:800;color:var(--ink)">{fmt(val)} <span style="font-weight:600;color:var(--muted);font-size:10.5px">{pct}%</span></div>
</div>'''
    return out


def html():
    hero = '<img class="hero" src="img/kid_01.png" style="right:30px;top:86px;width:196px" alt="">' \
           '<img class="hero" src="img/kid_00.png" style="right:196px;top:150px;width:122px;opacity:.96" alt="">'
    body = head('I', 'Contexto y situación de las <em>violencias</em>',
                '¿Qué está pasando con niñas y niños de 0 a 5 años?', hero)

    # Fila A
    body += f'''
<div class="card" style="left:34px;top:304px;width:232px;height:212px;background:var(--gd);color:#fff;display:flex;flex-direction:column;justify-content:center">
  <div style="display:flex;align-items:center;gap:8px;font-size:11px;font-weight:800;letter-spacing:.03em;color:#cfe8bd;white-space:nowrap">{ic('chart',18)} PARD ACTIVOS · MAYO 2024</div>
  <div class="num" style="font-size:56px;color:#fff;margin:8px 0 6px">10.034</div>
  <p style="color:#e9f4df;font-size:13.2px;line-height:1.35">procesos de niñas y niños de <b style="color:#fff">0 a 5 años</b> activos en el Proceso Administrativo de Restablecimiento de Derechos.</p>
</div>
<div class="card" style="left:280px;top:304px;width:502px;height:212px">
  <h3>{ic('layers',19)} ¿Por qué ingresan? Motivos de ingreso al PARD</h3>
  {bars_html()}
  <p style="font-size:11px;margin-top:5px;color:var(--muted)">Porcentaje sobre 10.034 procesos. Incluye además otros motivos (338), reunificación familiar (213) y conductas sexuales entre menores de 14 años (167).</p>
</div>'''

    # Fila B
    body += f'''
<div class="card tint-pk" style="left:34px;top:530px;width:366px;height:150px">
  <h3 style="color:#a02a52">{ic('alert',19)} Violencias reportadas · niñas y niños de 0 a 5 años</h3>
  <div style="display:flex;gap:12px">
    <div style="flex:1;background:#fff;border-radius:14px;padding:10px 10px 9px;text-align:center">
      <div class="num" style="font-size:33px;color:var(--pk)">2.222</div>
      <p style="font-size:12px;font-weight:700;color:var(--ink)">Violencia intrafamiliar</p></div>
    <div style="flex:1;background:#fff;border-radius:14px;padding:10px 10px 9px;text-align:center">
      <div class="num" style="font-size:33px;color:var(--pk)">2.546</div>
      <p style="font-size:12px;font-weight:700;color:var(--ink)">Violencia sexual</p></div>
  </div>
  <p style="font-size:10.8px;color:#8a4a62;margin-top:7px">Casos reportados · Observatorio de Violencias (ML), 2022</p>
</div>
<div class="card tint-g" style="left:414px;top:530px;width:368px;height:156px">
  <h3>{ic('pin',19)} Antioquia en la presentación ICBF</h3>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
    <div style="background:#fff;border-radius:12px;padding:5px 10px"><div class="num" style="font-size:22px;color:var(--pk)">328</div><p style="font-size:11.4px">Violencia intrafamiliar</p></div>
    <div style="background:#fff;border-radius:12px;padding:5px 10px"><div class="num" style="font-size:22px;color:var(--pk)">384</div><p style="font-size:11.4px">Violencia sexual</p></div>
    <div style="background:#fff;border-radius:12px;padding:5px 10px"><div class="num" style="font-size:22px">1.373</div><p style="font-size:11.4px">PARD abiertos</p></div>
    <div style="background:#fff;border-radius:12px;padding:5px 10px"><div class="num" style="font-size:22px">643</div><p style="font-size:11.4px">Por omisión o negligencia</p></div>
  </div>
</div>'''

    # Fila C
    body += f'''
<div class="card" style="left:34px;top:694px;width:476px;height:176px">
  <h3>{ic('users',19)} Una mirada nacional: la violencia empieza temprano</h3>
  <div style="display:flex;gap:16px;align-items:center">
    <svg width="116" height="116" viewBox="0 0 90 90" style="flex:none">
      <circle cx="45" cy="45" r="34" fill="none" stroke="#eef2e9" stroke-width="12"/>
      <circle cx="45" cy="45" r="34" fill="none" stroke="var(--pk)" stroke-width="12" stroke-dasharray="88.7 124.9" transform="rotate(-90 45 45)" stroke-linecap="round"/>
      <text x="45" y="47" text-anchor="middle" font-family="Poppins" font-weight="800" font-size="17" fill="#0f3b34">41,5%</text>
      <text x="45" y="59" text-anchor="middle" font-family="Nunito" font-weight="700" font-size="5.6" fill="#35564f">reportó violencia</text>
    </svg>
    <div style="flex:1">
      <p style="font-size:12.2px;margin-bottom:7px">De las personas de <b>18 a 24 años</b>, <b>41,5 %</b> reportó haber sufrido violencia antes de cumplir 18:</p>
      <div style="display:flex;gap:7px">
        <span class="pill" style="background:var(--pkl);color:#a02a52">32,1 % física</span>
        <span class="pill" style="background:var(--pul);color:var(--pu)">15,2 % psicológica</span>
        <span class="pill" style="background:var(--orl);color:#9a6310">11,4 % sexual</span>
      </div>
      <p style="font-size:10.8px;color:var(--muted);margin-top:7px">EVCNNA 2018. Las formas de violencia pueden presentarse juntas.</p>
    </div>
  </div>
</div>
<div class="card tint-pu" style="left:524px;top:694px;width:258px;height:176px">
  <h3 style="color:var(--pu)">{ic('target',19)} Lectura territorial</h3>
  <p style="font-size:12.8px;color:var(--ink);font-weight:700;line-height:1.35">¿Cuáles son los tipos de violencia más frecuentes en tu territorio contra niñas y niños, desde la gestación hasta los cinco años?</p>
  <div style="display:flex;flex-wrap:wrap;gap:5px;margin-top:9px;align-items:center">
    <span class="pill" style="background:#fff;color:var(--pu)">Regional</span>
    <span class="pill" style="background:#fff;color:var(--pu)">Centro zonal</span>
    <span class="pill" style="background:#fff;color:var(--pu)">Municipio</span>
    <span class="pill" style="background:#fff;color:var(--pu)">UDS</span>
  </div>
</div>'''

    # Fila D
    body += f'''
<div class="card tint-or" style="left:34px;top:884px;width:748px;height:92px;display:flex;gap:14px;align-items:center">
  <div class="hex hx-or" style="width:50px;height:56px">{ic('info',26)}</div>
  <div>
    <p style="font-size:12.6px;color:var(--ink)"><b>Cómo leer estas cifras.</b> Provienen de fuentes y años distintos (PARD a mayo de 2024, Observatorio de Violencias 2022 y EVCNNA 2018): <b>no se suman ni se comparan entre sí</b>. Detrás de cada número hay una niña o un niño que requiere protección.</p>
  </div>
</div>
<div class="src"><b>Fuentes:</b> ICBF Regional Antioquia, presentación «Prevención de violencias», 2024 (diap. 12-14); ICBF, <i>Modelos de probabilidad de vulneración</i> (EVCNNA 2018: OIM, CDC y MSPS, 2019). PARD: Proceso Administrativo de Restablecimiento de Derechos. ML: según rótulo de la presentación. Las cifras de Antioquia no indican fecha de corte en la presentación.</div>'''
    return page(body, 'I')
