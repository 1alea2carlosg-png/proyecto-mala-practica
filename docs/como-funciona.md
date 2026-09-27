# Extractor de PDF: cómo funciona

El Extractor de PDF te permite ver en pantalla el texto de un archivo PDF y descargarlo como archivo de texto (`.txt`), por ejemplo para copiarlo, editarlo o buscar en él.

## Pasos

### 1. Abre la aplicación

Entra en la dirección de la aplicación con tu navegador (Chrome, Edge, Firefox…). Si la usas en tu propio ordenador, la dirección es:

```
http://127.0.0.1:5000
```

Verás el título **Extractor de PDF** y un botón azul **CARGAR PDF**.

### 2. Carga tu PDF

1. Pulsa **CARGAR PDF**.
2. Se abre la ventana para elegir archivos. Busca tu PDF y selecciónalo.
3. No hace falta pulsar nada más: el archivo se sube y se procesa solo.

### 3. Revisa el texto

En unos segundos aparece:

- El **nombre del archivo** que cargaste.
- El **texto de cada página**, en un recuadro con su número («Página 1», «Página 2»…).

### 4. Exporta a TXT

Debajo de la última página está el botón **Exportar a TXT**. Al pulsarlo, se descarga un archivo `.txt` con todo el texto. Dentro del archivo, cada página empieza con una línea como esta:

```
--- Página 1 ---
```

El archivo se guarda en tu carpeta de **Descargas**, con el mismo nombre que el PDF. Puedes abrirlo con el Bloc de notas o con cualquier editor de texto.

### ¿Quieres procesar otro PDF?

Pulsa de nuevo **CARGAR PDF** y elige otro archivo. El texto del nuevo PDF sustituye al anterior.

## Mensajes que puedes ver

| Mensaje | Qué significa | Qué hacer |
|---|---|---|
| **El archivo debe tener extensión .pdf** | Elegiste un archivo que no es PDF (una imagen, un Word…). | Elige un archivo terminado en `.pdf`. |
| **No se pudo leer el PDF** | El archivo está dañado o no es un PDF de verdad, aunque su nombre termine en `.pdf`. | Prueba a abrirlo en tu ordenador. Si tampoco abre, consigue otra copia del archivo. |
| **(Esta página no contiene texto extraíble)** | Esa página no tiene texto, o su texto es en realidad una imagen. | Consulta la sección «Límites». |
| **Selecciona un archivo PDF.** | Se envió el formulario sin ningún archivo. | Pulsa **CARGAR PDF** y elige un archivo. |

## Límites

- **Tamaño máximo: 20 MB por archivo.** Si tu PDF pesa más, la aplicación lo rechazará.
- **PDF escaneados:** si el PDF es una foto o un escaneo de papel, sus páginas son imágenes y no tienen texto que extraer. En ese caso verás el mensaje «(Esta página no contiene texto extraíble)». Para esos archivos necesitas una herramienta de reconocimiento de texto (OCR).
- **Formato:** solo se extrae el **texto**. Las imágenes, tablas, colores y tipos de letra no se conservan. En algunos PDF, las columnas o las tablas pueden aparecer con el texto algo desordenado.

## Privacidad

Los PDF que cargas se guardan en una carpeta temporal del equipo donde funciona la aplicación, para poder generar después el TXT. No se envían a ningún otro sitio. De momento no se borran automáticamente. Si la aplicación funciona en un equipo que no es tuyo, evita cargar documentos con información confidencial.
