#ref - https://www.hackerearth.com/practice/notes/trees/
#ref - https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        


class Solution:
    
    def height(self, root):
        if root == None:
            return 0
        else:
            return 1 + max(self.height(root.left), self.height(root.right))
    
    def findDiameterofTree(self, root):
        
        #O(n^2) solution - for each node, find the height of left and right subtree and add them
        
        res = 0
        
        def diameter(self, root):
            nonlocal res
            
            if root == None:
                return 0
            else:
                lheight = self.height(root.left)
                rheight = self.height(root.right)
                
                res = max(res, lheight+rheight)
                
                diameter(root.left)
                diameter(root.right)
                
        diameter(root)
        return res
     
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        #https://www.youtube.com/watch?v=Rezetez59Nk&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=17
        res = 0
        
        def calcd(root):
            nonlocal res
             
            if root == None:
                return 0
            
            lh = calcd(root.left)
            rh = calcd(root.right)
        
            res = max(res, lh+rh)
            
            return 1 + max(lh, rh)
        
        calcd(root)
        return res

        
    
    # DFT - Depth First Traversal - Inorder, Preorder, Postorder
    
    def printInorder(self,root):
        if root:
            self.printInorder(root.left)
            print(root.val)
            self.printInorder(root.right)
    
    def printPreorder(self,root):
        if root:
            print(root.val)
            self.printPreorder(root.left)
            self.printPreorder(root.right)
            
    def printPostorder(self,root):
        if root:
            self.printPostorder(root.left)
            self.printPostorder(root.right)
            print(root.val)
        
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        def revbt(root):
            
            if root is None:
                return None
            
            if root.left != None and root.right != None:
                root.left, root.right = root.right, root.left
                revbt(root.left)
                revbt(root.right)
                
        
        revbt(root)
        return root
    
    def maxDepth(self, root: TreeNode) -> int:
        
        if root == None:
            return 0
                
        if root.left == None and root.right == None:
            return 1
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    def isBalanced(self, root: TreeNode) -> bool:
        
        res = True
        
        def checkBal(root):
            nonlocal res
            
            if root == None:
                return 0
            
            lh = 1+ checkBal(root.left)
            rh = 1 + checkBal(root.right)
            
            if abs(lh-rh) > 1:
                res = False
            
            return max(lh, rh)
        
        checkBal(root)
        return res
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        res = True
        
        def chk(p,q):
            nonlocal res
            
            if p and q:
                
                if p.val != q.val:
                    res = False
                
                chk(p.left, q.left)
                chk(p.right, q.right)
                
            elif p and not q or q and not p:
                res = False
        
        chk(p,q)
        return res
        
    def isSameBinaryTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameBinaryTree(p.left, q.left) and self.isSameBinaryTree(p.right, q.right)
        elif p and not q or q and not p:
            return False
        elif not p and not q:
            return True
        
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        
        if root == None:
            return False
        
        if root and subRoot:
            return self.isSameBinaryTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
    #BFT - Breadth First Traversal - Level Order Traversal
    
    def BFT(self, root):
        
        if root == None:
            return
        
        queue = []
        queue.append(root)
        
        while queue:
            node = queue.pop(0)
            print(node.val)
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

        
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        
        res = []
        
        def level(root, level):
                
            if root == None:
                return
            
            if len(res) == level:
                res.append([])
            
            res[level].append(root.val)
            
            level(root.left, level+1)
            level(root.right, level+1)    
            
        level(root, 0)
        return res
    
s = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print(s.diameterOfBinaryTree(root))