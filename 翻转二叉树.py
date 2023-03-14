from typing import List
import collections


class TreeNode:
    def __init__(self,val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(arr):
    """Generate a binary tree with a list

    Args:
        arr ([type]): [description]

    Returns:
        [type]: [description]
    """
    if not arr:
        return
    i = 1
    n = len(arr)
    root = TreeNode(int(arr[0]))
    queue = collections.deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        if i<n and arr[i] != None:
            node.left = TreeNode(int(arr[i]))
            queue.append(node.left)
        i += 1
        if i<n and arr[i] != None:
            node.right = TreeNode(int(arr[i]))
            queue.append(node.right)
        i += 1
    return root

def tree_to_list(root):
    """Serialize a tree into an array

    Args:
        root ([type]): [description]

    Returns:
        [type]: [description]
    """    
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
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if not root:
            return None
        
        left = root.left
        right = root.right
        root.left = self.invertTree(right)
        root.right = self.invertTree(left)
        return root


if __name__ == '__main__':
    # ======= Test Case =======
    root = [4,2,7,1,3,6,9]
    # ====== Driver Code ======
    Sol = Solution()
    root = list_to_tree(root)
    res = Sol.invertTree(root)
    res = tree_to_list(res)
    print(res)