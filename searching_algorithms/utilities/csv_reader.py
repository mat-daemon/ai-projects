from csv import reader

from searching_algorithms.utilities.Edge import Edge


class CsvReader:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.edges = []

    def read_file(self):
        print(self.csv_file)
        with open(self.csv_file, encoding = 'utf-8') as f:
            csv_reader = reader(f)
            header = next(csv_reader)

            for line in csv_reader:
                line = line[2:]
                self.edges.append(Edge(*line))

    def print_edges(self):
        for edge in self.edges:
            print(edge)


