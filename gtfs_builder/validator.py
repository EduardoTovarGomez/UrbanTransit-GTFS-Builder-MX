"""
UrbanTransit GTFS Builder MX
---------------------------------
Archivo:
validator.py

Versión:
v0.6 - Sprint 4

Descripción:
Realiza validaciones antes de generar el GTFS.
"""

from collections import Counter


class ProjectValidator:

    def __init__(self, parser):

        self.parser = parser

    def validate(self):

        print("\n" + "=" * 35)
        print("VALIDANDO PROYECTO")
        print("=" * 35)

        self.validate_routes()
        self.validate_stops()
        self.check_duplicate_stop_names()

        print("\n✅ Validación finalizada.")

    # =====================================

    def validate_routes(self):

        if len(self.parser.routes) == 0:

            print("❌ No se encontraron rutas.")

        else:

            print(f"✅ {len(self.parser.routes)} rutas detectadas.")

    # =====================================

    def validate_stops(self):

        if len(self.parser.stops) == 0:

            print("❌ No se encontraron paradas.")

        else:

            print(f"✅ {len(self.parser.stops)} paradas detectadas.")

    # =====================================

    def check_duplicate_stop_names(self):

        names = [stop.name for stop in self.parser.stops]

        duplicates = [
            name
            for name, count in Counter(names).items()
            if count > 1
        ]

        if duplicates:

            print("\n⚠ Paradas con nombres repetidos:")

            for name in duplicates:

                print(f"   • {name}")

        else:

            print("✅ No hay nombres repetidos.")