#!/bin/bash
# Uso: ./render.sh 1 2 ...  -> capituloN.png (2x) y capituloN.pdf (tamaño carta)
# Edge se lanza en segundo plano y escribe el archivo al terminar: se espera a que aparezca.
EDGE="/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
DIR="$(cd "$(dirname "$0")" && pwd -W)"
wait_for() { for i in $(seq 1 60); do [ -s "$1" ] && sleep 1 && return 0; sleep 1; done; return 1; }
for a in "$@"; do
  if [ "$a" = "0" ]; then n=0; B="portada"; else n=$a; B="capitulo$a"; fi
  rm -f "$DIR/$B.png" "$DIR/$B.pdf"
  "$EDGE" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 --window-size=816,1056 --virtual-time-budget=8000 --screenshot="$DIR/$B.png" "file:///$DIR/$B.html" >/dev/null 2>&1
  wait_for "$DIR/$B.png" || echo "sin PNG $n"
  "$EDGE" --headless=new --disable-gpu --no-pdf-header-footer --virtual-time-budget=8000 --print-to-pdf="$DIR/$B.pdf" "file:///$DIR/$B.html" >/dev/null 2>&1
  wait_for "$DIR/$B.pdf" || echo "sin PDF $n"
done
