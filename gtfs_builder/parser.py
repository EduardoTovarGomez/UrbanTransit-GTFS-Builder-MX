import xml.etree.ElementTree as ET
from pathlib import Path

from gtfs_builder import config
from gtfs_builder.models import Stop, Route


class KMLParser:

    def __init__(self, file_path):

        self.file_path = Path(file_path)

        self.tree = None
        self.root = None

        self.stops = []
        self.routes = []

    # =====================================================
    # LOAD
    # =====================================================

    def load(self):

        self.tree = ET.parse(self.file_path)
        self.root = self.tree.getroot()

        print("✅ KML cargado correctamente.")

    # =====================================================
    # PARSE
    # =====================================================

    def parse(self):

        print("\n🔍 Analizando archivo KML...")

        placemarks = self.root.findall(
            ".//{http://www.opengis.net/kml/2.2}Placemark"
        )

        if config.DEBUG:

            print(
                f"\nSe encontraron "
                f"{len(placemarks)} elementos.\n"
            )

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

            # =================================================
            # STOPS
            # =================================================

            if punto is not None:

                coords = punto.find(
                    "{http://www.opengis.net/kml/2.2}coordinates"
                )

                if coords is None:
                    continue

                lon, lat, *_ = coords.text.strip().split(",")

                stop = Stop(
                    stop_id=len(self.stops) + 1,
                    name=nombre.text.strip(),
                    lat=float(lat),
                    lon=float(lon)
                )

                self.stops.append(stop)

                if config.DEBUG:

                    print(f"🚌 {stop}")

            # =================================================
            # ROUTES
            # =================================================

            elif linea is not None:

                coords = linea.find(
                    "{http://www.opengis.net/kml/2.2}coordinates"
                )

                if coords is None:
                    continue

                description = placemark.find(
                    "{http://www.opengis.net/kml/2.2}description"
                )

                description_text = ""

                if (
                    description is not None
                    and description.text
                ):
                    description_text = (
                        description.text.strip()
                    )

                points = coords.text.strip().split()

                route = Route(
                    route_id=len(self.routes) + 1,
                    name=nombre.text.strip(),
                    description=description_text,
                    points=points
                )

                self.routes.append(route)

                if config.DEBUG:

                    print(f"🛣️ {route}")

        print(
            f"✅ {len(self.stops)} paradas y "
            f"{len(self.routes)} rutas cargadas."
        )