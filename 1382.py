#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        v=[]
        def dfs(Node):
            if Node:
                dfs(Node.left)
                v.append(Node.val)
                dfs(Node.right)
        dfs(root)
        print(v)
        def bst(v):
            if not v:
                return None
            mid=len(v)//2
            root=TreeNode(v[mid])
            root.left=bst(v[:mid])
            root.right=bst(v[mid+1:])
            return root
        return bst(v)
