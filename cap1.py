# -*- coding: utf-8 -*-
from base import head, page, ic, recordar

BARS = [  # (etiqueta, valor, %, clase)
    ('Omisión o negligencia', 5117, '51,0', 'a'),
    ('Falta absoluta o temporal de responsables', 2200, '21,9', 'b'),
    ('Violencia sexual', 1066, '10,6', 'v'),
    ('Abandono (con o sin discapacidad)', 410, '4,1', 'a'),
    ('Violencia física', 214, '2,1', 'v'),
    ('Violencia psicológica', 131, '1,3', 'v'),
]
COL = {'a': 'var(--g)', 'b': 'var(--tl)', 'v': 'var(--pk)'}

OTROS = [  # (motivo, procesos)
    ('Otros motivos', 338),
    ('Reunificación familiar', 213),
    ('Conductas sexuales entre menores de 14 años', 167),
    ('Alta permanencia en calle', 78),
    ('Condiciones especiales de cuidadores', 27),
    ('Trabajo infantil', 26),
    ('Situación de vida en calle', 25),
    ('Uso o utilización de niña, niño o adolescente para un delito', 8),
    ('Situación de amenaza a la integridad', 7),
    ('Desnutrición', 4),
    ('Trata de personas', 2),
    ('Consumo de sustancias psicoactivas', 1),
]


def fmt(n):
    return f'{n:,}'.replace(',', '.')


def bars_html():
    mx = 5117
    out = ''
    for lab, val, pct, k in BARS:
        w = max(val / mx * 100, 2.2)
        out += f'''<div style="display:flex;align-items:center;gap:6px;height:26px">
  <div style="width:146px;font-size:10.8px;font-weight:700;color:var(--ink2);line-height:1.1">{lab}</div>
  <div style="flex:1;background:#eef2e9;border-radius:6px;height:15px"><div style="width:{w}%;height:15px;border-radius:6px;background:{COL[k]}"></div></div>
  <div style="width:80px;text-align:right;font-size:11.6px;font-weight:800;color:var(--ink)">{fmt(val)} <span style="font-weight:700;color:var(--muted);font-size:10.8px">{pct}%</span></div>
</div>'''
    return out


def otros_html():
    return ''.join(
        f'<span style="display:inline-flex;gap:5px;align-items:baseline;background:#f3f6ee;border-radius:99px;padding:2px 9px;font-size:10.8px;font-weight:700;color:var(--ink2);line-height:1.25">{m} <b style="color:var(--ink);font-size:11px">{v}</b></span>'
        for m, v in OTROS)


def leg(c, t):
    return f'<span style="display:inline-flex;align-items:center;gap:5px;margin-right:12px"><i style="width:11px;height:11px;border-radius:3px;background:{c};display:inline-block"></i>{t}</span>'


