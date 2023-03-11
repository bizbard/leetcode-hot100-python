import collections
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(arr):
    if not arr:
        return None
    
    i = 1
    n = len(arr)
    root = TreeNode(arr[0])
    queue = collections.deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        if i<n and arr[i] != None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i<n and arr[i] != None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root


class Solution:
    # def isValidBST(self, root: TreeNode) -> bool:
    #     def helper(root, left, right):
    #         if not root:
    #             return True
            
    #         val = root.val
    #         if val <= left or val >= right:
    #             return False

    #         if not helper(root.right, val, right):
    #             return False
            
    #         if not helper(root.left, left, val):
    #             return False
            
    #         return True

    #     return helper(root, float("-inf"), float("inf"))
    pre = float("-inf")
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if not self.isValidBST(root.left) or root.val <= self.pre:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)
    

if __name__ == '__main__':
    # ======= Test Case =======
    root = [5,1,4,None,None,3,6]
    # ====== Driver Code ======
    Sol = Solution()
    root = list_to_tree(root)
    res = Sol.isValidBST(root)
    print(res)