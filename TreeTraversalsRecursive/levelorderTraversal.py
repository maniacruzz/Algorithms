
class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None

    def setLeft(self,val):
        self.left=Node(val)
        return self.left

    def setRight(self,val):
        self.right=Node(val)
        return self.right

def printGivenLevel(root,height,list):
    if not root:
        return
    if height==1:
        list.append(root.val)
    elif height>1:
        printGivenLevel(root.left,height-1,list)
        printGivenLevel(root.right,height-1,list)

def levelOrderTraversal(root,list):
    h=getHeight(root)
    for i in range(1,h+1):
        printGivenLevel(root,i,list)

def getHeight(root):
    if not root:
        return 0
    return max(getHeight(root.right),getHeight(root.left))+1


def main():
    root=Node(8)
    left=root.setLeft(5)
    right=root.setRight(11)
    leftleft=left.setLeft(3)
    leftright=left.setRight(7)
    rightleft=right.setLeft(9)
    rightright=right.setRight(13)
    list=[]
    levelOrderTraversal(root,list)
    print(list)

if __name__=="__main__":
    main()