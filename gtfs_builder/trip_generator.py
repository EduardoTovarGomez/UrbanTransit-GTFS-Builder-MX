"""
UrbanTransit GTFS Builder MX
---------------------------------
Archivo:
trip_generator.py

Descripción:
Genera automáticamente todos los viajes (trips)
del feed GTFS a partir del intervalo de servicio.
"""

from datetime import datetime, timedelta

from gtfs_builder import config
from gtfs_builder.models import Trip


class TripGenerator:

    def generate(self, routes):

        print("\n🚌 Generando viajes...")

        trips = []

        trip_counter = 1

        first_trip = datetime.strptime(
            config.FIRST_TRIP,
            "%H:%M:%S"
        )

        last_trip = datetime.strptime(
            config.LAST_TRIP,
            "%H:%M:%S"
        )

        headway = timedelta(
            minutes=config.HEADWAY_MINUTES
        )

        for route in routes:

            departure = first_trip

            while departure <= last_trip:

                trip = Trip(

                    trip_id=f"TRIP_{trip_counter:05d}",

                    route_id=route.route_id,

                    shape_id=route.route_id,

                    service_id=config.SERVICE_ID,

                    departure_time=departure.strftime(
                        "%H:%M:%S"
                    )

                )

                trips.append(trip)

                if config.DEBUG:

                    print(
                        f"   ✔ {trip.trip_id}"
                        f" | {route.name}"
                        f" | {trip.departure_time}"
                    )

                trip_counter += 1

                departure += headway

        print(f"✅ {len(trips)} viajes generados.")

        return trips