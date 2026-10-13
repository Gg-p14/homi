CASAS = [
    {"id": "1", "titulo": "Casa Jacaranda", "ciudad": "Tuxtla Gutiérrez", "precio": 950,
     "huespedes": 4, "recamaras": 2, "banos": 2, "calificacion": 4.8,
     "descripcion": "Casa familiar con jardín y estacionamiento, ideal para estancias tranquilas.",
     "condiciones": "Entrada a partir de las 15:00. Salida antes de las 12:00.",
     "servicios": ["Wi-Fi", "Estacionamiento", "Jardín"]},
    {"id": "2", "titulo": "Departamento Cerro Verde", "ciudad": "San Cristóbal de las Casas", "precio": 1200,
     "huespedes": 2, "recamaras": 1, "banos": 1, "calificacion": 4.9,
     "descripcion": "Departamento céntrico con vista a las montañas, cerca de la plaza.",
     "condiciones": "Entrada a partir de las 14:00. Salida antes de las 11:00.",
     "servicios": ["Wi-Fi", "Cocina equipada", "Lavadora"]},
    {"id": "3", "titulo": "Cabaña El Mirador", "ciudad": "Chiapa de Corzo", "precio": 1500,
     "huespedes": 6, "recamaras": 3, "banos": 2, "calificacion": 4.7,
     "descripcion": "Cabaña rodeada de naturaleza, ideal para grupos y escapadas.",
     "condiciones": "Entrada a partir de las 16:00. Salida antes de las 12:00.",
     "servicios": ["Alberca", "Estacionamiento", "Aire acondicionado"]},
]

RESERVAS = [
    {"casa_id": "1", "casa": "Casa Jacaranda", "fechas": "15 al 18 de noviembre de 2026",
     "total": 2850, "estado": "Pendiente"},
    {"casa_id": "3", "casa": "Cabaña El Mirador", "fechas": "2 al 5 de diciembre de 2026",
     "total": 4500, "estado": "Aceptada"},
]

SOLICITUDES = [
    {"huesped": "Laura Pérez", "casa": "Casa Jacaranda", "fechas": "15 al 18 de noviembre de 2026",
     "estado": "Pendiente"},
]

SERVICIOS = ["Wi-Fi", "Estacionamiento", "Alberca", "Aire acondicionado",
             "Cocina equipada", "Mascotas permitidas", "Lavadora", "Jardín"]

MENU = [
    ("explorar.html", "Encontrar"),
    ("reservas.html", "Mis reservaciones"),
    ("panel.html", "Mi panel"),
]

FILTROS_SERVICIOS = ["Wi-Fi", "Alberca", "Aire acondicionado",
                     "Cocina equipada", "Mascotas permitidas", "Jardín"]

BENEFICIOS = [
    ("Solo casas libres en tus fechas", "Al buscar por fechas, solo ves los alojamientos disponibles para esos días."),
    ("Toda la información en un lugar", "Precio, servicios, condiciones y reseñas, sin buscar en otras páginas."),
    ("Renta por el tiempo que quieras", "Desde una noche hasta temporadas largas, según lo que defina cada propietario."),
]
