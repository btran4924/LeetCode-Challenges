## Traverse both lists:
##    Traverse until *, once hit, keep moving until match again, if not, then fail.
##    Every time ?, move onto next value.
## Return true when both list have been traversed completely (at the same time)
## Way to attack:
##     (Deprecated) Most likely will compare both lists to eachother, anytime no match (unless ?), False
##     New attempt: iterate until "*", s compare with p until match, then iterate again. If ?, just move on no comparison.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p1 = p2 = 0
        match = 0
        star = -1
        n, m = len(s), len(p)

        while p1 < n:
            if p2 < m and (p[p2] == s[p1] or p[p2] == '?'):
                p1 += 1
                p2 += 1
            ## Start of checking if its a match
            elif p2 < m and p[p2] == '*':
                star = p2
                match = p1
                p2 += 1
            elif star != -1:
                p2 = star + 1
                match += 1
                p1 = match
            else: 
                return False
        
        while p2 < m and p[p2] == '*':
            p2 += 1
        return p2 == m