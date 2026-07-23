"""
UrbanTransit GTFS Builder MX
---------------------------------
Archivo:
schedule_generator.py

Descripción:
Genera stop_times.txt a partir de los viajes y las
distancias/tiempos calculados por TimeEngine.
"""

from datetime import datetime, timedelta

from gtfs_builder import config
from gtfs_builder.models import StopTime


class ScheduleGenerator:

    def generate(self, trips, routes):

        print("\n===================================")
        print("GENERANDO HORARIOS")
        print("===================================")

        stop_times = []

        for trip in trips:

            route = next(
                route
                for route in routes
                if route.route_id == trip.route_id
            )

            # Hora de salida propia de este viaje
            trip_start = datetime.strptime(
                trip.departure_time,
                "%H:%M:%S"
            )

            for sequence, matched_stop in enumerate(
                route.stops,
                start=1
            ):

                current_time = (
                    trip_start
                    +
                    timedelta(
                        seconds=matched_stop.travel_time
                    )
                )

                time_string = current_time.strftime(
                    "%H:%M:%S"
                )

                stop_times.append(

                    StopTime(

                        trip_id=trip.trip_id,

                        arrival_time=time_string,

                        departure_time=time_string,

                        stop_id=matched_stop.stop.stop_id,

                        stop_sequence=sequence,

                        shape_dist_traveled=round(
                            matched_stop.distance_from_start,
                            2
                        )

                    )

                )

                if config.DEBUG:

                    print(
                        f"   {trip.trip_id:<10}"
                        f"{time_string:<10}"
                        f"{matched_stop.stop.name}"
                    )

        print(
            f"✅ {len(stop_times)} horarios generados."
        )

        return stop_times