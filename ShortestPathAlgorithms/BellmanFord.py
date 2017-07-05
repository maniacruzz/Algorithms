from Graph import Graph
import sys

def findShortestPath(g,sourceVertex):
    num_iterations=len(g.getAllVertex())-1 #num of vertices - 1 times iterations
    #if the distance reduces further at next iteration then negative weight cycle is detected

    distance=dict()
    parent=dict()

    for v in g.getAllVertex():
        distance[v]=sys.maxsize
    distance[sourceVertex]=0
    parent[sourceVertex]=None

    for i in range(num_iterations):
        for edge in g.getAllEdges():
            relax(edge,distance,parent)

    return distance

def relax(edge,distance,parent):
    newDistance=distance[edge.vertex1]+edge.weight
    if distance[edge.vertex2]>newDistance:
        distance[edge.vertex2]=newDistance
        parent[edge.vertex2]=edge.vertex1

def printMap(d):
    for key,val in d.items():
        print(key.data, " " , val)

def main():
    g=Graph("inputGraph.txt")
    sourceVertex=g.getAllVertex()[0]
    result=findShortestPath(g,sourceVertex)
    printMap(result)

if __name__=="__main__":
    main()
