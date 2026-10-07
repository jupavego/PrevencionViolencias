# -*- coding: utf-8 -*-
"""Estilos, íconos y piezas compartidas de las infografías (tamaño carta, 816x1056 px)."""

ICONS = {
 'shield': '<path d="M12 3l7 3v5c0 5-3.5 8-7 10-3.5-2-7-5-7-10V6z"/><path d="M9 12l2 2 4-4"/>',
 'heart': '<path d="M12 20s-7-4.5-7-10a4 4 0 0 1 7-2.5A4 4 0 0 1 19 10c0 5.5-7 10-7 10z"/>',
 'eye': '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 'bell': '<path d="M6 16v-5a6 6 0 0 1 12 0v5l2 2H4z"/><path d="M10 21h4"/>',
 'search': '<circle cx="11" cy="11" r="6.5"/><path d="M20 20l-4.5-4.5"/>',
 'bolt': '<path d="M13 2L5 14h6l-1 8 8-12h-6z"/>',
 'loop': '<path d="M20 12a8 8 0 1 1-2.5-5.8"/><path d="M20 4v4.5h-4.5"/>',
 'chat': '<path d="M4 5h16v11H9l-5 4z"/>',
 'users': '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.5 2.7-6 6-6s6 2.5 6 6"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14.2c3 .3 5 2.5 5 5.8"/>',
 'home': '<path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
 'pin': '<path d="M12 21s-7-6-7-11a7 7 0 0 1 14 0c0 5-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
 'chart': '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
 'alert': '<path d="M12 3l10 18H2z"/><path d="M12 10v5M12 18v.5"/>',
 'book': '<path d="M4 5a2 2 0 0 1 2-2h14v16H6a2 2 0 0 0-2 2z"/><path d="M4 19V5"/>',
 'scale': '<path d="M12 3v18M6 21h12M5 7h14"/><path d="M5 7l-3 7a3.5 3.5 0 0 0 6 0z"/><path d="M19 7l-3 7a3.5 3.5 0 0 0 6 0z"/>',
 'phone': '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>',
 'check': '<path d="M4 12l5 5 11-11"/>',
 'sprout': '<path d="M12 21v-8"/><path d="M12 13c0-4-3-6-7-6 0 4 3 6 7 6z"/><path d="M12 15c0-3 2-5 6-5 0 3-2 5-6 5z"/>',
 'bulb': '<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-4 10.5c1 1 1 2 1 3h6c0-1 0-2 1-3A6 6 0 0 0 12 3z"/>',
 'doc': '<path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5M9 13h7M9 17h7"/>',
 'info': '<circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8v.5"/>',
 'gender': '<circle cx="12" cy="9" r="5"/><path d="M12 14v8M9 19h6"/>',
 'face': '<circle cx="12" cy="12" r="9"/><path d="M8.5 15.5c1-1.2 2.2-1.8 3.5-1.8s2.5.6 3.5 1.8M9 10v.5M15 10v.5"/>',
 'layers': '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
 'target': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.2"/>',
 'crack': '<path d="M4 5h16v11H9l-5 4z"/><path d="M13 5l-2 4 3 2-2 5"/>',
 'hourglass': '<path d="M6 3h12M6 21h12M7 3c0 5 5 6 5 9s-5 4-5 9M17 3c0 5-5 6-5 9s5 4 5 9"/>',
 'spark': '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/>',
 'link': '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
}


def sprite():
    s = ''.join(
        f'<symbol id="i-{k}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
        f'stroke-linecap="round" stroke-linejoin="round">{v}</symbol>' for k, v in ICONS.items())
    return f'<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>{s}</defs></svg>'


def ic(name, size=22, cls=''):
    return f'<svg class="ic {cls}" width="{size}" height="{size}" aria-hidden="true"><use href="#i-{name}"/></svg>'


