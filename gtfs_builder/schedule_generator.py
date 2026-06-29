from gtfs_builder.models import StopTime


class ScheduleGenerator:

    def generate(self, trips, stops):

        print("\n⏰ Generando horarios...\n")

        stop_times = []

        for trip in trips:

            hora = 8
            minuto = 0

            for secuencia, stop in enumerate(stops, start=1):

                tiempo = f"{hora:02}:{minuto:02}:00"

                stop_time = StopTime(
                    trip_id=trip.trip_id,
                    arrival_time=tiempo,
                    departure_time=tiempo,
                    stop_id=stop.stop_id,
                    stop_sequence=secuencia
                )

                stop_times.append(stop_time)

                print(
                    f"🚌 {trip.trip_id} -> "
                    f"{stop.name} ({tiempo})"
                )

                minuto += 2

                while minuto >= 60:
                    hora += 1
                    minuto -= 60

        print(f"\n✅ {len(stop_times)} horarios generados.")

        return stop_times