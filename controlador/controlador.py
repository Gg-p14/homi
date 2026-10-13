import os

from modelo import datos
from vistas import vistas

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARPETA_PAGINAS = os.path.join(RAIZ, "paginas")


def rutas(en_raiz):
    if en_raiz:
        ruta = {"pagina": "paginas/", "inicio": "index.html", "css": "static/estilo.css", "static": "static/"}
    else:
        ruta = {"pagina": "", "inicio": "../index.html", "css": "../static/estilo.css", "static": "../static/"}
    ruta["menu"] = datos.MENU
    return ruta


def construir():
    raiz = rutas(True)
    r = rutas(False)

    paginas = {
        "explorar.html": vistas.explorar(datos.CASAS, datos.FILTROS_SERVICIOS, r),
        "acceso.html": vistas.acceso(r),
        "registro.html": vistas.registro(r),
        "panel.html": vistas.panel(datos.CASAS, datos.SOLICITUDES, r),
        "publicar.html": vistas.publicar(datos.SERVICIOS, r),
        "reservas.html": vistas.reservas(datos.RESERVAS, r),
        "404.html": vistas.no_encontrada(r),
    }
    for casa in datos.CASAS:
        paginas[f"casa-{casa['id']}.html"] = vistas.detalle(casa, r)

    os.makedirs(CARPETA_PAGINAS, exist_ok=True)
    for archivo in os.listdir(RAIZ):
        if archivo.endswith(".html") and archivo != "index.html":
            os.remove(os.path.join(RAIZ, archivo))

    with open(os.path.join(RAIZ, "index.html"), "w", encoding="utf-8") as archivo:
        archivo.write(vistas.inicio(datos.CASAS, datos.BENEFICIOS, raiz))

    for nombre, html in paginas.items():
        with open(os.path.join(CARPETA_PAGINAS, nombre), "w", encoding="utf-8") as archivo:
            archivo.write(html)

    return 1 + len(paginas)
