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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # 双指针找到中点
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None

        left, right = self.sortList(head), self.sortList(mid)
        dummy = ListNode(-1)
        cur = dummy
        while left and right:
            if left.val <= right.val:
                cur.next = left
                cur = left
                left = left.next
            else:
                cur.next = right
                cur = right
                right = right.next

        if not (left and right):
            cur.next = left if left else right

        return dummy.next
        

if __name__ == "__main__":
    # 归并排序
    # ======= Test Case =======
    head = [4,2,1,3]
    # ====== Driver Code ======
    Sol = Solution()
    head = list_to_linked_list(head)
    res = Sol.sortList(head)
    res = linked_list_to_list(res)
    print(res)