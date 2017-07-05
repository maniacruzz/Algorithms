
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

def levelOrderTraversal(root,list):
    if not root:
        return
    queue=[]
    queue.append(root)
    while queue:
        current=queue.pop(0)
        list.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

def levelOrderTraversal_Levelbylevel(root,list):
    if not root:
        return
    queue=[]
    queue.append((root,1))
    currlevel=1
    templist=[]
    while queue:
        current,level=queue.pop(0)
        if level!=currlevel:
            list.append(templist)
            templist=[]
            currlevel=level
        templist.append(current.val)
        if current.left:
            queue.append((current.left,currlevel+1))
        if current.right:
            queue.append((current.right,currlevel+1))
    list.append(templist)

def main():
    root=Node(8)
    left=root.setLeft(5)
    right=root.setRight(11)
    leftleft=left.setLeft(3)
    leftright=left.setRight(7)
    rightleft=right.setLeft(9)
    rightright=right.setRight(13)
    list=[]
    levelOrderTraversal_Levelbylevel(root,list)
    print(list)

if __name__=="__main__":
    main()