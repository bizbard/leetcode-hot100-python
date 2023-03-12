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

def list_to_interacted_linked_list(listA, listB, intersectVal, skipA, skipB):
    if intersectVal == 0:
        return list_to_linked_list(listA), list_to_linked_list(listB)
    
    common = listA[skipA:]
    common = list_to_linked_list(common)

    dummyA = ListNode(-1)
    cur = dummyA
    for a in listA[:skipA]:
        node = ListNode(a)
        cur.next = node
        cur = node
    cur.next = common

    dummyB = ListNode(-1)
    cur = dummyB
    for a in listB[:skipB]:
        node = ListNode(a)
        cur.next = node
        cur = node
    cur.next = common

    return dummyA, dummyB

def linked_list_to_list(head):
    if not head:
        return []
    
    arr = []
    while head:
        arr.append(head.val)
        head = head.next

    return arr


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not (headA and headB):
            return None
        
        la = headA
        lb = headB

        while la or lb:
            if la == lb:
                return la.val
            
            if la.next and not lb.next:
                la = la.next
                lb = headA
            elif lb.next and not la.next:
                la = headB
                lb = lb.next
            else:
                la = la.next
                lb = lb.next

        return None
        

if __name__ == "__main__":
    # ======= Test Case =======
    intersectVal = 8
    listA = [4,1,8,4,5]
    listB = [5,6,1,8,4,5]
    skipA = 2
    skipB = 3
    # ====== Driver Code ======
    Sol = Solution()
    headA, headB = list_to_interacted_linked_list(listA, listB, intersectVal, skipA, skipB)
    res = Sol.getIntersectionNode(headA, headB)
    print(res)