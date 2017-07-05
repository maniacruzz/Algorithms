
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

def peek(stack):
    if stack:
        return stack[-1]
    return None

def printStack(s):
    l=[n.val for n in s]
    print(l)

def postOrderTraversal(root,list):
    if not root:
        return
    stack = []
    current=root
    while True:
        while root:
            if root.right:
                stack.append(root.right)
            stack.append(root)
            printStack(stack)
            root=root.left
        print("list ",list)
        root=stack.pop()
        if root.right and root.right==peek(stack):
            stack.pop()
            stack.append(root)
            root=root.right
        else:
            list.append(root.val)
            root=None

        if not stack:
            break



def main():
    root=Node(8)
    left=root.setLeft(5)
    right=root.setRight(11)
    leftleft=left.setLeft(3)
    leftright=left.setRight(7)
    rightleft=right.setLeft(9)
    rightright=right.setRight(13)
    list=[]
    postOrderTraversal(root,list)
    print(list)

if __name__=="__main__":
    main()