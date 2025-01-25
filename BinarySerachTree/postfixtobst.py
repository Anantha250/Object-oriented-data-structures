class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class ExpressionTree:
    def __init__(self):
        self.root = None

    def buildTree(self, postfix):
        stack = []

        for char in postfix:
            if char.isalnum(): 
                stack.append(Node(char))
            else: 
                node = Node(char)
                node.right = stack.pop()
                node.left = stack.pop()  
                stack.append(node)

    
        self.root = stack.pop()
        return self.root

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = ExpressionTree()
postfix = input('Enter Postfix Expression: ').split()

root = T.buildTree(postfix)

T.printTree(root)