CSS = """
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&family=Poppins:wght@600;700;800&display=swap');
:root{
  --bg:#faf7ee; --ink:#0f3b34; --ink2:#35564f; --muted:#5f7a73;
  --g:#5aa832; --gd:#1d6a3a; --gl:#e6f1dc; --gx:#f1f7ea;
  --blue:#0b4a8f; --bl:#e3edf8;
  --or:#f0a336; --orl:#fdf0dc; --tl:#1f7f8a; --tll:#e0f1f2;
  --pu:#7a52a6; --pul:#eee6f6; --pk:#e0507c; --pkl:#fbe4ec;
  --line:#dfe6d6;
}
*{box-sizing:border-box;margin:0;padding:0}
@page{size:8.5in 11in;margin:0}
html,body{background:#cfd6c8}
body{font-family:'Nunito','Segoe UI',system-ui,sans-serif;color:var(--ink);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:816px;height:1056px;margin:0 auto;position:relative;overflow:hidden;background:var(--bg)}
@media print{html,body{background:none}.page{margin:0}}
.ic{display:inline-block;flex:none;vertical-align:middle}
h1,h2,h3,.pop{font-family:'Poppins','Nunito',sans-serif}
.dhex{position:absolute;width:70px;height:78px;border:1.5px solid #bfd9b0;clip-path:polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%);opacity:.7}
.hex{clip-path:polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%);display:flex;align-items:center;justify-content:center;color:#fff;font-family:'Poppins',sans-serif;font-weight:700;flex:none}
.hx-g{background:var(--g)} .hx-gd{background:var(--gd)} .hx-or{background:var(--or)} .hx-tl{background:var(--tl)} .hx-pu{background:var(--pu)} .hx-pk{background:var(--pk)} .hx-bl{background:var(--blue)}
.hdr{position:absolute;left:34px;right:34px;top:22px;height:64px;display:flex;align-items:center;gap:14px;z-index:3}
.hdr .l1{height:56px} .hdr .l2{height:38px}
.hdr .sep{width:2px;height:44px;background:var(--line)}
.hdr .org{margin-left:auto;text-align:right;font-size:12px;line-height:1.3;color:var(--ink2);position:relative;z-index:3}
.hdr .org b{display:block;font-family:'Poppins';font-size:13px;color:var(--gd)}
.ttl{position:absolute;left:34px;top:100px;width:520px;z-index:2}
.chip{display:inline-flex;align-items:center;gap:6px;background:var(--gl);color:var(--gd);font-family:'Poppins';font-weight:700;font-size:13px;letter-spacing:.06em;padding:5px 14px;border-radius:999px}
.ttl h1{font-size:33px;line-height:1.08;font-weight:800;color:var(--ink);margin:9px 0 8px;letter-spacing:-.01em}
.ttl h1 em{font-style:normal;color:var(--g)}
.ttl .q{font-size:15px;font-weight:700;color:var(--gd);line-height:1.3}
.ttl .bar{width:64px;height:5px;background:var(--gd);border-radius:3px;margin-top:10px}
.hero{position:absolute;z-index:1}
.card{position:absolute;background:#fff;border-radius:18px;box-shadow:0 1px 0 rgba(15,59,52,.05),0 6px 18px rgba(15,59,52,.07);padding:13px 15px}
.card h3{font-size:14px;font-weight:700;color:var(--gd);display:flex;align-items:center;gap:7px;line-height:1.2;margin-bottom:7px}
.card p,.card li{font-size:12.2px;line-height:1.36;color:var(--ink2)}
.card b{color:var(--ink)}
.tint-g{background:var(--gx)} .tint-or{background:var(--orl)} .tint-tl{background:var(--tll)} .tint-pu{background:var(--pul)} .tint-pk{background:var(--pkl)} .tint-bl{background:var(--bl)}
.pill{display:inline-block;font-size:11.2px;font-weight:700;padding:3px 10px;border-radius:999px;background:var(--gl);color:var(--gd)}
.num{font-family:'Poppins';font-weight:800;color:var(--gd);line-height:1}
.src{position:absolute;left:34px;right:34px;bottom:14px;font-size:9.6px;line-height:1.35;color:var(--muted);border-top:1px solid var(--line);padding-top:6px}
.src b{color:var(--ink2)}
.q-quote{font-style:italic}
"""


def head(ch_roman, title_html, question, hero_html=''):
    return f'''
<div class="dhex" style="right:-18px;top:-26px;width:110px;height:122px;background:#e3efd8;border:none;opacity:1"></div>
<div class="dhex" style="right:80px;top:-34px;width:60px;height:66px"></div>
<div class="hdr">
  <img class="l1" src="img/logo-icbf.png" alt="ICBF Bienestar Familiar">
  <div class="sep"></div>
  <img class="l2" src="img/logo-bello.png" alt="Alcaldía de Bello">
  <div class="org"><b>Regional Antioquia</b>Prevención de violencias · Primera infancia</div>
</div>
<div class="ttl">
  <span class="chip">CAPÍTULO {ch_roman}</span>
  <h1>{title_html}</h1>
  <div class="q">{question}</div>
  <div class="bar"></div>
</div>
{hero_html}'''


def page(body, ch_roman):
    return f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=816">
<title>Capítulo {ch_roman} · Prevención de violencias en primera infancia</title>
<style>{CSS}</style></head>
<body>{sprite()}
<div class="page">{body}</div>
</body></html>'''
