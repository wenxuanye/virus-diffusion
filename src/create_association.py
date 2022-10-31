import networkx as nx
import numpy as np

# build a ER graph
class Graph(object):
    def __init__(self, N, p):
        self.N = N
        self.p = p
        self.G = nx.erdos_renyi_graph(N, p)
        self.A = self.create_adjacency_matrix()
    def create_adjacency_matrix(self):
        A = nx.adjacency_matrix(self.G)
        return np.array(A.todense())
    def show_graph(self):
        nx.draw(self.G, with_labels=True)
