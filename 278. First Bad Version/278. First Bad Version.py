# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> int:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        r = n
        l = 0    
        while l < r:
            mid = (l + r) // 2
            if isBadVersion(mid) == False:
               l = mid + 1
            else: 
               r = mid
        return l
                