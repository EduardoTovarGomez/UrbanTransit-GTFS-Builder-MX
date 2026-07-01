from gtfs_builder.parser import KMLParser
from gtfs_builder.exporter import GTFSExporter
from gtfs_builder.trip_generator import TripGenerator
from gtfs_builder.schedule_generator import ScheduleGenerator
from gtfs_builder import config
from gtfs_builder.validator import ProjectValidator

print("=" * 45)
print("UrbanTransit GTFS Builder MX")
print("=" * 45)

# ==========================================
# Cargar y analizar KML
# ==========================================

parser = KMLParser(config.INPUT_KML)

parser.load()
parser.parse()

validator = ProjectValidator(parser)
validator.validate()


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
# Generar horarios
# ==========================================

schedule_generator = ScheduleGenerator()

stop_times = schedule_generator.generate(
    trips,
    parser.stops
)

# ==========================================
# Exportar archivos GTFS
# ==========================================

exporter = GTFSExporter()

exporter.export_stops(parser.stops)
exporter.export_routes(parser.routes)
exporter.export_shapes(parser.routes)
exporter.export_trips(trips)
exporter.export_stop_times(stop_times)
exporter.export_agency()
exporter.export_calendar()
exporter.export_feed_info()