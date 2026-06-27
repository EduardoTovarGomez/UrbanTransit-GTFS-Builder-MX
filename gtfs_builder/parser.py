import xml.etree.ElementTree as ET
from pathlib import Path

from gtfs_builder.models import Stop, Route


class KMLParser:

    def __init__(self, file_path):

        self.file_path = Path(file_path)

        self.tree = None
        self.root = None

        self.stops = []
        self.routes = []

    def load(self):

        self.tree = ET.parse(self.file_path)
        self.root = self.tree.getroot()

        print("✅ KML cargado correctamente.")

    def parse(self):

        print("\nAnalizando elementos...\n")

        placemarks = self.root.findall(
            ".//{http://www.opengis.net/kml/2.2}Placemark"
        )

        print(f"Se encontraron {len(placemarks)} elementos.\n")

        for placemark in placemarks:

            nombre = placemark.find(
                "{http://www.opengis.net/kml/2.2}name"
            )

            if nombre is None:
                continue

            punto = placemark.find(
                "{http://www.opengis.net/kml/2.2}Point"
            )

            linea = placemark.find(
                "{http://www.opengis.net/kml/2.2}LineString"
            )

            # -------- PARADAS --------

            if punto is not None:

                coords = punto.find(
                    "{http://www.opengis.net/kml/2.2}coordinates"
                )

                if coords is None:
                    continue

                lon, lat, *_ = coords.text.strip().split(",")

                stop = Stop(
                    stop_id=len(self.stops) + 1,
                    name=nombre.text,
                    lat=float(lat),
                    lon=float(lon)
                )

                self.stops.append(stop)

                print(f"🚌 {stop}")

            # -------- RUTAS --------

            elif linea is not None:

                coords = linea.find(
                    "{http://www.opengis.net/kml/2.2}coordinates"
                )

                if coords is None:
                    continue

                puntos = coords.text.strip().split()

                route = Route(
                    route_id=len(self.routes) + 1,
                    name=nombre.text,
                    points=puntos
                )

                self.routes.append(route)

                print(f"🛣️ {route}")