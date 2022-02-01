class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 2:
            return False
        dict = {}
        for i in nums:
            if i in dict:
                return True
            else:
                dict[i] = 1
        return False