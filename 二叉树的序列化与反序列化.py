import collections
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(arr):
    if not arr:
        return None

    i = 1
    root = TreeNode(arr[0])
    queue = collections.deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        node.left = None
        node.right = None
        if i < len(arr):
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr):
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root


class Solution:
    def serialize(self, root):
        if not root:
            return 'None'
        return str(root.val) + self.serialize(root.left) + self.serialize(root.right)
    
    def deserialize(self, data):
        if not data:
            return None

        dataList = data.split(',')
        return list_to_tree(dataList)
        



if __name__ == "__main__":
    # ======= Test Case =======
    root = [1,2,3,None,None,4,5]
    # ====== Driver Code ======
    Sol = Solution()
    root = list_to_tree(root)
    res = Sol.deserialize(Sol.serialize(root))
    print(res)