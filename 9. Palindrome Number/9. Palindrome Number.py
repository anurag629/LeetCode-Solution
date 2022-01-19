class Solution:
    def isPalindrome(self, x: int) -> bool:
        new = str(x)[::-1]
        if str(x) == new:
            return True
        else:
            return False
