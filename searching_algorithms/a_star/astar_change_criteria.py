import heapq
import math
from math import inf

from searching_algorithms.utilities.Graph import Graph
from searching_algorithms.utilities.heuristics import distance_by_coordinates_heuristic
from searching_algorithms.utilities.route_printers import print_route, save_route


def astar_line_change_criteria(graph : Graph, start, end, start_time):
    open_queue = []
    # this cost is added when line is changed
    # it must be big enough to make line changing not cost-effective
    line_change_cost = 10000

    # mark that heuristic cost is added as an attribute to all nodes
    for node in graph.nodes:
        graph.nodes[node].heuristic_cost = inf
        # change 1-dimensional cost to multi-dimensional cost, each for one line
        graph.nodes[node].cost = inf
        graph.nodes[node].cheapest_lines = []
        graph.nodes[node].parent = {}

    start_node = graph.nodes[start]
    start_node.cost = 0
    # set all possible line costs to 0 in the start node
    for line in graph.lines:
        start_node.cheapest_lines.append(line)

    heapq.heappush(open_queue, (0, start_node))

    while len(open_queue) > 0:
        node_cost_tuple = heapq.heappop(open_queue)
        node = node_cost_tuple[1]

        if node.name == end:
            print("Number of changes: ", graph.nodes[end].cost)
            # print_route(graph.nodes[end])
            # save_route(graph.nodes[end])
            return

        for neighbor in node.neighbors.keys():
            graph.nodes[neighbor].heuristic_cost = distance_by_coordinates_heuristic(graph.nodes[neighbor],
                                                                                     graph.nodes[end])
            for edge in node.neighbors[neighbor]:
                cost = node.cost
                # change line because it does not exist in the node
                if edge.line not in node.cheapest_lines:
                    cost = cost + line_change_cost

                if edge.line not in graph.nodes[neighbor].cheapest_lines and graph.nodes[neighbor].cost == cost:
                    graph.nodes[neighbor].cheapest_lines.append(edge.line)
                    graph.nodes[neighbor].parent[edge.line] = node

                    heapq.heappush(open_queue, (cost + graph.nodes[neighbor].heuristic_cost, graph.nodes[neighbor]))

                if graph.nodes[neighbor].cost > cost:
                    graph.nodes[neighbor].cost = cost
                    graph.nodes[neighbor].cheapest_lines = [edge.line]

                    graph.nodes[neighbor].parent = {}
                    graph.nodes[neighbor].parent[edge.line] = node

                    heapq.heappush(open_queue, (cost + graph.nodes[neighbor].heuristic_cost, graph.nodes[neighbor]))



