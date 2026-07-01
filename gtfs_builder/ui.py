"""
UrbanTransit GTFS Builder MX
---------------------------------
Archivo:
ui.py

Versión:
v0.6 - Sprint 5

Descripción:
Funciones para mostrar mensajes en consola.
"""

import time

from gtfs_builder import config


class ConsoleUI:

    def __init__(self):

        self.start_time = time.time()

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

    def finish(self, parser):

        elapsed = time.time() - self.start_time

        print("\n" + "=" * 60)
        print("🎉 GTFS generado correctamente")
        print("=" * 60)

        print(f"📍 Paradas : {len(parser.stops)}")
        print(f"🛣️ Rutas   : {len(parser.routes)}")

        print(f"\n⏱ Tiempo de ejecución: {elapsed:.2f} segundos")
        print("=" * 60)