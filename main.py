import heapq
from searching_algorithms.utilities.heuristics import distance_by_coordinates_heuristic
from searching_algorithms.utilities.csv_reader import CsvReader
from searching_algorithms.utilities.Graph import Graph, Node
from searching_algorithms.dijkstra import dijkstra
from searching_algorithms.a_star.astar_time_criteria import astar_time_criteria
from searching_algorithms.utilities.heuristics import distance_by_coordinates_heuristic
from searching_algorithms.a_star.astar_change_criteria import astar_line_change_criteria
from searching_algorithms.tabu_search.tabu_search import tabu_search, path_cost


if __name__ == '__main__':
    file_path = 'searching_algorithms/utilities/connection_graph.csv'

    reader = CsvReader(file_path)
    reader.read_file()

    g = Graph(reader.edges)
    g.create_graph()

    # check dijkstra algorithm travel schedule output
    #dijkstra(g, "pl. Wróblewskiego", "Wiejska", "15:38:00")
    # g.clear_graph()
    #dijkstra(g, "ROD Bielany", "KOWALE", "15:38:00")
    # dijkstra(g, "pl. Wróblewskiego", "Wołowska", "15:38:00")
    #g.clear_graph()

    #astar(g, "pl. Wróblewskiego", "Wiejska", "15:38:00")
    # g.clear_graph()

    # astar_line_change_criteria(g, "KSIĘŻE MAŁE", "LEŚNICA", "15:38:00")
    # astar_line_change_criteria(g, "Wzgórze Partyzantów", "C.H. Aleja Bielany", "15:38:00")
    # astar_line_change_criteria(g, "pl. Wróblewskiego", "LEŚNICA", "15:38:00")
    # g.clear_graph()


    tabu_search_nodes = ["Piastowska", "Górnickiego", "Ogród Botaniczny", "Katedra", "Reja"]

    tabu_search_nodes = ["Piastowska", "Górnickiego", "Ogród Botaniczny", "Katedra", "Reja", "Wyszyńskiego", "Prusa", "Piastowska"]

    tabu_search(g, "PL. GRUNWALDZKI", tabu_search_nodes, "12:00:00")



