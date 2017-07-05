from Graph import Graph
from MinHeap import BinaryMinHeap
import sys

def findShortestPath(g,sourceVertex):
    distance=dict()
    vertexParent=dict()
    minHeap=BinaryMinHeap()
    for v in g.getAllVertex():
        minHeap.add(v,sys.maxsize)

    minHeap.decrease(sourceVertex,0)

    vertexParent[sourceVertex]=None

    while not minHeap.isEmpty():
        heapnode = minHeap.extractMin()
        currentVertex=heapnode.key
        distance[currentVertex]=heapnode.weight
        for edge in currentVertex.getAllEdges():
            adjacent=edge.vertex2
            if not minHeap.containsKey(adjacent):
                continue
            newDistance=distance.get(currentVertex)+edge.weight
            if newDistance<minHeap.getWeight(adjacent):
                minHeap.decrease(adjacent,newDistance)
                distance[adjacent]=newDistance
                vertexParent[adjacent]=currentVertex
    return distance
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