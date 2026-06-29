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

    def __init__(self, route_id, name, points):
        self.route_id = route_id
        self.name = name
        self.points = points

    def __str__(self):
        return f"{self.name} ({len(self.points)} puntos)"

    def to_dict(self):
        return {
            "route_id": self.route_id,
            "route_name": self.name,
            "points": self.points
        }


class Trip:

    def __init__(self, trip_id, route_id, shape_id, service_id="WEEKDAY"):

        self.trip_id = trip_id
        self.route_id = route_id
        self.shape_id = shape_id
        self.service_id = service_id

    def __str__(self):
        return f"Trip {self.trip_id}"

    def to_dict(self):
        return {
            "trip_id": self.trip_id,
            "route_id": self.route_id,
            "service_id": self.service_id,
            "shape_id": self.shape_id
        }