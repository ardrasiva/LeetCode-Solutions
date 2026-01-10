class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merge = sorted(nums1 + nums2)
        length = len(merge)
        
        if length % 2 != 0:
            median = float(merge[length//2]) 
            return median
        else:
            mid1 = length // 2
            mid2 = mid1 - 1
            median = float((merge[mid1]+merge[mid2]) / 2.0) #if 2 is put then it will not .5 in its op
            return median
