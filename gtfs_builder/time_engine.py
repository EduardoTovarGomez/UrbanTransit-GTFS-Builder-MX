from datetime import timedelta
import math

from gtfs_builder import config
from gtfs_builder.geometry import distance_along_segment


class TimeEngine:

    def __init__(self):
        pass

    # =====================================================
    # DISTANCE
    # =====================================================

    def distance_between_points(self, point_a, point_b):

        R = 6371000

        lon1, lat1 = point_a
        lon2, lat2 = point_b

        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)

        lat2 = math.radians(lat2)
        lon2 = math.radians(lon2)

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
    # SHAPE DISTANCES
    # =====================================================

    def build_shape_distances(self, route):

        cumulative = [0.0]
        total = 0.0

        for i in range(len(route.points) - 1):

            lon1, lat1 = map(
                float,
                route.points[i].split(",")[:2]
            )

            lon2, lat2 = map(
                float,
                route.points[i + 1].split(",")[:2]
            )

            distance = self.distance_between_points(
                (lon1, lat1),
                (lon2, lat2)
            )

            total += distance
            cumulative.append(total)

        route.shape_distances = cumulative

        if config.DEBUG:

            print(f"\n📏 {route.name}")
            print(
                f"   Longitud total: {total:.1f} m"
            )

        return cumulative

    # =====================================================
    # STOP DISTANCES
    # =====================================================

    def assign_stop_distances(self, route):

        if config.DEBUG:

            print(
                f"\n📍 Distancias ({route.name})"
            )

        for matched_stop in route.stops:

            segment = matched_stop.segment

            extra_distance = distance_along_segment(

                (
                    matched_stop.stop.lon,
                    matched_stop.stop.lat
                ),

                segment.start,
                segment.end

            )

            matched_stop.distance_from_start = (

                route.shape_distances[
                    segment.segment_index
                ]

                +

                extra_distance

            )

            if config.DEBUG:

                print(

                    f"   "
                    f"{matched_stop.stop.name:<35}"
                    f"{matched_stop.distance_from_start:8.1f} m"

                )

    # =====================================================
    # TRAVEL TIMES
    # =====================================================

    def calculate_travel_times(self, route):

        speed = (
            config.SPEED_PROFILE["urban"]
            / 3.6
        )

        if config.DEBUG:

            print(
                f"\n🕒 Tiempos ({route.name})"
            )

        for matched_stop in route.stops:

            seconds = (
                matched_stop.distance_from_start
                / speed
            )

            matched_stop.travel_time = int(seconds)

            if config.DEBUG:

                print(
                    f"   "
                    f"{matched_stop.stop.name:<35}"
                    f"{matched_stop.travel_time:>6} s"
                )