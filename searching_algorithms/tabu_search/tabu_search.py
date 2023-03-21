import math
import random

from searching_algorithms.utilities.Graph import Graph

# algorithm that searches for shortest path starting in start_node and passing through the all stop_nodes
def tabu_search(graph : Graph, start_node, stop_nodes, start_time):
    start_time_split = start_time.split(":")
    start_time = int(start_time_split[0]) * 3600 + int(start_time_split[1]) * 60 + int(start_time_split[2])

    n_nodes = len(stop_nodes)
    max_iterations = max(n_nodes ** 2, 10000)
    turns_improved = 0
    improve_thresh = 2 * math.floor(math.sqrt(max_iterations))

    tabu_list = []
    tabu_tenure = n_nodes

    best_solution_cost = math.inf
    current_solution = stop_nodes[:]
    random.shuffle(current_solution)

    best_solution = current_solution[:]

    for iteration in range(max_iterations):
        if turns_improved > improve_thresh:
            break
        best_neighbor = None
        best_neighbor_cost = float('inf')
        tabu_candidate = (0, 0)
        for i in range(n_nodes):
            for j in range(i + 1, n_nodes):
                neighbor = current_solution[:]
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbor.insert(0, start_node)
                neighbor_cost = path_cost(graph, neighbor, start_time)
                if (i, j) not in tabu_list:
                    if neighbor_cost < best_neighbor_cost:
                        best_neighbor = neighbor[:]
                        best_neighbor_cost = neighbor_cost
                        tabu_candidate = (i, j)

        if best_neighbor is not None:
            current_solution = best_neighbor[:]
            tabu_list.append(tabu_candidate)
            if len(tabu_list) > tabu_tenure:
                tabu_list.pop(0)
            if best_neighbor_cost < best_solution_cost:
                best_solution = best_neighbor[:]
                best_solution_cost = best_neighbor_cost
                turns_improved = 0
            else:
                turns_improved = turns_improved + 1
        else:
            random.shuffle(current_solution)
        # print("Iteration {}: Best solution cost = {}".format(iteration, best_solution_cost))

    print("Best solution: {}".format(best_solution))
    print("Best solution cost: {}".format(best_solution_cost))


def path_cost(graph, nodes_on_path, start_time):
    cost = 0

    for i in range(len(nodes_on_path) - 1):
        neighbor1 = nodes_on_path[i]
        neighbor2 = nodes_on_path[i+1]

        # nodes are no neighbors
        if neighbor2 not in graph.nodes[neighbor1].neighbors.keys():
            return math.inf

        for edge in graph.nodes[neighbor1].neighbors[neighbor2]:
            if edge.departure >= start_time:
                start_time = edge.departure
                cost += edge.arrival - edge.departure
                break

    if nodes_on_path[0] not in graph.nodes[nodes_on_path[-1]].neighbors.keys():
        return math.inf

    # last node on path - first node path
    for edge in graph.nodes[nodes_on_path[-1]].neighbors[nodes_on_path[0]]:
        if edge.departure >= start_time:
            cost += edge.arrival - edge.departure
            break

    return cost