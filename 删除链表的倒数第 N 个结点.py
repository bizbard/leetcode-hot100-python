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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def getLength(head):
            if not head:
                return 0
            
            i = 0
            while head:
                i += 1
                head = head.next
            return i
        
        length = getLength(head)
        dummy = ListNode(-1, head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next

        return dummy.next


if __name__ == '__main__':
    # 本题考查链表的遍历
    # ======= Test Case =======
    head = [1,2,3,4,5]
    n = 2
    head = list_to_linked_list(head)
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.removeNthFromEnd(head, n)
    res = linked_list_to_list(res)
    print(res)


