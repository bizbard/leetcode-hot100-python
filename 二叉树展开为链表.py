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
    def flatten(self, root: Optional[TreeNode]) -> None:
        # # 先序遍历
        # if not root:
        #     return []
        
        # preorder = []
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     preorder.append(node.val)
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)

        # # 单链表
        # def helper(root, arr):
        #     if not arr:
        #         return None
            
        #     if len(arr) == 1:
        #         node = TreeNode(arr[0])
        #         root.right = node
        #         return
            
        #     node = TreeNode(arr[0])
        #     root.right = node
        #     helper(node, arr[1:])

        # dummy = TreeNode(-1)
        # helper(dummy, preorder)

        # return dummy.right

        if not root:
            return []
        while root:
            if not root.left:
                root = root.right
            else:
                tmp = root.left
                while tmp.right:
                    tmp = tmp.right
                tmp.right = root.right
                root.right = root.left
                root.left = None
                root = root.right
                

if __name__ == "__main__":
    # 找左子树最右边的节点
    # 将原来的右子树接到左子树的最右边节点
    # 将左子树插入到右子树的地方
    # ======= Test Case =======
    root = [1,2,5,3,4,None,6]
    # ====== Driver Code ======
    Sol = Solution()
    root = list_to_tree(root)
    Sol.flatten(root)
    root = tree_to_list(root)
    print(root)