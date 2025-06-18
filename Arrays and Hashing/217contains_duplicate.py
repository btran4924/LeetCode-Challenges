# Simple solution: Use Hashmap to store key, if num exists in list of keys, then return True.
# Otherwise, add num to keys and keep going.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exists = dict()
        for num in nums:
            if num in exists.keys():
                return True
            else:
                exists[num] = "exists"
        return False