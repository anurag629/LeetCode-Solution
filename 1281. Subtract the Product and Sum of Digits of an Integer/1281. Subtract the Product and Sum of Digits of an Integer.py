class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ = 0
        pro = 1
        for i in str(n):
            summ = summ + int(i)
            pro = pro * int(i)
            
        return (pro - summ)