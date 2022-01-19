class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p = 0
        ans = -1
        for i in range(len(nums)):
            if nums[i] == target:
                ans  = i
                p = 1
                break
        return ans        
            