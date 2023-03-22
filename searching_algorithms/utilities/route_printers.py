import math
import os
import time

from datetime import datetime


def save_route(prefix, node):
    route = []
    arrival_line = None

    if hasattr(node, "cheapest_lines"):
        arrival_line = node.cheapest_lines[0]


    while node.parent is not None:
        if type(node.parent) is dict:
            if arrival_line not in node.cheapest_lines:
                arrival_line = node.cheapest_lines[0]
            node.parent = node.parent[arrival_line]
            node.edge = node.edge[arrival_line]

        route.insert(0, node)
        node = node.parent

    for node in route:
        print(node.name)

    absolute_path = os.path.dirname(__file__)
    relative_path = "../routes/" + prefix + '.csv'
    full_path = os.path.join(absolute_path, relative_path)

    with open(full_path, 'w', encoding='utf-8') as file:
        file.write("Name,Latitude,Longitude,Line,Time\n")
        for node in route:
            arrival_time = time.strftime('%H:%M:%S', time.gmtime(node.edge.arrival))
            file.write(f"{node.name},{node.latitude},{node.longitude},{node.edge.line},{arrival_time}\n")



def print_route(node):
    if node.parent is None:
        print(node.name)
        return
    else:
        print_route(node.parent)
        print(node.name)

