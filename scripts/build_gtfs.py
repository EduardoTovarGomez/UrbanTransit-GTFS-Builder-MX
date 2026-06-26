from pathlib import Path
import xml.etree.ElementTree as ET
import csv

print("=" * 45)
print("     TUXTLA GTFS BUILDER")
print("=" * 45)

# Ruta del archivo KML
kml_file = Path("data/kml/RutaA Tuxtla.kml")

if not kml_file.exists():
    print("❌ No se encontró el archivo.")
    exit()

print(f"✅ Archivo encontrado: {kml_file.name}")

# Leer el KML
tree = ET.parse(kml_file)
root = tree.getroot()

print("\n📄 KML cargado correctamente.")

# Namespace de KML
ns = {"kml": "http://www.opengis.net/kml/2.2"}

placemarks = root.findall(".//kml:Placemark", ns)

print(f"📍 Se encontraron {len(placemarks)} elementos Placemark.\n")

stops = []
routes = []

print("Analizando elementos...\n")

for placemark in placemarks:

    nombre = placemark.find("kml:name", ns)

    if nombre is None:
        continue

    nombre = nombre.text.strip()

    punto = placemark.find("kml:Point", ns)
    linea = placemark.find("kml:LineString", ns)

    # ------------------------
    # PARADA
    # ------------------------
    if punto is not None:

        coords = punto.find("kml:coordinates", ns)

        if coords is None:
            continue

        lon, lat, *_ = coords.text.strip().split(",")

        stop = {
            "id": len(stops) + 1,
            "name": nombre,
            "lat": float(lat),
            "lon": float(lon)
        }

        stops.append(stop)

        print(f"🚌 {nombre}")
        print(f"   Lat: {lat}")
        print(f"   Lon: {lon}\n")

    # ------------------------
    # RUTA
    # ------------------------
    elif linea is not None:

        coords = linea.find("kml:coordinates", ns)

        if coords is None:
            continue

        puntos = coords.text.strip().split()

        routes.append({
            "name": nombre,
            "points": puntos
        })

        print(f"🛣️ Ruta: {nombre}")
        print(f"   Tiene {len(puntos)} puntos\n")

print("=" * 45)
print("RESUMEN")
print("=" * 45)

print(f"Paradas encontradas: {len(stops)}")
print(f"Rutas encontradas: {len(routes)}")

print("\nListado de paradas:\n")

for stop in stops:
    print(stop)

print("\nListado de rutas:\n")

for route in routes:
    print(f"{route['name']} -> {len(route['points'])} puntos")

output = Path("output")
output.mkdir(exist_ok=True)

stops_file = output / "stops.txt"

with open(stops_file, "w", newline="", encoding="utf-8") as f:

    writer = csv.writer(f)

    writer.writerow([
        "stop_id",
        "stop_name",
        "stop_lat",
        "stop_lon"
    ])

    for stop in stops:

        writer.writerow([
            stop["id"],
            stop["name"],
            stop["lat"],
            stop["lon"]
        ])

print("\n✅ Archivo stops.txt generado correctamente.")