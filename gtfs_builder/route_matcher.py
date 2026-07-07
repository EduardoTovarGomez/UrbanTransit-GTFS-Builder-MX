import math


class RouteMatcher:

    def __init__(self, routes, stops):

        self.routes = routes
        self.stops = stops

        # Aquí guardaremos las asociaciones
        self.matches = {}

    def parse_shape_points(self, route):

        coordinates = []

        for point in route.points:

            values = point.split(",")

            lon = float(values[0])
            lat = float(values[1])

            coordinates.append((lon, lat))

        return coordinates

    def calculate_distance(self, stop, point):

        lon1 = stop.lon
        lat1 = stop.lat

        lon2 = point[0]
        lat2 = point[1]

        return math.sqrt(
            (lon2 - lon1) ** 2 +
            (lat2 - lat1) ** 2
        )

    def find_closest_shape_point(self, stop, shape):

        closest_index = None
        shortest_distance = float("inf")

        for index, point in enumerate(shape):

            distance = self.calculate_distance(stop, point)

            if distance < shortest_distance:

                shortest_distance = distance
                closest_index = index

        return closest_index, shortest_distance

    def match(self):

        print("\n===================================")
        print("ASOCIANDO PARADAS A RUTAS")
        print("===================================")

        for route in self.routes:

            shape = self.parse_shape_points(route)

            matched_stops = []

            print(f"\n🛣️ {route.name}")
            print(f"   Shape: {len(shape)} puntos")

            for stop in self.stops:

                closest_index, distance = self.find_closest_shape_point(
                    stop,
                    shape
                )

                matched_stops.append({
                    "stop": stop,
                    "shape_index": closest_index,
                    "distance": distance
                })

            matched_stops.sort(
                key=lambda item: item["shape_index"]
            )

            self.matches[route.route_id] = matched_stops

            print("\n   Orden detectado:\n")

            for item in matched_stops:

                stop = item["stop"]

                print(
                    f"   {item['shape_index']:>3}  "
                    f"{stop.name}"
                )

        print("\n✅ Asociación finalizada.")