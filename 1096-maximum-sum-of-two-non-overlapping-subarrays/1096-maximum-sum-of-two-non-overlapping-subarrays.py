
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Adds two numbers represented by linked lists.
        Each node contains a single digit and the digits are stored in reverse order.

        Args:
            l1 (ListNode): Head of first linked list.
            l2 (ListNode): Head of second linked list.

        Returns:
            ListNode: Head of the resulting linked list.
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry, digit = divmod(total, 10)
            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        """
        Return the maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.
        """
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def window_sum(start: int, length: int) -> int:
            return prefix[start + length] - prefix[start]

        max_total = 0
        # first before second
        for i in range(0, n - firstLen - secondLen + 1):
            sum_first = window_sum(i, firstLen)
            best_second = 0
            for j in range(i + firstLen, n - secondLen + 1):
                s2 = window_sum(j, secondLen)
                if s2 > best_second:
                    best_second = s2
            total = sum_first + best_second
            if total > max_total:
                max_total = total
        # second before first
        for i in range(0, n - firstLen - secondLen + 1):
            sum_second = window_sum(i, secondLen)
            best_first = 0
            for j in range(i + secondLen, n - firstLen + 1):
                s1 = window_sum(j, firstLen)
                if s1 > best_first:
                    best_first = s1
            total = sum_second + best_first
            if total > max_total:
                max_total = total
        return max_total

# Helper functions for testing
def list_to_linked(lst: list[int]) -> Optional[ListNode]:
    head = None
    tail = None
    for num in lst:
        node = ListNode(num)
        if not head:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head

def linked_to_list(node: Optional[ListNode]) -> list[int]:
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res