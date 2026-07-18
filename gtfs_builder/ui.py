"""
UrbanTransit GTFS Builder MX
---------------------------------
Archivo:
ui.py

Descripción:
Interfaz de consola del proyecto.
"""

import time

from gtfs_builder import config


class ConsoleUI:

    def __init__(self):

        self.start_time = time.time()

    # =====================================================
    # BANNER
    # =====================================================

    def banner(self):

        print()
        print("=" * 68)

        print(f"🚍 {config.PROJECT_NAME}")
        print(config.PROJECT_EDITION)
        print(f"Versión {config.FEED_VERSION}")

        print()

        print(config.PROJECT_TAGLINE)

        print()

        print(f"Open-source project by {config.AUTHOR}")
        print(config.PROJECT_URL)

        print("=" * 68)

    # =====================================================
    # SECTION
    # =====================================================

    def section(self, title):

        print()

        print("=" * 35)
        print(title.upper())
        print("=" * 35)

    # =====================================================
    # SUMMARY
    # =====================================================

    def summary(self, parser):

        self.section("Resumen del proyecto")

        print(
            f"📍 Paradas : {len(parser.stops)}"
        )

        print(
            f"🛣️ Rutas   : {len(parser.routes)}"
        )

    # =====================================================
    # FINISH
    # =====================================================

    def finish(self, parser):

        elapsed = (
            time.time()
            - self.start_time
        )

        print()
        print("=" * 60)

        print("🎉 GTFS generado correctamente")

        print("=" * 60)

        print(
            f"📍 Paradas : {len(parser.stops)}"
        )

        print(
            f"🛣️ Rutas   : {len(parser.routes)}"
        )

        print()

        print(
            f"⏱ Tiempo de ejecución: "
            f"{elapsed:.2f} segundos"
        )

        print("=" * 60)