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
        
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()

inp = [i for i in input("Enter the BST values and search value: ").split(", ")]

bst_inp = [int(i) for i in inp[0].split()]
print(f"Input: root = {bst_inp}, val = {inp[1]}")
for i in bst_inp :
    root = T.insert(i)

new_root = T.search_val(root,int(inp[1]))
print("Output:",T.search_child(new_root))