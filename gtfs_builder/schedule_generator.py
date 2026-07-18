from datetime import datetime, timedelta

from gtfs_builder import config
from gtfs_builder.models import StopTime


class ScheduleGenerator:

    def generate(self, trips, routes):

        print("\n===================================")
        print("SCHEDULE GENERATOR")
        print("===================================")

        stop_times = []

        start_time = datetime.strptime(
            "08:00:00",
            "%H:%M:%S"
        )

        for trip in trips:

            route = next(

                route

                for route in routes

                if route.route_id == trip.route_id

            )

            for sequence, matched_stop in enumerate(

                route.stops,

                start=1

            ):

                current_time = (

                    start_time

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

                        stop_sequence=sequence

                    )

                )

                if config.DEBUG:

                    print(

                        f"🚌 "

                        f"{trip.trip_id:<8}"

                        f"{time_string}  "

                        f"{matched_stop.stop.name}"

                    )

        print(
            f"\n✅ {len(stop_times)} horarios generados."
        )

        return stop_times