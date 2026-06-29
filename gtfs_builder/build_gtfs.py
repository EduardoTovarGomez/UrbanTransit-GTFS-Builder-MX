from gtfs_builder.parser import KMLParser
from gtfs_builder.exporter import GTFSExporter
from gtfs_builder.trip_generator import TripGenerator

print("=" * 45)
print("UrbanTransit GTFS Builder MX")
print("=" * 45)

# ==========================================
# Cargar y analizar KML
# ==========================================

parser = KMLParser("data/kml/RutaA Tuxtla.kml")

parser.load()
parser.parse()

print("\n" + "=" * 35)
print("RESUMEN DEL PROYECTO")
print("=" * 35)

print(f"Paradas almacenadas : {len(parser.stops)}")
print(f"Rutas almacenadas   : {len(parser.routes)}")

# ==========================================
# Generar viajes
# ==========================================

trip_generator = TripGenerator()

trips = trip_generator.generate(parser.routes)

# ==========================================
# Exportar archivos GTFS
# ==========================================

exporter = GTFSExporter()

exporter.export_stops(parser.stops)
exporter.export_routes(parser.routes)
exporter.export_shapes(parser.routes)
exporter.export_trips(trips)