import heapq
import os
from datetime import datetime
from utilities.Graph import Graph


def dijkstra(graph : Graph, start, end, start_time):
    start_time_split = start_time.split(":")
    start_time = int(start_time_split[0]) * 3600 + int(start_time_split[1]) * 60 + int(start_time_split[2])

    queue = []

    graph.nodes[start].cost = 0

    # TODO: consider if it is necessary
    for node in graph.nodes:
        heapq.heappush(queue, (graph.nodes[node].cost, graph.nodes[node].name))

    while len(queue) > 0:
        node_cost_tuple = heapq.heappop(queue)
        node = graph.nodes[node_cost_tuple[1]]

        if not node.visited:
            node.visited = True

            for neighbor in node.neighbors.keys():
                if not graph.nodes[neighbor].visited:
                    for edge in node.neighbors[neighbor]:
                        # if next departure time is after the node arrival time and
                        if edge.departure >= node.cost + start_time:
                            # if cost to next node is lower than cost to current node plus travel time plus waiting time
                            cost = node.cost + (edge.arrival - edge.departure) + \
                                (edge.departure - (node.cost + start_time))

                            if graph.nodes[neighbor].cost > cost:
                                graph.nodes[neighbor].cost = cost
                                graph.nodes[neighbor].parent = node

                                heapq.heappush(queue, (cost, graph.nodes[neighbor].name))


    print('Travel cost: ' + str(graph.nodes[end].cost))

    print_route(graph.nodes[end])


def print_route(node):
    route = []

    while node.parent is not None:
        route.insert(0, node)
        node = node.parent

    for node in route:
        print(node.name)

    absolute_path = os.path.dirname(__file__)
    relative_path = "routes/route" + datetime.now().strftime("%d%m%Y%H%M%S") + '.csv'
    full_path = os.path.join(absolute_path, relative_path)

    with open(full_path, 'w') as file:
        file.write("Name,Latitude,Longitude\n")
        for node in route:
            file.write(f"{node.name},{node.latitude},{node.longitude}\n")