def html():
    hero = '<img class="hero" src="img/kid_01.png" style="right:26px;top:92px;width:196px" alt="">'
    body = head('I', 'Contexto y situación de las violencias',
                '1 de cada 2 procesos activos en el PARD de la primera infancia se abrió por <em>omisión o negligencia</em>',
                '¿Qué está pasando con niñas y niños de 0 a 5 años?', hero)

    # Fila A: total + 6 motivos principales (barras) + los otros 12 (lista)
    otros_li = ''.join(
        f'<div style="display:flex;justify-content:space-between;gap:8px;border-bottom:1px dotted #d3dcc8;padding:1.5px 0;font-size:10.8px;line-height:1.2;color:var(--ink2);font-weight:700"><span>{m}</span><b style="color:var(--ink);font-size:11.2px">{v}</b></div>'
        for m, v in OTROS)
    body += f'''
<div class="card" style="left:34px;top:284px;width:748px;height:318px;padding:12px 16px">
  <h3 style="margin-bottom:8px">{ic('layers',19)} ¿Por qué ingresan? Los 18 motivos de ingreso al PARD <span class="yr" style="color:var(--gd)">Mayo 2024</span></h3>
  <div style="display:flex;gap:22px;align-items:flex-start">
    <div style="width:352px;flex:none">
      <div style="background:var(--gd);border-radius:14px;color:#fff;padding:9px 14px;display:flex;align-items:center;gap:12px;height:76px">
        <div class="num" style="font-size:40px;color:#fff">10.034</div>
        <p style="color:#e9f4df;font-size:11.4px;line-height:1.3">procesos de niñas y niños de <b style="color:#fff">0 a 5 años</b> activos en el PARD (Proceso Administrativo de Restablecimiento de Derechos)</p>
      </div>
      <div style="font-size:11.4px;font-weight:800;color:var(--ink);margin:8px 0 3px">Los 6 principales: <b>9.138</b> procesos (91,1 %)</div>
      {bars_html()}
      <div style="font-size:10.8px;font-weight:700;color:var(--ink2);margin-top:5px">{leg('var(--pk)','Violencias')}{leg('var(--g)','Omisión y abandono')}{leg('var(--tl)','Falta de responsables')}</div>
    </div>
    <div style="flex:1;min-width:0">
      <div style="font-size:11.4px;font-weight:800;color:var(--ink);margin-bottom:4px">Los otros 12 motivos: <b>896</b> procesos (8,9 %)</div>
      {otros_li}
      <p style="font-size:10.8px;margin-top:8px;color:var(--muted)">Porcentajes sobre 10.034 procesos. Los 18 motivos suman 10.034.</p>
    </div>
  </div>
</div>'''

    # Fila B
    body += f'''
<div class="card tint-pk" style="left:34px;top:618px;width:366px;height:150px">
  <h3 style="color:#a02a52">{ic('alert',19)} Violencias reportadas · 0 a 5 años <span class="yr" style="color:#a02a52">2022</span></h3>
  <div style="display:flex;gap:12px">
    <div style="flex:1;background:#fff;border-radius:14px;padding:10px 10px 9px;text-align:center">
      <div class="num" style="font-size:34px;color:var(--pk)">2.222</div>
      <p style="font-size:12.4px;font-weight:700;color:var(--ink)">Violencia intrafamiliar</p></div>
    <div style="flex:1;background:#fff;border-radius:14px;padding:10px 10px 9px;text-align:center">
      <div class="num" style="font-size:34px;color:var(--pk)">2.546</div>
      <p style="font-size:12.4px;font-weight:700;color:var(--ink)">Violencia sexual</p></div>
  </div>
  <p style="font-size:11.2px;color:#7c3d56;margin-top:7px">Casos reportados · Observatorio de Violencias (ML)</p>
</div>
<div class="card tint-g" style="left:414px;top:618px;width:368px;height:150px;padding:11px 14px">
  <h3 style="margin-bottom:5px">{ic('pin',19)} Antioquia <span class="yr" style="color:var(--gd)">Sin fecha de corte</span></h3>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6px">
    <div style="background:#fff;border-radius:12px;padding:2px 10px 3px"><div class="num" style="font-size:19px;color:var(--pk)">328</div><div style="font-size:11.4px;font-weight:700;line-height:1.15">violencia intrafamiliar</div></div>
    <div style="background:#fff;border-radius:12px;padding:2px 10px 3px"><div class="num" style="font-size:19px;color:var(--pk)">384</div><div style="font-size:11.4px;font-weight:700;line-height:1.15">violencia sexual</div></div>
    <div style="background:#fff;border-radius:12px;padding:2px 10px 3px"><div class="num" style="font-size:19px">1.373</div><div style="font-size:11.4px;font-weight:700;line-height:1.15">PARD abiertos</div></div>
    <div style="background:#fff;border-radius:12px;padding:2px 10px 3px"><div class="num" style="font-size:19px">643</div><div style="font-size:11.4px;font-weight:700;line-height:1.15">omisión o negligencia</div></div>
  </div>
  <p style="font-size:10.8px;margin-top:5px;color:var(--ink2)"><b>Para comparar:</b> la más alta de los 8 departamentos de la presentación (cifras absolutas).</p>
</div>'''

    # Fila C
    body += f'''
<div class="card" style="left:34px;top:780px;width:476px;height:132px;padding:11px 16px">
  <h3 style="margin-bottom:6px">{ic('users',19)} La violencia empieza temprano <span class="yr" style="color:var(--gd)">2018</span></h3>
  <div style="display:flex;gap:16px;align-items:center">
    <svg width="92" height="92" viewBox="0 0 90 90" style="flex:none">
      <circle cx="45" cy="45" r="34" fill="none" stroke="#eef2e9" stroke-width="12"/>
      <circle cx="45" cy="45" r="34" fill="none" stroke="var(--pk)" stroke-width="12" stroke-dasharray="88.7 124.9" transform="rotate(-90 45 45)" stroke-linecap="round"/>
      <text x="45" y="47" text-anchor="middle" font-family="Poppins" font-weight="800" font-size="17" fill="#0f3b34">41,5%</text>
      <text x="45" y="59" text-anchor="middle" font-family="Nunito" font-weight="700" font-size="5.6" fill="#35564f">reportó violencia</text>
    </svg>
    <div style="flex:1">
      <p style="font-size:12.6px;margin-bottom:7px">De las personas de <b>18 a 24 años</b>, <b>41,5 %</b> reportó haber sufrido violencia antes de cumplir 18:</p>
      <div style="display:flex;gap:6px;flex-wrap:wrap">
        <span class="pill" style="background:var(--pkl);color:#a02a52">32,1 % física</span>
        <span class="pill" style="background:var(--pul);color:var(--pu)">15,2 % psicológica</span>
        <span class="pill" style="background:var(--orl);color:#8a5410">11,4 % sexual</span>
      </div>
      <p style="font-size:11px;color:var(--muted);margin-top:6px">EVCNNA 2018. Las formas de violencia pueden presentarse juntas.</p>
    </div>
  </div>
</div>
<div class="card tint-pu" style="left:524px;top:780px;width:258px;height:132px">
  <h3 style="color:var(--pu)">{ic('target',19)} Lectura territorial</h3>
  <p style="font-size:11.8px;color:var(--ink);font-weight:700;line-height:1.3">¿Cuáles son los tipos de violencia más frecuentes en tu territorio contra niñas y niños, desde la gestación hasta los cinco años?</p>
  <div style="margin-top:6px"><span class="pill" style="background:#fff;color:var(--pu);font-size:11px">Regional · Zonal · Municipio · UDS</span></div>
</div>'''

    # Fila D
    body += f'''
{recordar(924, 'Detrás de cada número hay una niña o un niño que requiere protección. <small>Las cifras vienen de fuentes y años distintos (2024, 2022 y 2018): no se suman ni se comparan entre sí. Conocer tu territorio es el primer paso para cuidarlo.</small>', 70)}
<div class="src"><b>Fuentes:</b> ICBF Regional Antioquia, presentación «Prevención de violencias», 2024 (diap. 12-14); ICBF, <i>Modelos de probabilidad de vulneración</i> (EVCNNA 2018: OIM, CDC y MSPS, 2019). PARD: Proceso Administrativo de Restablecimiento de Derechos. ML: según rótulo de la presentación. Las cifras de Antioquia no indican fecha de corte.</div>'''
    return page(body, 'I')
