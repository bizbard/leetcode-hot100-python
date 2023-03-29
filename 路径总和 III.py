import collections
from typing import List, Optional
    
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
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

class Solution:
    # def pathSum(self, root: TreeNode, targetSum: int) -> int:
    #     def rootSum(root, targetSum):
    #         if root is None:
    #             return 0

    #         ret = 0
    #         if root.val == targetSum:
    #             ret += 1

    #         ret += rootSum(root.left, targetSum - root.val)
    #         ret += rootSum(root.right, targetSum - root.val)
    #         return ret
        
    #     if root is None:
    #         return 0
            
    #     ret = rootSum(root, targetSum)
    #     ret += self.pathSum(root.left, targetSum)
    #     ret += self.pathSum(root.right, targetSum)
    #     return ret

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        def dfs(root, curr):
            if not root:
                return 0
            
            ret = 0
            curr += root.val
            ret += prefix[curr - targetSum]
            prefix[curr] += 1
            ret += dfs(root.left, curr)
            ret += dfs(root.right, curr)
            prefix[curr] -= 1

            return ret

        return dfs(root, 0)


if __name__ == '__main__':
    # ======= Test Case =======
    root = [10,5,-3,3,2,None,11,3,-2,None,1]
    targetSum = 8
    # ====== Driver Code ======
    Sol = Solution()
    root = list_to_tree(root)
    res = Sol.pathSum(root, targetSum)
    print(res)