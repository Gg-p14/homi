def pagina(titulo, contenido, r):
    enlaces = "".join(f'<a href="{r["pagina"]}{destino}">{texto}</a>' for destino, texto in r["menu"])
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{titulo} · Homi</title>
  <link rel="stylesheet" href="{r['css']}">
</head>
<body>
  <header class="cabecera">
    <div class="contenedor fila-cabecera">
      <a href="{r['inicio']}" class="logo">Homi</a>
      <nav class="menu">
        {enlaces}
        <a class="btn-menu" href="{r['pagina']}acceso.html">Usuario</a>
      </nav>
    </div>
  </header>

  <main class="contenedor">
    {contenido}
  </main>

  <footer class="pie">
    <div class="contenedor pie-grid">
      <div>
        <p class="logo">Homi</p>
        <p class="gris">Tu casa por el tiempo que tú quieras.</p>
      </div>
      <div>
        <p class="titulo-pie">Encontrar</p>
        <a href="{r['pagina']}explorar.html">Alojamientos</a>
        <a href="{r['pagina']}reservas.html">Mis reservaciones</a>
      </div>
      <div>
        <p class="titulo-pie">Anfitriones</p>
        <a href="{r['pagina']}panel.html">Mi panel</a>
      </div>
      <div>
        <p class="titulo-pie">Cuenta</p>
        <a href="{r['pagina']}acceso.html">Usuario</a>
        <a href="{r['pagina']}registro.html">Crear cuenta</a>
      </div>
    </div>
    <div class="contenedor pie-legal">Homi · Proyecto del equipo más perrón, equipo 3</div>
  </footer>
</body>
</html>"""


def ilustracion(numero, clase="ilustracion"):
    colores = [("#3b1452", "#c30df5"), ("#14283a", "#6aa9ff"), ("#2c1d10", "#e0a040")]
    fondo, techo = colores[int(numero) % len(colores)]
    return f"""<svg class="{clase}" viewBox="0 0 160 120" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Ilustración de una casa">
  <rect width="160" height="120" rx="12" fill="{fondo}"/>
  <polygon points="80,20 130,58 30,58" fill="{techo}"/>
  <rect x="42" y="58" width="76" height="50" fill="#f2f2f2"/>
  <rect x="70" y="76" width="20" height="32" fill="{fondo}"/>
  <rect x="50" y="68" width="14" height="12" fill="{fondo}"/>
  <rect x="96" y="68" width="14" height="12" fill="{fondo}"/>
</svg>"""


def imagen_casa(casa, r):
    return (ilustracion(casa["id"], "ilustracion-fondo")
            + f'<img class="foto-real" src="{r["static"]}fotos/casa-{casa["id"]}.jpg" '
            + f'alt="Foto de {casa["titulo"]}" onerror="this.remove()">')


def tarjeta(casa, r):
    return f"""<a class="tarjeta" href="{r['pagina']}casa-{casa['id']}.html">
  <div class="foto">{imagen_casa(casa, r)}<span class="etiqueta-foto">★ {casa['calificacion']}</span></div>
  <div class="tarjeta-info">
    <p class="ciudad">{casa['ciudad']}</p>
    <h3>{casa['titulo']}</h3>
    <p class="precio"><strong>${casa['precio']:,}</strong> <span>por noche</span></p>
  </div>
</a>"""


def cuadricula(casas, r):
    return '<section class="cuadricula">' + "".join(tarjeta(c, r) for c in casas) + "</section>"


def buscador(r, extra=""):
    return f"""<form class="buscador" action="{r['pagina']}explorar.html">
  <div class="pastilla">
    <div class="campo-pill">
      <label for="destino">Destino</label>
      <input id="destino" name="destino" placeholder="¿A dónde vas?">
    </div>
    <div class="campo-pill">
      <label for="entrada">Entrada</label>
      <input id="entrada" type="date" name="entrada">
    </div>
    <div class="campo-pill">
      <label for="salida">Salida</label>
      <input id="salida" type="date" name="salida">
    </div>
    <div class="campo-pill">
      <label for="huespedes">Huéspedes</label>
      <input id="huespedes" type="number" name="huespedes" min="1" placeholder="1">
    </div>
    <button class="btn-buscar" type="submit">Buscar</button>
  </div>
  {extra}
