class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)

        firstsum = nums[0]+nums[1]+nums[2]

        for i in range(length-2):
            left = i+1
            right = length-1
            while left<right:
                newsum = nums[i] + nums[left] + nums[right]
                if abs(newsum - target) < abs(firstsum - target):
                
                    firstsum = newsum  
                
                if newsum < target:
                    left = left + 1
                elif newsum > target:
                    right = right - 1
                else:
                    return newsum
        return firstsum
            
