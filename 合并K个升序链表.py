from typing import List, Optional


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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        n = len(lists)

        res = self.partition(lists, 0, n - 1)
        return res

    def partition(self, lists, left, right):
        if left == right:
            return lists[left] # output: node
        mid = left + (right - left) // 2
        l1 = self.partition(lists, left, mid)
        l2 = self.partition(lists, mid + 1, right) # 记得加一
        return self.mergeTwoLists(l1, l2)
    
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == '__main__':
    # 分而治之
    # ======= Test Case =======
    lists = [[1,4,5],[1,3,4],[2,6]]
    newlists = []

    for i, listItem in enumerate(lists):
        newlists.append(list_to_linked_list(listItem))
    # ====== Driver Code ======
    # newlists [node1, node2, ...]
    Sol = Solution()
    res = Sol.mergeKLists(newlists)
    res = linked_list_to_list(res)
    print(res)