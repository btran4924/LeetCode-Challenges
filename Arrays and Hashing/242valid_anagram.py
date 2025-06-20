# Simple Approach, tally each letter in word, if both dicts match return true.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = dict()
        dictt = dict()
        for letter in s:
            dicts[letter] = dicts.get(letter, 0) + 1
        for letter in t:
            dictt[letter] = dictt.get(letter, 0) + 1
        return dicts == dictt