</form>"""


def _beneficios(beneficios, r):
    tarjetas = "".join(
        f'<div class="beneficio"><h3>{titulo}</h3><p class="gris">{texto}</p></div>'
        for titulo, texto in beneficios
    )
    return f"""<section class="beneficios">{tarjetas}</section>
<div class="cta-centro"><a class="boton" href="{r['pagina']}explorar.html">Explorar alojamientos</a></div>"""


def inicio(casas, beneficios, r):
    return pagina("Inicio", f"""<section class="hero">
  <p class="etiqueta-hero">Tu casa por el tiempo que tú quieras</p>
  <h1>Tu próxima aventura<br>está por comenzar</h1>
  <p class="gris">Encuentra alojamientos con todo lo que necesitas, al alcance de tus manos con solo un clic.</p>
</section>

{buscador(r)}
{_beneficios(beneficios, r)}

<div class="seccion-cabecera">
  <h2>Alojamientos destacados</h2>
  <a class="subrayado" href="{r['pagina']}explorar.html">Ver todos →</a>
</div>
{cuadricula(casas, r)}

<section class="banner">
  <div>
    <h2>¿Tienes una casa para rentar?</h2>
    <p class="gris">Publica en Homi y recibe dinerito.</p>
  </div>
  <a class="boton" href="{r['pagina']}publicar.html">Publicar mi casa</a>
</section>""", r)


def explorar(casas, servicios, r):
    chips = "".join(
        f'<label class="chip"><input type="checkbox" name="servicio"> {s}</label>'
        for s in servicios
    )
    filtros = f"""<details class="filtros">
    <summary>Más filtros</summary>
    <div class="filtros-caja">
      <div class="campo">
        <label for="precio">Precio máximo por noche</label>
        <input id="precio" type="number" name="precio" placeholder="Sin límite">
      </div>
      <div class="campo ancho">
        <span class="etiqueta">Servicios</span>
        <div class="chips">{chips}</div>
      </div>
    </div>
  </details>"""
    return pagina("Encontrar", f"""<h1>Alojamientos disponibles</h1>
<p class="gris">Busca por destino, fechas y número de huéspedes.</p>
{buscador(r, filtros)}
<p class="gris resultados">{len(casas)} alojamiento(s)</p>
{cuadricula(casas, r)}""", r)


def detalle(casa, r):
    servicios = "".join(f"<li>{s}</li>" for s in casa["servicios"])
    galeria = ('<div class="galeria"><div class="foto foto-principal">' + imagen_casa(casa, r)
               + '</div>' + '<div class="foto foto-chica"></div>' * 4 + "</div>")
    return pagina(casa["titulo"], f"""<p class="migas">
  <a href="{r['inicio']}">Inicio</a> / <a href="{r['pagina']}explorar.html">Encontrar</a> / {casa['titulo']}
</p>
<h1>{casa['titulo']}</h1>
<p class="gris">★ {casa['calificacion']} · {casa['ciudad']}</p>

{galeria}

