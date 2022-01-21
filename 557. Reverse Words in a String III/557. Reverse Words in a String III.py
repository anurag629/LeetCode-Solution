class Solution:
    def reverseWords(self, s: str) -> str:
        news = list(s.split(" "))
        ans = ""
        for i in range(len(news)):
            ans = ans + news[i][::-1]
            if i == len(news)-1:
                pass
            else:
                ans = ans + " "
        return ans