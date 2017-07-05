
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

def preOrderTraversal(root,list):
    if not root:
        return
    stack=[]
    stack.append(root)
    while stack:
        current=stack.pop()
        list.append(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

def main():
    root=Node(8)
    left=root.setLeft(5)
    right=root.setRight(11)
    leftleft=left.setLeft(3)
    leftright=left.setRight(7)
    rightleft=right.setLeft(9)
    rightright=right.setRight(13)
    list=[]
    preOrderTraversal(root,list)
    print(list)

if __name__=="__main__":
    main()