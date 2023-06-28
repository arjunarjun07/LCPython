
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBinarySearchTree:
    
    def __init__(self, root_node) -> None:
        self.root = root_node
        
    def __repr__(self) -> str:
        ls = []
        
        def inorder(root:TreeNode):
            nonlocal ls
            
            if root:
                inorder(root.left)
                ls.append(root.val)
                inorder(root.right)

        inorder(self.root)
        return str(ls)
        

    # Insert a node
    def insert(self, node, key):

        # Return a new node if the tree is empty
        if node is None:
            return TreeNode(key)

        # Traverse to the right place and insert the node
        if key < node.val:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        return node


    # Find the inorder successor
    def minValueNode(self, node:TreeNode):
        current = node

        # Find the leftmost leaf
        while current.left:
            current = current.left

        return current
    
    def MaxValNode(self, node:TreeNode):
        
        current = node
        
        while current.right:
            current = current.right
        
        return current
                        
    def search(self, node:TreeNode, val) -> TreeNode:
        if not node:
            return None
        elif val < node.val:
            return self.search(node.left, val)
        elif val > node.val:
            return self.search(node.right, val)
        else:
            return node
        
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        else:
            #leaf
            if not root.left and not root.right:
                root = None
            
            # 1 child - Left is null
            elif not root.left:
                temp = root
                root = root.right
                del temp
            
            #1 child - Right is null
            elif not root.right:
                temp = root
                root = root.left
                del temp
                
            #2 child
            else:
                #find inorder successor of the current node
                temp = self.minValueNode(root.right)
                
                #assign the value of it
                root.val = temp.val
                
                #now we can delete inorder successor
                root.right = self.deleteNode(root.right, temp.val)
        return root
    
root = TreeNode(5)
s = CBinarySearchTree(root)

s.insert(root, 3)
s.insert(root, 7)
s.insert(root, 1)
s.insert(root, 9)
s.insert(root, 100)
s.insert(root, 8)

s.search(root, 100)

s.deleteNode(root, 9)

print(s)
