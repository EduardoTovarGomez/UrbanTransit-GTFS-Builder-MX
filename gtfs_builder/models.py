class Stop:

    def __init__(self, stop_id, name, lat, lon):
        self.stop_id = stop_id
        self.name = name
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f"{self.stop_id} - {self.name}"

    def to_dict(self):
        return {
            "stop_id": self.stop_id,
            "stop_name": self.name,
            "stop_lat": self.lat,
            "stop_lon": self.lon
        }


class Route:

    def __init__(
        self,
        route_id,
        name,
        description,
        points
    ):

        self.route_id = route_id
        self.name = name
        self.description = description
        self.points = points

        # Paradas asociadas a esta ruta
        self.stops = []

    def __str__(self):

        return (
            f"{self.name}"
            f" ({self.description})"
            f" - {len(self.points)} puntos"
        )


class Trip:

    def __init__(
        self,
        trip_id,
        route_id,
        shape_id,
        service_id,
        departure_time
    ):

        self.trip_id = trip_id
        self.route_id = route_id
        self.shape_id = shape_id
        self.service_id = service_id
        self.departure_time = departure_time

    def __str__(self):

        return (
            f"{self.trip_id}"
            f" ({self.departure_time})"
        )

    def to_dict(self):

        return {

            "trip_id": self.trip_id,
            "route_id": self.route_id,
            "shape_id": self.shape_id,
            "service_id": self.service_id,
            "departure_time": self.departure_time

        }


class StopTime:

    def __init__(
        self,
        trip_id,
        arrival_time,
        departure_time,
        stop_id,
        stop_sequence,
        shape_dist_traveled
    ):

        self.trip_id = trip_id
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.stop_id = stop_id
        self.stop_sequence = stop_sequence
        self.shape_dist_traveled = shape_dist_traveled

    def __str__(self):

        return (
            f"{self.trip_id} | "
            f"Parada {self.stop_sequence} | "
            f"{self.arrival_time}"
        )

    def to_dict(self):

        return {
            "trip_id": self.trip_id,
            "arrival_time": self.arrival_time,
            "departure_time": self.departure_time,
            "stop_id": self.stop_id,
            "stop_sequence": self.stop_sequence,
            "shape_dist_traveled": round(
                self.shape_dist_traveled,
                2
            )
        }


class MatchedStop:

    def __init__(
        self,
        stop,
        shape_index,
        distance
    ):

        self.stop = stop
        self.shape_index = shape_index
        self.distance = distance

        self.segment = None
        self.side = None
        self.confidence = 1.0
        self.distance_from_start = 0.0
        self.travel_time = 0

    def __str__(self):

        side = self.side if self.side else "?"

        return (
            f"{self.stop.name} | "
            f"shape={self.shape_index} | "
            f"{self.distance:.1f} m | "
            f"side={side}"
        )


class MatchedSegment:

    def __init__(
        self,
        segment_index,
        start,
        end,
        distance
    ):

        self.segment_index = segment_index
        self.start = start
        self.end = end
        self.distance = distance

    def __str__(self):

        return (
            f"Segmento {self.segment_index} "
            f"({self.distance:.1f} m)"
        )