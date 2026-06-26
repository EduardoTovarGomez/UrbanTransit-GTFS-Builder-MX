class Stop:
    def __init__(self, stop_id, name, lat, lon):
        self.stop_id = stop_id
        self.name = name
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f"{self.stop_id} - {self.name}"