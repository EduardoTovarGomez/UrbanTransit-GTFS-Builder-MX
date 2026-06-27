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
            "route_name": self.name
        }