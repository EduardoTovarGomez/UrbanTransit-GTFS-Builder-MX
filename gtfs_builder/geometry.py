import math


EARTH_RADIUS = 6371000


def haversine_distance(point1, point2):

    lon1, lat1 = point1
    lon2, lat2 = point2

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

    return EARTH_RADIUS * c


def stop_distance(stop, point):

    return haversine_distance(
        (stop.lon, stop.lat),
        point
    )


def vector(a, b):

    return (
        b[0] - a[0],
        b[1] - a[1]
    )


def cross(v1, v2):

    return (
        v1[0] * v2[1]
        - v1[1] * v2[0]
    )