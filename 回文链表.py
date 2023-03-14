from typing import List, Optional
import collections


class ListNode:
    """Definition for a singly-linked list node
    """    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked_list(arr):
    """Generate a linked list with a list

    Args:
        arr ([type]): [description]

    Returns:
        [type]: [description]
    """    
    dum = head = ListNode(0)
    for a in arr:
        node = ListNode(a)
        head.next = node
        head = head.next
    return dum.next

def linked_list_to_list(head):
    """Serialize a linked list into an array

    Args:
        head ([type]): [description]

    Returns:
        [type]: [description]
    """    
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr
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
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]


if __name__ == '__main__':
    # ======= Test Case =======
    head = [1,2,2,1]
    # ====== Driver Code ======
    Sol = Solution()
    head = list_to_linked_list(head)
    res = Sol.isPalindrome(head)
    print(res)