/* Formulario "Informar un caso": ventana emergente compartida por la interfaz y el capítulo V. */
(function () {
  'use strict';
  var root = null;

  var CSS = '#rp-back{position:fixed;inset:0;z-index:9999;display:none;align-items:center;justify-content:center;padding:14px;background:rgba(15,59,52,.55);font-family:Nunito,"Segoe UI",system-ui,sans-serif}' +
    '#rp-back.open{display:flex}' +
    '#rp-box{background:#fffdf5;border-radius:22px;max-width:560px;width:100%;max-height:94vh;overflow:auto;box-shadow:0 20px 60px rgba(0,0,0,.35);border:6px solid #1d6a3a;color:#0f3b34}' +
    '#rp-box h2{font-family:Poppins,"Baloo 2",Nunito,sans-serif;font-size:22px;line-height:1.15;color:#1d6a3a;margin:0 0 4px}' +
    '#rp-box .in{padding:18px 20px 20px}' +
    '#rp-box .warn{background:#fdf0dc;border-radius:14px;padding:10px 13px;font-size:13.5px;line-height:1.4;margin:10px 0 12px;font-weight:700}' +
    '#rp-box .warn a{color:#1d6a3a}' +
    '#rp-box label{display:block;font-weight:800;font-size:13.5px;margin:10px 0 3px}' +
    '#rp-box label small{font-weight:600;color:#4a665f}' +
    '#rp-box input[type=text],#rp-box select,#rp-box textarea{width:100%;font:inherit;font-size:15px;padding:9px 11px;border:2px solid #cfe3bf;border-radius:12px;background:#fff;color:#0f3b34}' +
    '#rp-box textarea{min-height:110px;resize:vertical}' +
    '#rp-box input:focus,#rp-box select:focus,#rp-box textarea:focus{outline:3px solid #5aa832;border-color:#5aa832}' +
    '#rp-box .ck{display:flex;gap:9px;align-items:flex-start;font-size:13px;font-weight:700;margin-top:12px}' +
    '#rp-box .ck input{margin-top:3px;width:18px;height:18px;flex:none}' +
    '#rp-box .row{display:flex;gap:10px;flex-wrap:wrap}.row>div{flex:1;min-width:200px}' +
    '#rp-box .btns{display:flex;gap:10px;justify-content:flex-end;margin-top:16px;flex-wrap:wrap}' +
    '#rp-box button{font:inherit;font-weight:800;font-size:15px;border:0;border-radius:999px;padding:10px 22px;cursor:pointer}' +
    '#rp-box .send{background:#1d6a3a;color:#fff}#rp-box .send:disabled{opacity:.55;cursor:wait}' +
    '#rp-box .cancel{background:#e6f1dc;color:#1d6a3a}' +
    '#rp-box .msg{margin-top:10px;font-weight:800;font-size:14px}.msg.err{color:#b8325f}' +
    '#rp-box .ok{text-align:center;padding:10px 4px}.ok .big{font-size:44px}' +
    '#rp-box .hp{position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden}' +
    '.noexp{}html.exp .noexp{display:none!important}@media print{.noexp{display:none!important}}';

  var HTML = '<div id="rp-box" role="dialog" aria-modal="true" aria-labelledby="rp-t"><div class="in">' +
    '<div id="rp-form"><h2 id="rp-t">Informar un caso</h2>' +
    '<div class="warn">Si hay un <b>peligro inmediato</b>, llama al <b>123</b>. Para orientación y denuncias llama a la <a href="tel:141"><b>Línea 141</b></a> del ICBF (gratuita, 24 horas). Este formulario <b>no es un canal de atención inmediata</b> y no garantiza una respuesta.</div>' +
    '<form id="rp-f" novalidate>' +
    '<label for="rp-rol">¿Quién informa?</label><select id="rp-rol"><option>Conozco o presencié un caso</option><option>Soy la persona afectada</option><option>Soy familiar o cuidador</option><option>Soy agente educativo o del servicio</option><option>Prefiero no decirlo</option></select>' +
    '<label for="rp-relato">¿Qué está ocurriendo? <small>(obligatorio; no escribas datos que no sean necesarios)</small></label><textarea id="rp-relato" maxlength="3000" required></textarea>' +
    '<div class="row"><div><label for="rp-lugar">Lugar o municipio <small>(opcional)</small></label><input type="text" id="rp-lugar" maxlength="160"></div>' +
    '<div><label for="rp-cuando">¿Cuándo? <small>(opcional)</small></label><input type="text" id="rp-cuando" maxlength="120"></div></div>' +
    '<div class="row"><div><label for="rp-nombre">Tu nombre <small>(opcional)</small></label><input type="text" id="rp-nombre" maxlength="120" autocomplete="name"></div>' +
    '<div><label for="rp-contacto">Teléfono o correo <small>(opcional, solo si quieres que te contacten)</small></label><input type="text" id="rp-contacto" maxlength="160" autocomplete="off"></div></div>' +
    '<div class="hp" aria-hidden="true"><label>No llenar<input type="text" id="rp-web" tabindex="-1" autocomplete="off"></label></div>' +
    '<label class="ck"><input type="checkbox" id="rp-ok"><span>Entiendo que este formulario no es un canal de atención inmediata y acepto que mi mensaje se envíe por correo electrónico al equipo responsable.</span></label>' +
    '<div class="msg" id="rp-msg" role="alert"></div>' +
    '<div class="btns"><button type="button" class="cancel" id="rp-x">Cancelar</button><button type="submit" class="send" id="rp-s">Enviar</button></div></form></div>' +
    '<div id="rp-done" class="ok" style="display:none"><div class="big">💚</div><h2>Gracias por informar</h2>' +
    '<p style="font-size:14.5px;line-height:1.45;margin:8px 0 12px">Tu mensaje fue enviado. Si hay peligro inmediato llama al <b>123</b>; para orientación llama a la <b>Línea 141</b> del ICBF.</p>' +
    '<div class="btns" style="justify-content:center"><button type="button" class="send" id="rp-c">Cerrar</button></div></div>' +
    '</div></div>';

  function build() {
    if (root) return;
    var st = document.createElement('style'); st.textContent = CSS; document.head.appendChild(st);
    root = document.createElement('div'); root.id = 'rp-back'; root.innerHTML = HTML; document.body.appendChild(root);
    var $ = function (s) { return root.querySelector(s); };
    $('#rp-x').onclick = $('#rp-c').onclick = close;
    root.addEventListener('mousedown', function (e) { if (e.target === root) close(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && root.classList.contains('open')) { e.stopPropagation(); close(); } }, true);
    $('#rp-f').addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = $('#rp-msg'), btn = $('#rp-s'); msg.className = 'msg'; msg.textContent = '';
      var data = { rol: $('#rp-rol').value, relato: $('#rp-relato').value, lugar: $('#rp-lugar').value, cuando: $('#rp-cuando').value,
        nombre: $('#rp-nombre').value, contacto: $('#rp-contacto').value, web: $('#rp-web').value, acepto: $('#rp-ok').checked };
      if (data.relato.trim().length < 20) { msg.className = 'msg err'; msg.textContent = 'Cuéntanos un poco más de lo que ocurre (mínimo 20 caracteres).'; $('#rp-relato').focus(); return; }
      if (!data.acepto) { msg.className = 'msg err'; msg.textContent = 'Marca la casilla para poder enviar.'; return; }
      btn.disabled = true; btn.textContent = 'Enviando…';
      fetch('/api/reportar', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) })
        .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok && j.ok, j: j }; }); })
        .then(function (o) {
          if (o.ok) { $('#rp-form').style.display = 'none'; $('#rp-done').style.display = 'block'; $('#rp-f').reset(); }
          else { msg.className = 'msg err'; msg.textContent = (o.j && o.j.error) || 'No pudimos enviar el mensaje. Por favor llama a la Línea 141.'; }
        })
        .catch(function () { msg.className = 'msg err'; msg.textContent = 'Sin conexión. Por favor llama a la Línea 141.'; })
        .then(function () { btn.disabled = false; btn.textContent = 'Enviar'; });
    });
  }
  function open() { build(); root.querySelector('#rp-form').style.display = ''; root.querySelector('#rp-done').style.display = 'none'; root.classList.add('open'); setTimeout(function () { root.querySelector('#rp-relato').focus(); }, 50); }
  function close() { if (root) root.classList.remove('open'); }

  window.abrirReporte = open;
  /* Dentro del visor (iframe) se usa la ventana de la página principal, que es más grande. */
  window.abrirReporteDesdeInfografia = function () {
    try { if (window.parent !== window && window.parent.abrirReporte) return window.parent.abrirReporte(); } catch (e) {}
    open();
  };
  /* Al exportar PDF/PNG (URL con #export) o al imprimir, el botón no se muestra. */
  var st0 = document.createElement('style');
  st0.textContent = 'html.exp .noexp{display:none!important}@media print{.noexp{display:none!important}}';
  document.head.appendChild(st0);
  if (/#.*export/.test(location.hash)) document.documentElement.classList.add('exp');
})();
