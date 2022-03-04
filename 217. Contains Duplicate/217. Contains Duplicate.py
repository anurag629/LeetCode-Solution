class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s_nums = set(nums)
        len_s = len(s_nums)
        len_l = len(nums)
        if len_s == len_l:
            return False
        else:
            return True
            