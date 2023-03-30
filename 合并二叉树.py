import collections
from typing import List, Optional
    

class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(arr):
    if not arr:
        return None
    
    root = TreeNode(arr[0])
    i = 1
    queue = collections.deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        if i < len(arr) and arr[i]:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i]:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root

def tree_to_list(root):
    if not root: return []
    queue = collections.deque()
    queue.append(root)
    res = []
    while queue:
        node = queue.popleft()
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else: res.append(None)
    return res



class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root1, root2):
            if not root1:
                return root2
            if not root2:
                return root1
        
            merged = TreeNode(root1.val + root2.val) 
            merged.left = dfs(root1.left, root2.left)
            merged.right = dfs(root1.right, root2.right)
            return merged

        return dfs(root1, root2)


if __name__ == '__main__':
    # ======= Test Case =======
    root1 = [1,3,2,5]
    root2 = [2,1,3,None,4,None,7]
    # ====== Driver Code ======
    Sol = Solution()
    root1 = list_to_tree(root1)
    root2 = list_to_tree(root2)
    res = Sol.mergeTrees(root1, root2)
    res = tree_to_list(res)
    print(res)