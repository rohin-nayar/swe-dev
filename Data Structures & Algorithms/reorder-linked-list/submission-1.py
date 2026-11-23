# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 1.) Find the middle of the list using slow/fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2.) Split and reverse the second half
        second = slow.next
        slow.next = None # cut the first half
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        # prev is the head of the reversed second half

        # 3.) Merge two halves
        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2