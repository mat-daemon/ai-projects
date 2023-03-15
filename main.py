import heapq

from utilities.csv_reader import CsvReader
from utilities.Graph import Graph, Node
from searching_algorithms.dijkstra import dijkstra

file_path = 'utilities/connection_graph.csv'

reader = CsvReader(file_path)
reader.read_file()

g = Graph(reader.edges)
g.create_graph()

dijkstra(g, "pl. Wróblewskiego", "Wiejska", "15:38:00")