<div class="detalle">
  <div>
    <h2>Sobre este alojamiento</h2>
    <p>{casa['descripcion']}</p>
    <p class="gris">{casa['huespedes']} huéspedes · {casa['recamaras']} recámara(s) · {casa['banos']} baño(s)</p>

    <h2>Servicios</h2>
    <ul class="lista">{servicios}</ul>

    <h2>Condiciones</h2>
    <p>{casa['condiciones']}</p>
  </div>

  <aside class="reserva">
    <p class="precio-grande"><strong>${casa['precio']:,}</strong> por noche</p>
    <form action="{r['pagina']}reservas.html">
      <div class="campo">
        <label for="entrada">Entrada</label>
        <input id="entrada" type="date" name="entrada">
      </div>
      <div class="campo">
        <label for="salida">Salida</label>
        <input id="salida" type="date" name="salida">
      </div>
      <div class="campo">
        <label for="huespedes">Huéspedes (máximo {casa['huespedes']})</label>
        <input id="huespedes" type="number" name="huespedes" min="1" placeholder="1">
      </div>
      <button class="boton boton-bloque" type="submit">Solicitar reservación</button>
    </form>
    <p class="pequeno gris">Es una solicitud: el propietario la acepta o la rechaza.</p>
    <p class="pequeno"><a class="subrayado" href="{r['pagina']}acceso.html">Inicia sesión</a> para reservar.</p>
  </aside>
</div>""", r)


def acceso(r):
    return pagina("Usuario", f"""<div class="formulario-centrado"><section class="seccion">
  <h1>Bienvenido a Homi</h1>
  <p class="gris">Inicia sesión para reservar o publicar tus casas.</p>
  <form action="{r['pagina']}panel.html">
    <div class="campo"><label for="correo">Correo</label><input id="correo" type="email" placeholder="tu@correo.com"></div>
    <div class="campo"><label for="clave">Contraseña</label><input id="clave" type="password"></div>
    <button class="boton boton-bloque" type="submit">Entrar</button>
  </form>
  <p class="pequeno gris">¿No tienes cuenta? <a class="subrayado" href="{r['pagina']}registro.html">Crea una</a></p>
</section></div>""", r)


def registro(r):
    return pagina("Crear cuenta", f"""<div class="formulario-centrado"><section class="seccion">
  <h1>Crea tu cuenta</h1>
  <p class="gris">Reserva casas o rentar las tuyas.</p>
  <form action="{r['pagina']}acceso.html">
    <div class="campo"><label for="nombre">Nombre</label><input id="nombre"></div>
    <div class="campo"><label for="correo">Correo</label><input id="correo" type="email"></div>
    <div class="campo"><label for="clave">Contraseña</label><input id="clave" type="password"></div>
    <div class="campo"><label for="rol">Quiero</label>
      <select id="rol"><option>Reservar casas</option><option>Rentar mis casas</option></select></div>
    <button class="boton boton-bloque" type="submit">Crear cuenta</button>
  </form>
  <p class="pequeno gris">¿Ya tienes cuenta? <a class="subrayado" href="{r['pagina']}acceso.html">Inicia sesión</a></p>
</section></div>""", r)


def _estadisticas(casas, solicitudes):
    pendientes = sum(1 for s in solicitudes if s["estado"] == "Pendiente")
    promedio = sum(c["calificacion"] for c in casas) / len(casas) if casas else 0
    return f"""<div class="estadisticas">
  <div class="estadistica"><strong>{len(casas)}</strong><span>Alojamientos publicados</span></div>
  <div class="estadistica"><strong>{pendientes}</strong><span>Solicitudes pendientes</span></div>
  <div class="estadistica"><strong>★ {promedio:.1f}</strong><span>Calificación promedio</span></div>
</div>"""


def panel(casas, solicitudes, r):
    filas_casas = "".join(f"""<div class="fila-item">
  <div><strong>{c['titulo']}</strong><br><span class="gris">{c['ciudad']} · ${c['precio']:,} por noche</span></div>
  <div class="acciones">
    <a class="subrayado" href="{r['pagina']}publicar.html">Editar</a>
    <a class="subrayado" href="{r['pagina']}casa-{c['id']}.html">Ver</a>
  </div>
