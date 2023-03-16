import heapq

from utilities.csv_reader import CsvReader
from utilities.Graph import Graph, Node
from searching_algorithms.dijkstra import dijkstra
from searching_algorithms.a_star.a_star import distance_by_coordinates_heuristic, astar

if __name__ == '__main__':
    file_path = 'utilities/connection_graph.csv'

    reader = CsvReader(file_path)
    reader.read_file()

    g = Graph(reader.edges)
    g.create_graph()

    # check dijkstra algorithm travel schedule output
    #dijkstra(g, "pl. Wróblewskiego", "Wiejska", "15:38:00")
    dijkstra(g, "ROD Bielany", "KOWALE", "15:38:00")
    #g.clear_graph()
    #astar(g, "pl. Wróblewskiego", "Wiejska", "15:38:00")

    # check distance in straight line between two points in the graph
    # print(distance_by_coordinates_heuristic(g.nodes['Hallera'], g.nodes['Stalowa']))
    # print(distance_by_coordinates_heuristic(g.nodes['GALERIA DOMINIKAŃSKA'], g.nodes['DWORZEC GŁÓWNY']))

    # check astar algorithm travel schedule output



