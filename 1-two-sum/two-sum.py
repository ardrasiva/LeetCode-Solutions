class Solution:
    def twoSum(self,nums,target):
    
        l=len(nums)
        anslist=[]
        for i in range(0,l):
            for j in range(i+1,l):
                if nums[i]+nums[j] == target:
                    anslist.append(i)
                    anslist.append(j)
        return anslist

