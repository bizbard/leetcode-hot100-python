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


def tree_to_list(root):
    if not root:
        return []
    
    arr = []
    queue = collections.deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        if node:
            arr.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            arr.append(None)
    
    return arr


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = []
        self.temp = 0

        def depth(root):
            if not root:
                return 0
            
            leftDepth = depth(root.left)
            rightDepth = depth(root.right)
            
            return 1 + max(leftDepth, rightDepth)


        def dfs(root):
            if not root:
                return 
            self.temp = 0
            self.res.append(depth(root))
            dfs(root.left)
            dfs(root.right)
                

        dfs(root)
        return max(self.res)

if __name__ == "__main__":
    # ======= Test Case =======
    root = [1, 2, 3, 4, 5]
    # ====== Driver Code ======
    Sol = Solution()
    root = list_to_tree(root)
    res = Sol.diameterOfBinaryTree(root)
    print(res)