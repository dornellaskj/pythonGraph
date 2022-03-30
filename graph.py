import abc
import numpy as np


class Graph(abc.ABC):
    def __init__(self, numVerticies, directed=False):
        self.numVerticies = numVerticies
        self.directed = directed

        @abc.abstractmethod
        def add_edge(self, v1, v2, weight):
            pass

        @abc.abstractmethod
        def get_adjacent_verticies(self,v):
            pass

        @abc.abstractmethod
        def get_indegree(self,v):
            pass

        @abc.abstractmethod
        def get_edge_weight(self,v1, v2):
            pass

        @abc.abstractmethod
        def display(self):
            pass



class AdjacencyMatrixGraph(Graph):

    def __init__(self, numVerticies, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(numVerticies, directed)

        self.matrix = np.zeros((numVerticies, numVerticies))

    def add_edge(self, v1, v2, weight=1):
        #make sure you stay in the bounds of the graph
        if v1 >= self.numVerticies or v2 >= self.numVerticies or v1 < 0 or v2 < 0:
            raise ValueError("Werticies %d and %d are out of bounds" % (v1, v2))

        if weight < 1:
            raise ValueError("An edge cannot have weight < 1")

        self.matrix[v1][v2] = weight

        if self.directed == False:
            self.matrix[v2][v1] = weight
    
    def get_adjacent_verticies(self, v):
        if v < 0 or v >= self.numVerticies:
            raise ValueError("Cannot access vertex %d" % v)

        adjacent_verticies = []
        for i in range(self.numVerticies):
            if self.matrix[v][i] > 0:
                adjacent_verticies.append(i)
        return adjacent_verticies
    #measure edges flowing into each node
    def get_indegree(self, v):
        if v < 0 or v >= self.numVerticies:
            raise ValueError("cannot access vertex %d" % v)
        indegree = 0 
        for i in range(self.numVerticies):
            if self.matrix[i][v] > 0:
                indegree = indegree + 1
        
        return indegree

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.numVerticies):
            for v in self.get_adjacent_verticies(i):
                print(i, "-->", v)

g = AdjacencyMatrixGraph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)

for i in range(4):
    print("Adjacent to:", i, g.get_adjacent_verticies(i))

for i in range(4):
    print("Indegree:", i, g.get_indegree(i))

for i in range(4):
    for j in g.get_adjacent_verticies(i):
        print("Edge weight: ", i, " ", j, " weight: ", g.get_edge_weight(i, j))

g.display()



    

        