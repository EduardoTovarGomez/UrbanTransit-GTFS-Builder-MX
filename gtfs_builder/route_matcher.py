import math

from gtfs_builder import config
from gtfs_builder.geometry import point_side
from gtfs_builder.models import (
    MatchedSegment,
    MatchedStop
)


class RouteMatcher:

    def __init__(self, routes, stops):

        self.routes = routes
        self.stops = stops

    # =====================================================
    # GEOMETRY
    # =====================================================

    def parse_shape_points(self, route):

        coordinates = []

        for point in route.points:

            lon, lat = map(
                float,
                point.split(",")[:2]
            )

            coordinates.append((lon, lat))

        return coordinates

    def calculate_distance(self, stop, point):

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

    # =====================================================
    # MATCHING
    # =====================================================

    def find_closest_shape_point(self, stop, shape):

        closest_index = None
        shortest_distance = float("inf")

        for index, point in enumerate(shape):

            distance = self.calculate_distance(
                stop,
                point
            )

            if distance < shortest_distance:

                shortest_distance = distance
                closest_index = index

        return closest_index, shortest_distance

    def find_closest_segment(self, stop, shape):

        best_segment = None
        shortest_distance = float("inf")

        for i in range(len(shape) - 1):

            start = shape[i]
            end = shape[i + 1]

            distance = min(
                self.calculate_distance(stop, start),
                self.calculate_distance(stop, end)
            )

            if distance < shortest_distance:

                shortest_distance = distance

                best_segment = MatchedSegment(
                    segment_index=i,
                    start=start,
                    end=end,
                    distance=distance
                )

        return best_segment

    # =====================================================
    # CLASSIFICATION
    # =====================================================

    def classify_side(self, stop, segment):

        return point_side(
            stop.lon,
            stop.lat,
            segment.start[0],
            segment.start[1],
            segment.end[0],
            segment.end[1]
        )

    def keep_correct_side(self, route):

        accepted = []
        rejected = []

        for matched_stop in route.stops:

            if matched_stop.side == config.STOP_SIDE:

                accepted.append(matched_stop)

            else:

                rejected.append(matched_stop)

        route.stops = accepted

        return len(accepted), len(rejected)

    # =====================================================
    # MAIN
    # =====================================================

    def match(self):

        print("\n===================================")
        print("ROUTE MATCHER")
        print("===================================")

        for route in self.routes:

            shape = self.parse_shape_points(route)

            route.stops.clear()

            for stop in self.stops:

                segment = self.find_closest_segment(
                    stop,
                    shape
                )

                matched_stop = MatchedStop(
                    stop=stop,
                    shape_index=segment.segment_index,
                    distance=segment.distance
                )

                matched_stop.segment = segment

                matched_stop.side = self.classify_side(
                    stop,
                    segment
                )

                route.stops.append(
                    matched_stop
                )

            route.stops.sort(
                key=lambda item: item.segment.segment_index
            )

            accepted, rejected = self.keep_correct_side(
                route
            )

            print(f"\n🛣️ {route.name}")
            print(
                f"   ✓ Shape: {len(shape)} puntos"
            )
            print(
                f"   ✓ Paradas aceptadas : {accepted}"
            )
            print(
                f"   ✓ Paradas descartadas : {rejected}"
            )

            if config.DEBUG:

                print("\n   Orden detectado:\n")

                for item in route.stops:

                    print(
                        f"✓ "
                        f"{item.segment.segment_index:>3} "
                        f"{item.distance:8.1f} m "
                        f"{item.side:>6} "
                        f"{item.stop.name}"
                    )

        print("\n✅ Asociación finalizada.")