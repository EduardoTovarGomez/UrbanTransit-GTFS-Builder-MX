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

    def __str__(self):

        return (
            f"{self.name}"
            f" ({self.description})"
            f" - {len(self.points)} puntos"
        )


class Trip:

    def __init__(self, trip_id, route_id, shape_id, service_id):

        self.trip_id = trip_id
        self.route_id = route_id
        self.shape_id = shape_id
        self.service_id = service_id

    def __str__(self):

        return self.trip_id


class StopTime:

    def __init__(
        self,
        trip_id,
        arrival_time,
        departure_time,
        stop_id,
        stop_sequence
    ):

        self.trip_id = trip_id
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.stop_id = stop_id
        self.stop_sequence = stop_sequence

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
            "stop_sequence": self.stop_sequence
        }