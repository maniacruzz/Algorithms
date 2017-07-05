class Node:
    def __init__(self, weight, key):
        self.weight = weight
        self.key = key

class BinaryMinHeap:
    def __init__(self,):
        self.allNodes = []
        self.nodeposition = dict()

    def isEmpty(self):
        return len(self.allNodes)==0

    def containsKey(self,key):
        return (key in self.nodeposition)

    def swap(self,node1,node2):
        node1.key,node2.key=node2.key,node1.key
        node1.weight,node2.weight=node2.weight,node1.weight

    def updateMapPosition(self,key1,key2,pos1,pos2):
        self.nodeposition[key1]=pos1
        self.nodeposition[key2]=pos2

    def getWeight(self,key):
        pos=self.nodeposition[key]
        return self.allNodes[pos].weight

    def add(self,key,weight):
        node=Node(weight,key)
        self.allNodes.append(node)
        size=len(self.allNodes)
        current=size-1
        parentInd=(current-1)//2
        self.nodeposition[node.key]=current

        while (parentInd>=0):
            parentnode=self.allNodes[parentInd]
            currentnode=self.allNodes[current]
            if parentnode.weight>currentnode.weight:
                self.swap(currentnode,parentnode)
                self.updateMapPosition(currentnode.key,parentnode.key,current,parentInd)
                current=parentInd
                parentInd=(parentInd-1)//2
            else:
                break

    def decrease(self,key,newweight):
        current=self.nodeposition[key]
        self.allNodes[current].weight=newweight
        parentInd=(current-1)//2
        parentnode=self.allNodes[parentInd]
        currentnode=self.allNodes[current]
        while parentInd>=0:
            parentnode = self.allNodes[parentInd]
            currentnode = self.allNodes[current]
            if parentnode.weight>currentnode.weight:
                self.swap(currentnode,parentnode)
                self.updateMapPosition(currentnode.key,parentnode.key,current,parentInd)
                current=parentInd
                parentInd=(parentInd-1)//2
            else:
                break

    def extractMin(self):
        size=len(self.allNodes)-1
        minNode=Node(self.allNodes[0].weight,self.allNodes[0].key)

        self.allNodes[0].weight,self.allNodes[0].key=self.allNodes[size].weight,self.allNodes[size].key
        self.nodeposition.pop(minNode.key)
        self.nodeposition[self.allNodes[0].key]=0
        self.allNodes.pop()
        size-=1

        currentInd=0

        while True:
            leftInd=2*currentInd+1
            rightInd=2*currentInd+2
            if leftInd > size:
                break
            if rightInd>size:
                rightInd=leftInd

            smallInd=leftInd if self.allNodes[leftInd].weight<=self.allNodes[rightInd].weight else rightInd
            if self.allNodes[currentInd].weight > self.allNodes[smallInd].weight:
                self.swap(self.allNodes[currentInd],self.allNodes[smallInd])
                self.updateMapPosition(self.allNodes[currentInd].key,self.allNodes[smallInd].key,currentInd,smallInd)
                currentInd=smallInd
            else:
                break

        return minNode