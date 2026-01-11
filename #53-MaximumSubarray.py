class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = nums[0]
        maxsum = nums[0]

        for i in nums[1:]:
            curr = max(i,curr+i)
            maxsum = max(maxsum,curr)

        return maxsum
