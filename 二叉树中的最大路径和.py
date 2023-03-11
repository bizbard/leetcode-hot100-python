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
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def maxGain(root):
            if not root:
                return 0
            
            leftGain = max(maxGain(root.left), 0)
            rightGain = max(maxGain(root.right), 0)

            priceNewpath = root.val + leftGain + rightGain

            self.maxSum = max(self.maxSum, priceNewpath)

            return root.val + max(leftGain, rightGain)
        
        maxGain(root)

        return self.maxSum


if __name__ == "__main__":
    # ======= Test Case =======
    root = [-10,9,20,None,None,15,7]
    # ====== Driver Code ======
    Sol = Solution()
    root = list_to_tree(root)
    res = Sol.maxPathSum(root)
    print(res)