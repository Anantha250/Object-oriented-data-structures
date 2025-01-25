class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
        return self.root

    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)
    
    def search_val(self,node, val) : 
        if node != None :
            
            if node.data == val :
                return node

            isFound = self.search_val(node.left, val)
            if isFound:
                return isFound
            isFound = self.search_val(node.right, val)
            if isFound:
                return isFound

    def search_child(self, node, child = []) :
        if node != None :
            child.append(node.data)
            self.search_child(node.left, child)
            self.search_child(node.right, child)
        return child   

    
    
    def preorder(self, node):
        if node is not None:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)

print("\nInorder Traversal:")
T.inorder(root)

print("\nPreorder Traversal:")
T.preorder(root)

print("\nPostorder Traversal:")
T.postorder(root)

print("\nTree Structure:")
T.printTree(root)
