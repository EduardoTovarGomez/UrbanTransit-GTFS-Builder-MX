"""
UrbanTransit GTFS Builder MX
---------------------------------
Archivo:
exporter.py

Versión:
v0.6 - Sprint 3

Descripción:
Genera los archivos GTFS del proyecto.
"""

import csv
import zipfile
from pathlib import Path

from gtfs_builder import config


class GTFSExporter:

    def __init__(self):

        self.output_folder = Path(config.OUTPUT_FOLDER)
        self.output_folder.mkdir(exist_ok=True)
        
        self.archive_folder = Path("archives")
        self.archive_folder.mkdir(exist_ok=True)
        
    # =====================================================
    # STOPS
    # =====================================================

    def export_stops(self, stops):

        print("\n📄 Generando stops.txt...")

        file = self.output_folder / "stops.txt"

        with open(file, "w", newline="", encoding="utf-8") as f:

            writer = csv.writer(f)

            writer.writerow([
                "stop_id",
                "stop_name",
                "stop_lat",
                "stop_lon"
            ])

            for stop in stops:
                writer.writerow(stop.to_dict().values())

        print("✅ stops.txt generado.")

    # =====================================================
    # ROUTES
    # =====================================================

    def export_routes(self, routes):

        print("\n📄 Generando routes.txt...")

        file = self.output_folder / "routes.txt"

        with open(file, "w", newline="", encoding="utf-8") as f:

            writer = csv.writer(f)

            writer.writerow([
                "route_id",
                "route_short_name",
                "route_long_name",
                "route_type"
            ])

            for i, route in enumerate(routes, start=1):

                writer.writerow([
                    i,
                    route.name,
                    route.description,
                    3
                ])

        print("✅ routes.txt generado.")

    # =====================================================
    # SHAPES
    # =====================================================

    def export_shapes(self, routes):

        print("\n📄 Generando shapes.txt...")

        file = self.output_folder / "shapes.txt"

        with open(file, "w", newline="", encoding="utf-8") as f:

            writer = csv.writer(f)

            writer.writerow([
                "shape_id",
                "shape_pt_lat",
                "shape_pt_lon",
                "shape_pt_sequence"
            ])

            for shape_id, route in enumerate(routes, start=1):

                for sequence, point in enumerate(route.points, start=1):

                    lon, lat, *_ = point.split(",")

                    writer.writerow([
                        shape_id,
                        float(lat),
                        float(lon),
                        sequence
                    ])

        print("✅ shapes.txt generado.")

    # =====================================================
    # TRIPS
    # =====================================================

    def export_trips(self, trips):

        print("\n📄 Generando trips.txt...")

        file = self.output_folder / "trips.txt"

        with open(file, "w", newline="", encoding="utf-8") as f:

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

        print("✅ trips.txt generado.")

    # =====================================================
    # STOP TIMES
    # =====================================================

    def export_stop_times(self, stop_times):

        print("\n📄 Generando stop_times.txt...")

        file = self.output_folder / "stop_times.txt"

        with open(file, "w", newline="", encoding="utf-8") as f:

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

        print("✅ stop_times.txt generado.")

    # =====================================================
    # AGENCY
    # =====================================================

    def export_agency(self):

        print("\n📄 Generando agency.txt...")

        file = self.output_folder / "agency.txt"

        with open(file, "w", newline="", encoding="utf-8") as f:

            writer = csv.writer(f)

            writer.writerow([
                "agency_id",
                "agency_name",
                "agency_url",
                "agency_timezone",
                "agency_lang"
            ])

            writer.writerow([
                config.AGENCY_ID,
                config.AGENCY_NAME,
                config.AGENCY_URL,
                config.TIMEZONE,
                config.LANGUAGE
            ])

        print("✅ agency.txt generado.")

    # =====================================================
    # CALENDAR
    # =====================================================

    def export_calendar(self):

        print("\n📄 Generando calendar.txt...")

        file = self.output_folder / "calendar.txt"

        with open(file, "w", newline="", encoding="utf-8") as f:

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
                config.SERVICE_ID,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                config.START_DATE,
                config.END_DATE
            ])

        print("✅ calendar.txt generado.")

    # =====================================================
    # FEED INFO
    # =====================================================

    def export_feed_info(self):

        print("\n📄 Generando feed_info.txt...")

        file = self.output_folder / "feed_info.txt"

        with open(file, "w", newline="", encoding="utf-8") as f:

            writer = csv.writer(f)

            writer.writerow([
                "feed_publisher_name",
                "feed_publisher_url",
                "feed_lang",
                "feed_start_date",
                "feed_end_date",
                "feed_version",
                "feed_contact_email",
                "feed_contact_url"
            ])

            writer.writerow([
                config.AGENCY_NAME,
                config.AGENCY_URL,
                config.LANGUAGE,
                config.START_DATE,
                config.END_DATE,
                config.FEED_VERSION,
                config.CONTACT_EMAIL,
                config.CONTACT_URL
            ])

        print("✅ feed_info.txt generado.")
        
    def export_zip(self):

        print("\n📦 Generando archivo ZIP...")

        zip_name = self.archive_folder / f"GTFS_{config.FEED_VERSION}.zip"

        with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:

            for file in self.output_folder.glob("*.txt"):
                zipf.write(file, arcname=file.name)

        print(f"✅ ZIP generado: {zip_name}")