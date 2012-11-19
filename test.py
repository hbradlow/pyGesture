def getVariance(nums):
    count = len(nums)
    ev = sum(nums) / count
    variance = sum(map(lambda x: (ev-x)**2, nums)) / count
    return variance

print getVariance([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])

