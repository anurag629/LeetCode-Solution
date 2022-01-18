class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p = 0
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if ((nums[i] + nums[j] == target) and i != j):
                    ans = [i, j]
                    p = 1
                    break
            if p == 1:
                break
        return ans
