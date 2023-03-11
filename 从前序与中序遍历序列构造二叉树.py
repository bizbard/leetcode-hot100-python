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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid+1])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root


if __name__ == "__main__":
    # ======= Test Case =======
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.buildTree(preorder, inorder)
    res = tree_to_list(res)
    print(res)