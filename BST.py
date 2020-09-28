class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        return self.insert_help(self.root,new_val)
    
    
    def insert_help(self,root,new_val):
        if root.value>new_val:
            if root.left:
                return self.insert_help(root.left,new_val)
            else:
                root.left=Node(new_val)
        else:
            if root.right:
                return self.insert_help(root.right,new_val)
            else:
                root.right=Node(new_val)
            
        

    def search(self, find_val):
        if self.BSTSearch(self.root,find_val):
            return True
        else:
            return False
        
    def BSTSearch(self,root,find_val):
        if root:
            if root.value==find_val:
                return True
            elif root.value<find_val:
                return self.BSTSearch(root.right,find_val)
            else:
                return self.BSTSearch(root.left,find_val)
    
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)