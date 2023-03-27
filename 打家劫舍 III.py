import collections
from typing import List, Optional


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
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root.left and not root.right:
                return [root.val, 0]
            
            left1, right1 = dfs(root.left) if root.left else [0, 0]
            left2, right2 = dfs(root.right) if root.right else [0, 0]
            return [root.val+right1+right2, max(left1, right1) + max(left2, right2)]
        
        return max(dfs(root))


if __name__ == '__main__':
    # ======= Test Case =======
    root = [3,2,3,None,3,None,1]
    # ====== Driver Code ======
    Sol = Solution()
    root = list_to_tree(root)
    res = Sol.rob(root)
    print(res)