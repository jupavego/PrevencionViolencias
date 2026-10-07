# Prevención de violencias en primera infancia

Infografías interactivas, tamaño carta, sobre la prevención de violencias contra niñas y niños de 0 a 5 años.
ICBF Regional Antioquia · Alcaldía de Bello.

## Qué contiene

| Archivo | Contenido |
|---|---|
| `index.html` | Interfaz principal: un cielo con globos aerostáticos, uno por pieza. Al tocar un globo se abre la infografía en un visor con desplazamiento, zoom, descarga en PDF e imagen y navegación entre piezas. |
| `portada.html` | Portada resumen de los cinco capítulos |
| `capitulo1.html` | I. Contexto y situación de las violencias |
| `capitulo2.html` | II. Las violencias y su incidencia |
| `capitulo3.html` | III. Enfoques y modelo de análisis |
| `capitulo4.html` | IV. Orientaciones para la prevención |
| `capitulo5.html` | V. Atención y restablecimiento de derechos |
| `*.pdf`, `*.png` | Versiones imprimibles (carta) de cada pieza |
| `img/` | Logos y ilustraciones |

Es un sitio estático: no necesita compilación. Basta con abrir `index.html` o publicar la carpeta.

## Enlaces directos a una pieza

`index.html#cap=0` (portada) hasta `index.html#cap=5`.

## Regenerar las piezas (opcional)

El contenido de cada infografía está en `cap0.py` … `cap5.py` y los estilos en `base.py`.

```bash
python build.py          # genera portada.html y capitulo1-5.html
./render.sh 0 1 2 3 4 5  # exporta PNG y PDF con Microsoft Edge (Windows)
```

## Fuentes

- ICBF Regional Antioquia, presentación «Prevención de violencias», 2024.
- Constitución Política de 1991; Ley 12 de 1991; Ley 1098 de 2006; Ley 1804 de 2016.
- ICBF, Plan Nacional de Acción contra la Violencia hacia la Niñez y la Adolescencia 2021-2024.
- ICBF, Política Nacional de Infancia y Adolescencia 2018-2030.
- ICBF, Modelos de probabilidad de vulneración (EVCNNA 2018).

Las cifras provienen de fuentes y años distintos y no deben sumarse ni compararse entre sí.
Las ilustraciones fueron generadas con herramientas de IA.
