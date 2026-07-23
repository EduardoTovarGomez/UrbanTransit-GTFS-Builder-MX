"""
Configuración global del proyecto
UrbanTransit GTFS Builder MX
"""

# ==========================
# Rutas
# ==========================
INPUT_FOLDER = "data/kml"
OUTPUT_FOLDER = "output"

# ==========================
# Agencia
# ==========================
AGENCY_ID = 1
AGENCY_NAME = "Secretaría de Movilidad y Transporte"
AGENCY_URL = "https://github.com/EduardoTovarGomez/urbantransit-gtfs-builder-mx"

# ==========================
# GTFS
# ==========================
TIMEZONE = "America/Mexico_City"
LANGUAGE = "es"
SERVICE_ID = "WEEKDAY"

START_DATE = "20260101"
END_DATE = "20261231"

FEED_VERSION = "0.8.0"

# ==========================================
# Spatial Engine
# ==========================================
# Distancia máxima (metros) para asociar una parada
MATCH_DISTANCE = 100

# Lado de circulación donde normalmente se
# encuentran las paradas.
#
# RIGHT -> países con circulación por la derecha
# LEFT  -> países con circulación por la izquierda
STOP_SIDE = "RIGHT"

# VELOCIDAD PROMEDIO DEL TRANSPORTE
SPEED_PROFILE = {

    "urban": 22,

    "downtown": 15,

    "highway": 45

}

# ==========================
# Servicio
# ==========================

FIRST_TRIP = "05:00:00"

LAST_TRIP = "21:30:00"

HEADWAY_MINUTES = 15

# ==========================
# Proyecto
# ==========================
PROJECT_NAME = "UrbanTransit GTFS Builder MX"
PROJECT_EDITION = "Professional Edition"
PROJECT_TAGLINE = (
    "Conversión de información geográfica "
    "en datos abiertos para el transporte."
)
AUTHOR = "Arq. Eduardo Tovar Gómez"
PROJECT_URL = (
    "https://github.com/EduardoTovarGomez/"
    "urbantransit-gtfs-builder-mx"
)

# ==========================
# Contacto del proyecto
# ==========================

CONTACT_EMAIL = "eduardo.tovar10@unach.mx"
CONTACT_URL = "https://github.com/EduardoTovarGomez/urbantransit-gtfs-builder-mx"

# ==========================
# Desarrollo
# ==========================

DEBUG = False