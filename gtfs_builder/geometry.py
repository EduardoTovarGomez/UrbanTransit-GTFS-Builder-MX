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
    
def point_side(px, py, x1, y1, x2, y2):

    value = (
        (x2 - x1) * (py - y1)
        - (y2 - y1) * (px - x1)
    )

    if value > 0:
        return "LEFT"

    elif value < 0:
        return "RIGHT"

    return "CENTER"

def project_point_on_segment(point, start, end):

    px, py = point
    ax, ay = start
    bx, by = end

    abx = bx - ax
    aby = by - ay

    apx = px - ax
    apy = py - ay

    ab_squared = abx * abx + aby * aby

    if ab_squared == 0:

        return start, 0.0

    t = (
        apx * abx +
        apy * aby
    ) / ab_squared

    t = max(0.0, min(1.0, t))

    projection = (
        ax + t * abx,
        ay + t * aby
    )

    return projection, t

def distance_along_segment(point, start, end):

    projection, _ = project_point_on_segment(
        point,
        start,
        end
    )

    return haversine_distance(
        start,
        projection
    )