</div>""" for c in casas)

    filas_solicitudes = "".join(f"""<div class="fila-item">
  <div><strong>{s['casa']}</strong> · {s['huesped']}<br><span class="gris">{s['fechas']}</span></div>
  <div>
    <span class="estado {s['estado'].lower()}">{s['estado']}</span>
    <div class="acciones">
      <button class="boton" type="button">Aceptar</button>
      <button class="boton-2" type="button">Rechazar</button>
    </div>
  </div>
</div>""" for s in solicitudes)

    return pagina("Mi panel", f"""<div class="encabezado-pagina">
  <div>
    <h1>Mi panel</h1>
    <p class="gris">Administra tus alojamientos y responde las solicitudes.</p>
  </div>
  <a class="boton" href="{r['pagina']}publicar.html">+ Publicar alojamiento</a>
</div>

{_estadisticas(casas, solicitudes)}

<section class="seccion">
  <h2>Mis alojamientos</h2>
  {filas_casas}
</section>

<section class="seccion">
  <h2>Solicitudes recibidas</h2>
  {filas_solicitudes}
</section>""", r)


def publicar(servicios, r):
    casillas = "".join(
        f'<label class="chip"><input type="checkbox" name="servicio"> {s}</label>'
        for s in servicios
    )
    return pagina("Publicar alojamiento", f"""<div class="encabezado-pagina">
  <div>
    <h1>Publica tu alojamiento</h1>
    <p class="gris">Completa los datos. Las fotos se agregarán después.</p>
  </div>
</div>

<form action="{r['pagina']}panel.html">
  <section class="seccion">
    <h2>Información básica</h2>
    <div class="campo"><label for="titulo">Nombre del alojamiento</label>
      <input id="titulo" placeholder="Ej. Casa con jardín"></div>
    <div class="campo"><label for="descripcion">Descripción</label>
      <textarea id="descripcion"></textarea></div>
  </section>

  <section class="seccion">
    <h2>Ubicación y capacidad</h2>
    <div class="dos">
      <div class="campo"><label for="ciudad">Ciudad</label><input id="ciudad"></div>
      <div class="campo"><label for="direccion">Dirección o colonia</label><input id="direccion"></div>
    </div>
    <div class="dos">
      <div class="campo"><label for="precio">Precio por noche (MXN)</label><input id="precio" type="number"></div>
      <div class="campo"><label for="huespedes">Huéspedes máximo</label><input id="huespedes" type="number"></div>
    </div>
  </section>

  <section class="seccion">
    <h2>Servicios</h2>
    <div class="chips">{casillas}</div>
  </section>

  <section class="seccion">
    <h2>Fotos</h2>
    <div class="foto-pequena"></div>
  </section>

  <div class="acciones">
    <button class="boton" type="submit">Publicar alojamiento</button>
    <a class="boton-2" href="{r['pagina']}panel.html">Cancelar</a>
  </div>
</form>""", r)


def reservas(filas, r):
    bloques = "".join(f"""<article class="reserva-tarjeta">
  {ilustracion(f['casa_id'])}
  <div class="reserva-info">
    <span class="estado {f['estado'].lower()}">{f['estado']}</span>
    <h2>{f['casa']}</h2>
    <p class="gris">{f['fechas']}</p>
    <p><strong>${f['total']:,}</strong> en total</p>
    <a class="subrayado" href="{r['pagina']}casa-{f['casa_id']}.html">Ver alojamiento</a>
  </div>
</article>""" for f in filas)

    return pagina("Mis reservaciones", f"""<div class="encabezado-pagina">
  <div>
    <h1>Mis reservaciones</h1>
    <p class="gris">Revisa el estado de tus solicitudes.</p>
  </div>
</div>
{bloques}""", r)


def no_encontrada(r):
    return pagina("No encontrada", f"""<section class="hero">
  <h1>Página no encontrada</h1>
  <p class="gris">La dirección que buscas no existe.</p>
  <p><a class="boton" href="{r['inicio']}">Volver al inicio</a></p>
</section>""", r)
