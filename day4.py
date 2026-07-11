## max depth My solutions
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 1
        if root == None:
            return 0
        
        stack = []
        stack.append(root)
        while(len(stack)!= 0):

            temp = []
            for node in stack:
                print(node.val)
                if node.left != None:
                    temp.append(node.left)
                if node.right != None:
                    temp.append(node.right)
            if len(temp) > 0:
                depth += 1
                stack = temp
            else:
                break
        return depth




# max depth fastest solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0 
            
            lefth = dfs(node.left)
            righth = dfs(node.right)

            return 1+ max(lefth, righth)

        return dfs(root)


### Same tree search (My solution)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = []
        if p == q == None:
            return True
        if (p == None and q != None) or (p != None and q == None):
            return False
        if p.val != q.val:
            return False
        stack.append((p,q))
        while len(stack) > 0:
            temp = []
            print(stack)
            for node1,node2 in stack:
                if node1.val != node2.val:
                    return False
                if (node1.left != None) and (node2.left != None):
                    temp.append((node1.left, node2.left))
                if (node1.right != None) and (node2.right != None):
                    temp.append((node1.right, node2.right))
                # check for children 
                if ((node1.left == None) and (node2.left != None) or
                    (node1.left != None) and (node2.left == None) or
                    (node1.right == None) and (node2.right != None) or
                    (node1.right != None) and (node2.right  == None)):
                    return False
                
                stack = temp

        return True




## Fastest solution to same tree search:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 


