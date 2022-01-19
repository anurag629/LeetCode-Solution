class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        l = len(nums)
        if nums[l - 1] < target:
            return l
        elif nums[0] > target:
            return 0
        else:
            s = 0
            e = l
            while True:
                m = int((e + s) / 2)
                if nums[m] == target:
                    return m
                elif e-s == 1 and nums[s] < target and nums[e] > target:
                    return e
                elif nums[m] < target:
                    s = m
                else:
                    e = m
                