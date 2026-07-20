# Changelog

Todos los cambios importantes del proyecto se documentan aquí.

---

# v0.8.0

## Added

- Time Engine
- Shape cumulative distances
- Automatic travel time calculation
- Dynamic schedules
- Automatic KML loader
- Automatic project naming
- ZIP named after project
- Cleaner console output
- DEBUG mode

## Improved

- Route matching
- Schedule generation
- Export process
- Console UI

## Fixed

- agency_id warnings
- GTFS validator warnings
- duplicated exporter messages

# v0.3.0 — Shape Engine

Fecha: Junio 2026

## Added

- Lectura de rutas desde archivos KML.
- Clase `Route`.
- Arquitectura orientada a objetos para rutas y paradas.
- Exportación automática de `routes.txt`.
- Exportación automática de `shapes.txt`.
- Conversión de coordenadas KML al formato GTFS.
- Mejora de la estructura del proyecto.

## Fixed

- Organización interna del parser.
- Refactorización del exportador.

v0.7.0
-------

Added
- RouteMatcher module
- Shape parsing
- Closest point algorithm
- Route matching structure
- Automatic GTFS ZIP generation
- feed_info.txt support
- Improved console interface

Improved
- Route parsing
- Route descriptions
- Project architecture