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

def linked_list_to_list(head):
    if not head:
        return []
    
    arr = []
    while head:
        arr.append(head.val)
        head = head.next

    return arr


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        cur = head
        prev = None
        while cur != None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev
        

if __name__ == "__main__":
    # ======= Test Case =======
    head = [1,2,3,4,5]
    # ====== Driver Code ======
    Sol = Solution()
    head = list_to_linked_list(head)
    res = Sol.reverseList(head)
    res = linked_list_to_list(res)
    print(res)