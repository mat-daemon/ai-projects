import math
from utilities.Edge import Edge

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.parent = None
        self.cost = math.inf
        self.neighbors = {}

    def __lt__(self, other):
        return self.cost < other.cost


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.nodes = {}

    def create_graph(self):
        for edge in self.edges:
            if edge.start not in self.nodes:
                node = Node(edge.start)
                self.nodes[node.name] = node

            if edge.end not in self.nodes[edge.start].neighbors:
                self.nodes[edge.start].neighbors[edge.end] = []

            if edge.end not in self.nodes:
                node = Node(edge.end)
                self.nodes[node.name] = node

            self.nodes[edge.start].neighbors[edge.end].append(edge)

