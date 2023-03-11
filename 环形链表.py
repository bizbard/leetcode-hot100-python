import collections
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked_list(arr):
    if not arr:
        return None
    
    dummy = ListNode(-1)
    cur = dummy
    for a in arr:
        node = ListNode(a)
        cur.next = node
        cur = node
    return dummy.next

def get_cycle_list_node(head, pos):
    """
    Args:
        head ([type]): [description]
        pos ([type]): [description]

    Returns:
        [type]: [description]
    """    
    if not head:
        return None
    
    dummy = ListNode(-1)
    cur = dummy
    for i, he in enumerate(head):
        node = ListNode(he)
        cur.next = node
        cur = node

        if i == pos:
            tail = node

        if i == len(head) - 1:
            node.next = tail
            
    return dummy.next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False


if __name__ == "__main__":
    # ======= Test Case =======
    head = [3,2,0,-4]
    pos = 1
    # ====== Driver Code ======
    Sol = Solution()
    root = get_cycle_list_node(head, pos)
    res = Sol.hasCycle(root)
    print(res)