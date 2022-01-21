class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p = s[::-1]
        for i in range(len(p)):
            s[i] = p[i]
            
           