def sortedSquares(self, nums: List[int]) -> List[int]:
    newnums = []
    for i in nums:
        newnums.append(i*i)
    newnums.sort()
    return newnums