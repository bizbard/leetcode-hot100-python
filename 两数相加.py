from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(arr):
    dum = head = ListNode(0)
    for a in arr:
        node = ListNode(a)
        head.next = node
        head = node
    return dum.next


def linked_list_to_list(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr


class Solution():
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def step(l1, l2, l, carry):
            if not l1 and not l2:
                if carry == 1:
                    tail = ListNode(carry)
                    l.next = tail
                return

            t = carry
            if l1:
                t = t + l1.val
                l1 = l1.next

            if l2:
                t = t + l2.val
                l2 = l2.next

            value = t % 10
            carry = t // 10
            l.next = ListNode(value)
            step(l1, l2, l.next, carry)

        dum = ListNode(-1)
        step(l1, l2, dum, carry=0)
        return dum.next


if __name__ == '__main__':
    # ======= Test Case =======
    l1 = [2,4,3]
    l2 = [5,6,4]
    
    l1 = list_to_linked_list(l1)
    l2 = list_to_linked_list(l2)
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.addTwoNumbers(l1, l2)
    res = linked_list_to_list(res)
    print(res)