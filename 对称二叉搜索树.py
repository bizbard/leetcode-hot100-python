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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(left, right):
            if not left and not right:
                return True
            
            if not (left and right):
                return False
            
            if left.val != right.val:
                return False
            
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)
    

if __name__ == '__main__':
    # ======= Test Case =======
    root = [1,2,2,3,4,4,3]
    # ====== Driver Code ======
    Sol = Solution()
    root = list_to_tree(root)
    res = Sol.isSymmetric(root)
    print(res)