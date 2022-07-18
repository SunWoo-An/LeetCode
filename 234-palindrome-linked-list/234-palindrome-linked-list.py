# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        str = list()
        curr = head
        while True:
            if curr == None:
                break
            str.append(curr.val)
            curr = curr.next
        if str[::-1] == str:
            return True
        else:
            return False