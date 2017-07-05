import MinHeap,sys

class Node:
    def __init__(self,val):
        self.val=val
        self.neighbors=[]

class Graph:
    def __init__(self,edges,vertices):
        self.vertices=self.getvertices(edges,vertices)

    def getvertices(self,edges,vertices):
        vertexset=dict()
        for v in vertices:
            vertexset[v]=(Node(v))
        self.buildedges(edges,vertexset)
        return vertexset

    def buildedges(self,edges,vertexset):
        for edge in edges:
            node1 = vertexset.get(edge[1])
            node2 = vertexset.get(edge[2])
            node1.neighbors.append((edge[0], node2))
            node2.neighbors.append((edge[0], node1))

    def printGraph(self):
        for v in self.vertices:
            print(v)
            for x in (self.vertices[v].neighbors):
                print(x[0],x[1].val)

def mstPRIMS(g):
    result=[]
    heap=MinHeap.BinaryMinHeap()
    vertextoedge=dict()
    for v in g.vertices:
        heap.add(v,sys.maxsize)

    startvertex=list(g.vertices.keys())[0]

    heap.decrease(startvertex,0)

    while(not heap.isEmpty()):
        current=heap.extractMin()
        spanningTreeEdge=vertextoedge.get(current.key,None)
        if spanningTreeEdge:
            result.append(spanningTreeEdge)

        for edge in g.vertices[current.key].neighbors:
            adjVertex=edge[1].val
            weight=edge[0]
            if heap.containsKey(adjVertex) and heap.getWeight(adjVertex)>weight:
                heap.decrease(adjVertex,weight)
                vertextoedge[adjVertex]=(edge[0],current.key,adjVertex)
    return result





def readfile(filename):
    f=open(filename)
    data=f.readlines()
    v,e=[int(n) for n in data[0].split()]
    vertices,edges=data[1:v+1],data[v+1:]
    edgelist=[]
    vertexlist=set()
    for vertex in vertices:
        vertexlist.add(vertex.strip())
    for edge in edges:
        first,second,weight=edge.split(" ")
        edgelist.append((int(weight),first,second))
    return edgelist,vertexlist

def main():
    edges,vertices=readfile("inputgraph.txt")
    g=Graph(edges,vertices)
    #g.printGraph()
    result=mstPRIMS(g)
    #print(sorted(edges))
    print(result)
if __name__=="__main__":
    main()