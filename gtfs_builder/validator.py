"""
UrbanTransit GTFS Builder MX
---------------------------------
Archivo:
validator.py

Descripción:
Validaciones previas a la generación del GTFS.
"""

from collections import Counter

from gtfs_builder import config


class ProjectValidator:

    def __init__(self, parser):

        self.parser = parser

    # =====================================================
    # VALIDATION
    # =====================================================

    def validate(self):

        print("\n🔎 Validando proyecto...")

        self.validate_routes()
        self.validate_stops()
        self.check_duplicate_stop_names()

        print("✅ Validación completada.")

    # =====================================================
    # ROUTES
    # =====================================================

    def validate_routes(self):

        total = len(self.parser.routes)

        if total == 0:

            print("❌ No se encontraron rutas.")

        elif config.DEBUG:

            print(f"✅ {total} rutas detectadas.")

    # =====================================================
    # STOPS
    # =====================================================

    def validate_stops(self):

        total = len(self.parser.stops)

        if total == 0:

            print("❌ No se encontraron paradas.")

        elif config.DEBUG:

            print(f"✅ {total} paradas detectadas.")

    # =====================================================
    # DUPLICATE STOP NAMES
    # =====================================================

    def check_duplicate_stop_names(self):

        names = [

            stop.name

            for stop in self.parser.stops

        ]

        duplicates = [

            name

            for name, count in Counter(names).items()

            if count > 1

        ]

        if not duplicates:

            if config.DEBUG:

                print("✅ No hay nombres repetidos.")

            return

        print("\n⚠ Paradas con nombres repetidos:")

        for name in duplicates:

            print(f"   • {name}")