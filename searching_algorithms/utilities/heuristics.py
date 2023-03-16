from math import radians, cos, sin, asin, sqrt

def distance_by_coordinates_heuristic(start_node, end_node):
    longitude1 = radians(start_node.longitude)
    latitude1 = radians(start_node.latitude)

    longitude2 = radians(end_node.longitude)
    latitude2 = radians(end_node.latitude)

    # Haversine formula
    dlon = longitude2 - longitude1
    dlat = latitude2 - latitude1
    a = sin(dlat / 2) ** 2 + cos(latitude1) * cos(latitude2) * sin(dlon / 2) ** 2

    c = 2 * asin(sqrt(a))

    # Radius of earth in meters
    r = 6371000

    # ~12 km/h average bus velocity in Wroclaw
    velocity = 12 * 0.28

    # calculate the result
    return (c * r / velocity)