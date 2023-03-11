from typing import Optional


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(arr):
    dummy = ListNode(-1)
    cur = dummy

    for i in range(len(arr)):
        node = ListNode(arr[i])
        cur.next = node
        cur = node
    return dummy.next


def linked_list_to_list(head):
    arr = []
    
    while head:
        arr.append(head.val)
        head = head.next

    return arr


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


if __name__ == '__main__':
    # 考查递归和迭代
    # ======= Test Case =======
    l1 = [1,2,4]
    l2 = [1,3,4]

    l1 = list_to_linked_list(l1)
    l2 = list_to_linked_list(l2)
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.mergeTwoLists(l1, l2)
    res = linked_list_to_list(res)
    print(res)
