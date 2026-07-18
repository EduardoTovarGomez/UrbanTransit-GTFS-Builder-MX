"""
UrbanTransit GTFS Builder MX
---------------------------------
Archivo:
exporter.py

Descripción:
Genera y exporta los archivos GTFS del proyecto.
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
    # UTILITIES
    # =====================================================

    def write_csv(self, filename, headers, rows):

        file = self.output_folder / filename

        with open(
            file,
            "w",
            newline="",
            encoding="utf-8"
        ) as f:

            writer = csv.writer(f)

            writer.writerow(headers)

            writer.writerows(rows)

        return file

    # =====================================================
    # STOPS
    # =====================================================

    def export_stops(self, stops):

        rows = [

            stop.to_dict().values()

            for stop in stops

        ]

        self.write_csv(

            "stops.txt",

            [
                "stop_id",
                "stop_name",
                "stop_lat",
                "stop_lon"
            ],

            rows

        )

    # =====================================================
    # ROUTES
    # =====================================================

    def export_routes(self, routes):

        rows = []

        for i, route in enumerate(routes, start=1):

            rows.append([

                i,

                config.AGENCY_ID,

                route.name,

                route.description,

                3

            ])

        self.write_csv(

            "routes.txt",

            [
                "route_id",
                "agency_id",
                "route_short_name",
                "route_long_name",
                "route_type"
            ],

            rows

        )

    # =====================================================
    # SHAPES
    # =====================================================

    def export_shapes(self, routes):

        rows = []

        for shape_id, route in enumerate(routes, start=1):

            for sequence, point in enumerate(
                route.points,
                start=1
            ):

                lon, lat, *_ = point.split(",")

                rows.append([

                    shape_id,

                    float(lat),

                    float(lon),

                    sequence

                ])

        self.write_csv(

            "shapes.txt",

            [
                "shape_id",
                "shape_pt_lat",
                "shape_pt_lon",
                "shape_pt_sequence"
            ],

            rows

        )

    # =====================================================
    # TRIPS
    # =====================================================

    def export_trips(self, trips):

        rows = [

            [

                trip.route_id,

                trip.service_id,

                trip.trip_id,

                trip.shape_id

            ]

            for trip in trips

        ]

        self.write_csv(

            "trips.txt",

            [
                "route_id",
                "service_id",
                "trip_id",
                "shape_id"
            ],

            rows

        )

    # =====================================================
    # STOP TIMES
    # =====================================================

    def export_stop_times(self, stop_times):

        rows = [

            [

                stop_time.trip_id,

                stop_time.arrival_time,

                stop_time.departure_time,

                stop_time.stop_id,

                stop_time.stop_sequence

            ]

            for stop_time in stop_times

        ]

        self.write_csv(

            "stop_times.txt",

            [
                "trip_id",
                "arrival_time",
                "departure_time",
                "stop_id",
                "stop_sequence"
            ],

            rows

        )

    # =====================================================
    # AGENCY
    # =====================================================

    def export_agency(self):

        self.write_csv(

            "agency.txt",

            [

                "agency_id",

                "agency_name",

                "agency_url",

                "agency_timezone",

                "agency_lang"

            ],

            [[

                config.AGENCY_ID,

                config.AGENCY_NAME,

                config.AGENCY_URL,

                config.TIMEZONE,

                config.LANGUAGE

            ]]

        )

    # =====================================================
    # CALENDAR
    # =====================================================

    def export_calendar(self):

        self.write_csv(

            "calendar.txt",

            [

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

            ],

            [[

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

            ]]

        )

    # =====================================================
    # FEED INFO
    # =====================================================

    def export_feed_info(self):

        self.write_csv(

            "feed_info.txt",

            [

                "feed_publisher_name",

                "feed_publisher_url",

                "feed_lang",

                "feed_start_date",

                "feed_end_date",

                "feed_version",

                "feed_contact_email",

                "feed_contact_url"

            ],

            [[

                config.AGENCY_NAME,

                config.AGENCY_URL,

                config.LANGUAGE,

                config.START_DATE,

                config.END_DATE,

                config.FEED_VERSION,

                config.CONTACT_EMAIL,

                config.CONTACT_URL

            ]]

        )

    # =====================================================
    # ZIP
    # =====================================================

    def export_zip(self):

        zip_name = (

            self.archive_folder

            / f"GTFS_{config.FEED_VERSION}.zip"

        )

        with zipfile.ZipFile(

            zip_name,

            "w",

            zipfile.ZIP_DEFLATED

        ) as zipf:

            for file in self.output_folder.glob("*.txt"):

                zipf.write(

                    file,

                    arcname=file.name

                )

        print("\n===================================")
        print("EXPORTER")
        print("===================================")

        print(
            f"✅ 8 archivos GTFS exportados"
        )

        print(
            f"📦 ZIP generado: {zip_name}"
        )