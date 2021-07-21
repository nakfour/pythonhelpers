class Node:
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

# Inorder traversal
# Left -> Root -> Right
    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            print(root.data)
            self.inorderTraversal(root.right)

# Postorder traversal
# Left -> Root -> Right
    def postorderTraversal(self, root):
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            print(root.data)

# Pre traversal
# Root -> Left -> Right
    def preorderTraversal(self, root):
        if root:
            print(root.data)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)

    def createBSTTree(self, datarray, start, end):
        if(end < start):
            return None
        mid = (start+end)//2
        newNode = Node(datarray[mid])
        newNode.left = self.createBSTTree(datarray, start, mid - 1)
        newNode.right = self.createBSTTree(datarray, mid + 1, end)
        return newNode

    #convert a sorted array into a BTS
    def convertArrayToBinaryTreeSearch(self, datarray):
        sizeofarray = len(datarray)-1
        return self.createBSTTree(datarray, 0,len(datarray)-1)

    #Check if a binary tree is balanced, ie at any node, height does not differ by more than one
    def checkBTBalanced(self, root):
        return self.checkHeight(self, root)

    def checkHeight(self, root):
        if (root is None):
            return -1
        rightHeight = self.checkHeight(root.right)
        leftHeight = self.checkHeight(root.left)
        if abs(rightHeight - leftHeight) > 1:
            return False
        if leftHeight is False or rightHeight is False:
            return False
        newHeight= max(leftHeight, rightHeight) + 1
        return newHeight

    #check if a tree is a binary tree search, leftnodedata<=nodedata<rightdata
    def checkBTS(self, root):
        return self.checkBTSRecur(None, None, root)

    def checkBTSRecur(self, min, max, root):
        if root is None:
            return True
        if min is not None and root.data <= min:
            return False
        if max is not None and root.data > max:
            return False

        if not self.checkBTSRecur(min,root.data,root.left) or not self.checkBTSRecur(root.data,max,root.right):
            return False
        return True





