## Greedy Approach, iterate through list, if value greater than prev, reload with new value.
## Returns true when ite gets to the last position in the list.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0
        for num in nums:
            if curr < 0:
                return False
            elif num > curr:
                curr = num
            curr -= 1
        return True
