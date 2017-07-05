from Graph import Graph
import sys

def findShortestPath(g):
    num=len(g.getAllVertex())
    distance=[[sys.maxsize for i in range(num)] for j in range(num)]

    path=[[None for i in range(num)] for j in range(num)]

    for i in range(num):
        distance[i][i]=0

    for edge in g.getAllEdges():
        i=int(edge.vertex1.data)
        j=int(edge.vertex2.data)
        weight=edge.weight
        distance[i][j]=weight
        path[i][j]=i

    for k in range(num):
        for i in range(num):
            for j in range(num):
                if distance[i][k]==sys.maxsize or distance[k][j]==sys.maxsize:
                    continue
                newDistance=distance[i][k]+distance[k][j]
                if distance[i][j]>newDistance:
                    distance[i][j]=newDistance
                    path[i][j]=path[k][j]

    #if any of the element in the \ diagonal of distance matrix is negative then there is negative weighted cycle

    return distance

def relax(edge,distance,parent):
    newDistance=distance[edge.vertex1]+edge.weight
    if distance[edge.vertex2]>newDistance:
        distance[edge.vertex2]=newDistance
        parent[edge.vertex2]=edge.vertex1

def printList(d):
    for x in d:
        print(x)

def main():
    g=Graph("inputGraph.txt")
    result=findShortestPath(g)
    printList(result)

if __name__=="__main__":
    main()
