import heapq
from utilities.Graph import Graph


def astar(graph : Graph, start, end, start_time):
    start_time_split = start_time.split(":")
    start_time = int(start_time_split[0]) * 3600 + int(start_time_split[1]) * 60 + int(start_time_split[2])

    open_queue = []

    graph.nodes[start].cost = 0

    for node in graph.nodes:
        heapq.heappush(open_queue, (graph.nodes[node].cost, graph.nodes[node].name))

    while len(open_queue) > 0:
        node_cost_tuple = heapq.heappop(open_queue)
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

                                heapq.heappush(open_queue, (cost, graph.nodes[neighbor].name))