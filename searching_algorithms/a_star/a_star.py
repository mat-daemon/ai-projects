import heapq
from math import radians, cos, sin, asin, sqrt, inf

from utilities.Graph import Graph


def astar(graph : Graph, start, end, start_time):
    start_time_split = start_time.split(":")
    start_time = int(start_time_split[0]) * 3600 + int(start_time_split[1]) * 60 + int(start_time_split[2])

    open_queue = []

    # assign heuristic based function attribute to all nodes
    for node in graph.nodes:
        graph.nodes[start].heuristic_cost = inf

    graph.nodes[start].cost = 0
    graph.nodes[start].heuristic_cost = 0

    heapq.heappush(open_queue, (graph.nodes[start].cost + graph.nodes[start].heuristic_cost, graph.nodes[start].name))

    while len(open_queue) > 0:
        node_cost_tuple = heapq.heappop(open_queue)
        node = graph.nodes[node_cost_tuple[1]]

        if node.name == end:
            print(graph.nodes[end].cost)

        if not node.visited:
            node.visited = True

            for neighbor in node.neighbors.keys():
                if not any(neighbor in n for n in open_queue) and not graph.nodes[neighbor].visited:
                    for edge in node.neighbors[neighbor]:
                        if edge.departure >= node.cost + start_time:
                            graph.nodes[neighbor].heuristic_cost = distance_by_coordinates_heuristic(graph.nodes[neighbor], graph.nodes[end])

                            cost = node.cost + (edge.arrival - edge.departure) + \
                                   (edge.departure - (node.cost + start_time))

                            if graph.nodes[neighbor].cost > cost:
                                graph.nodes[neighbor].cost = cost
                                graph.nodes[neighbor].parent = node
                                heapq.heappush(open_queue, (graph.nodes[neighbor].cost + graph.nodes[neighbor].heuristic_cost, neighbor))


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


