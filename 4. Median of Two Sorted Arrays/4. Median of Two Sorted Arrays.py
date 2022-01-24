#Approach 1
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        listt = nums1 + nums2
        listt.sort()
        n = len(listt)
        if n%2 == 0:
            return (listt[(n//2)] + listt[((n//2) - 1)])/2
        else:
            return listt[n//2]


# Approach 2
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return median(nums1 + nums2)
        