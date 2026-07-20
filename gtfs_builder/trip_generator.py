"""
UrbanTransit GTFS Builder MX
---------------------------------
Archivo:
trip_generator.py

Descripción:
Genera los viajes (trips) del feed GTFS.
"""

from gtfs_builder import config
from gtfs_builder.models import Trip


class TripGenerator:

    def generate(self, routes):

        print("\n🚌 Generando viajes...")

        trips = []

        for route in routes:

            trip = Trip(
                trip_id=f"TRIP_{route.route_id}",
                route_id=route.route_id,
                shape_id=route.route_id,
                service_id="WEEKDAY"
            )

            trips.append(trip)

            if config.DEBUG:

                print(
                    f"   ✔ {trip.trip_id}"
                    f" ({route.name})"
                )

        print(f"✅ {len(trips)} viajes generados.")

        return trips