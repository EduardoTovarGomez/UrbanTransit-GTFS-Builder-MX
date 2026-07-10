import math

from gtfs_builder import config


class RouteMatcher:

    def __init__(self, routes, stops):

        self.routes = routes
        self.stops = stops


    def parse_shape_points(self, route):

        coordinates = []

        for point in route.points:

            values = point.split(",")

            lon = float(values[0])
            lat = float(values[1])

            coordinates.append((lon, lat))

        return coordinates



    def calculate_distance(self, stop, point):

        # Radio medio de la Tierra (metros)
        R = 6371000

        lat1 = math.radians(stop.lat)
        lon1 = math.radians(stop.lon)

        lat2 = math.radians(point[1])
        lon2 = math.radians(point[0])

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = (
            math.sin(dlat / 2) ** 2
            + math.cos(lat1)
            * math.cos(lat2)
            * math.sin(dlon / 2) ** 2
        )

        c = 2 * math.atan2(
            math.sqrt(a),
            math.sqrt(1 - a)
        )

        return R * c



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

            route.stops.clear()

            print(f"\n🛣️ {route.name}")
            print(f"   Shape: {len(shape)} puntos")

            for stop in self.stops:

                closest_index, distance = self.find_closest_shape_point(
                    stop,
                    shape
                )


                accepted = distance <= config.MATCH_DISTANCE
                
                route.stops.append({
                    "stop": stop,
                    "shape_index": closest_index,
                    "distance": distance,
                    "accepted": accepted
                })



            route.stops.sort(
                key=lambda item: item["shape_index"]
            )

            print("\n   Orden detectado:\n")

            for item in route.stops:

                stop = item["stop"]

                status = "✓" if item["accepted"] else "✗"
                
                print(
                    f"{status} "
                    f"{item['shape_index']:>3} "
                    f"{item['distance']:8.1f} m "
                    f"{stop.name}"
                )

        print("\n✅ Asociación finalizada.")