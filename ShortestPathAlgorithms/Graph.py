class Vertex:
    def __init__(self, data):
        self.data = data
        self.adjacent = []

    def addNeighbor(self, vertex2, weight):
        edge = Edge(self, vertex2, weight)
        self.adjacent.append(edge)
        return edge

    def getAllEdges(self):
        return self.adjacent


class Edge:
    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight

class Graph:
    def __init__(self,filename):
        self.vertices=[]
        self.edges=[]
        self.readfile(filename)

    def getAllVertex(self):
        return self.vertices

    def getAllEdges(self):
        return self.edges

    def readfile(self,filename):
        f = open(filename)
        data = f.readlines()
        v, e = [int(n) for n in data[0].split()]
        vertices, edges = data[1:v + 1], data[v + 1:]
        tempmap=dict()
        for vertex in vertices:
            v=Vertex(vertex.strip())
            self.vertices.append(v)
            tempmap[v.data]=v
        for edge in edges:
            first, second, weight = edge.strip().split(" ")
            edge=tempmap[first].addNeighbor(tempmap[second],int(weight))
            self.edges.append(edge)
            #tempmap[second].addNeighbor(tempmap[first], int(weight))