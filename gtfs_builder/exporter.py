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
        
    # ==========================================
    # TRIPS.TXT
    # ==========================================

    def export_trips(self, trips):

        print("\n📄 Generando trips.txt...")

        archivo = self.output_folder / "trips.txt"

        with open(
            archivo,
            "w",
            newline="",
            encoding="utf-8"
        ) as f:

            writer = csv.writer(f)

            writer.writerow([
                "route_id",
                "service_id",
                "trip_id",
                "shape_id"
            ])

            for trip in trips:

                writer.writerow([
                    trip.route_id,
                    trip.service_id,
                    trip.trip_id,
                    trip.shape_id
                ])

        print("✅ trips.txt generado correctamente.")
        
    # ==========================================
    # STOP_TIMES.TXT
    # ==========================================

    def export_stop_times(self, stop_times):

        print("\n📄 Generando stop_times.txt...")

        archivo = self.output_folder / "stop_times.txt"

        with open(
            archivo,
            "w",
            newline="",
            encoding="utf-8"
        ) as f:

            writer = csv.writer(f)

            writer.writerow([
                "trip_id",
                "arrival_time",
                "departure_time",
                "stop_id",
                "stop_sequence"
            ])

            for stop_time in stop_times:

                writer.writerow([
                    stop_time.trip_id,
                    stop_time.arrival_time,
                    stop_time.departure_time,
                    stop_time.stop_id,
                    stop_time.stop_sequence
                ])

        print(
            f"✅ stop_times.txt generado correctamente "
            f"({len(stop_times)} registros)."
        )
        
    # ==========================================
    # AGENCY.TXT
    # ==========================================

    def export_agency(self):

        print("\n📄 Generando agency.txt...")

        archivo = self.output_folder / "agency.txt"

        with open(
            archivo,
            "w",
            newline="",
            encoding="utf-8"
        ) as f:

            writer = csv.writer(f)

            writer.writerow([
                "agency_id",
                "agency_name",
                "agency_url",
                "agency_timezone",
                "agency_lang"
            ])

            writer.writerow([
                1,
                "UrbanTransit MX",
                "https://github.com/EduardoTovarGomez/urbantransit-gtfs-builder-mx",
                "America/Mexico_City",
                "es"
            ])

        print("✅ agency.txt generado correctamente.")
        
    # ==========================================
    # CALENDAR.TXT
    # ==========================================

    def export_calendar(self):

        print("\n📄 Generando calendar.txt...")

        archivo = self.output_folder / "calendar.txt"

        with open(
            archivo,
            "w",
            newline="",
            encoding="utf-8"
        ) as f:

            writer = csv.writer(f)

            writer.writerow([
                "service_id",
                "monday",
                "tuesday",
                "wednesday",
                "thursday",
                "friday",
                "saturday",
                "sunday",
                "start_date",
                "end_date"
            ])

            writer.writerow([
                "WEEKDAY",
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                "20260101",
                "20261231"
            ])

        print("✅ calendar.txt generado correctamente.")
        
    # ==========================================
    # FEED_INFO.TXT
    # ==========================================

    def export_feed_info(self):

        print("\n📄 Generando feed_info.txt...")

        archivo = self.output_folder / "feed_info.txt"

        with open(
            archivo,
            "w",
            newline="",
            encoding="utf-8"
        ) as f:

            writer = csv.writer(f)

            writer.writerow([
                "feed_publisher_name",
                "feed_publisher_url",
                "feed_lang",
                "feed_start_date",
                "feed_end_date",
                "feed_version"
            ])

            writer.writerow([
                "UrbanTransit MX",
                "https://github.com/EduardoTovarGomez/urbantransit-gtfs-builder-mx",
                "es",
                "20260101",
                "20261231",
                "v0.5.0"
            ])

        print("✅ feed_info.txt generado correctamente.")