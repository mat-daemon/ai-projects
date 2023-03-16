import math
from utilities.Edge import Edge

class Node:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.visited = False
        self.parent = None
        self.cost = math.inf
        self.neighbors = {}
        self.longitude = longitude
        self.latitude = latitude

    def __lt__(self, other):
        return self.cost < other.cost


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.nodes = {}

    def create_graph(self):
        for edge in self.edges:
            if edge.start not in self.nodes:
                node = Node(edge.start, edge.start_lat, edge.start_lon)
                self.nodes[node.name] = node

            if edge.end not in self.nodes[edge.start].neighbors:
                self.nodes[edge.start].neighbors[edge.end] = []

            if edge.end not in self.nodes:
                node = Node(edge.end, edge.stop_lat, edge.stop_lon)
                self.nodes[node.name] = node

            self.nodes[edge.start].neighbors[edge.end].append(edge)

    def clear_graph(self):
        for node in self.nodes:
            self.nodes[node].visited = False
            self.nodes[node].parent = None
            self.nodes[node].cost = math.inf
