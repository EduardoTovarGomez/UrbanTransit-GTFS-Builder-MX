from gtfs_builder.models import Trip


class TripGenerator:

    def generate(self, routes):

        print("\n🚌 Generando viajes...\n")

        trips = []

        for route in routes:

            trip = Trip(
                trip_id=f"TRIP_{route.route_id}",
                route_id=route.route_id,
                shape_id=route.route_id,
                service_id="WEEKDAY"
            )

            trips.append(trip)

            print(
                f"✔ {trip.trip_id} "
                f"(Ruta {route.route_id}: {route.name})"
            )

        print(f"\n✅ {len(trips)} viajes generados.")

        return trips