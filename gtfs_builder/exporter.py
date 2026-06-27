import csv
from pathlib import Path


class GTFSExporter:

    def __init__(self, output_folder="output"):

        self.output_folder = Path(output_folder)
        self.output_folder.mkdir(exist_ok=True)

    # ==========================================
    # STOPS.TXT
    # ==========================================

    def export_stops(self, stops):

        print("\n📄 Generando stops.txt...")

        archivo = self.output_folder / "stops.txt"

        with open(
            archivo,
            "w",
            newline="",
            encoding="utf-8"
        ) as f:

            writer = csv.writer(f)

            writer.writerow([
                "stop_id",
                "stop_name",
                "stop_lat",
                "stop_lon"
            ])

            for stop in stops:

                writer.writerow([
                    stop.stop_id,
                    stop.name,
                    stop.lat,
                    stop.lon
                ])

        print("✅ stops.txt generado correctamente.")

    # ==========================================
    # ROUTES.TXT
    # ==========================================

    def export_routes(self, routes):

        print("\n📄 Generando routes.txt...")

        archivo = self.output_folder / "routes.txt"

        with open(
            archivo,
            "w",
            newline="",
            encoding="utf-8"
        ) as f:

            writer = csv.writer(f)

            writer.writerow([
                "route_id",
                "route_short_name",
                "route_long_name",
                "route_type"
            ])

            for route in routes:

                writer.writerow([
                    route.route_id,
                    route.name,
                    route.name,
                    3
                ])

        print("✅ routes.txt generado correctamente.")

    # ==========================================
    # SHAPES.TXT
    # ==========================================

    def export_shapes(self, routes):

        print("\n📄 Generando shapes.txt...")

        archivo = self.output_folder / "shapes.txt"

        with open(
            archivo,
            "w",
            newline="",
            encoding="utf-8"
        ) as f:

            writer = csv.writer(f)

            writer.writerow([
                "shape_id",
                "shape_pt_lat",
                "shape_pt_lon",
                "shape_pt_sequence"
            ])

            total_points = 0

            for route in routes:

                sequence = 1

                for point in route.points:

                    lon, lat, *_ = point.split(",")

                    writer.writerow([
                        route.route_id,
                        lat,
                        lon,
                        sequence
                    ])

                    sequence += 1
                    total_points += 1

                print(f"   ✔ {route.name}: {sequence - 1} puntos")

        print(f"\n✅ shapes.txt generado correctamente ({total_points} puntos).")