class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 1:
            median = float(nums[len(nums)//2])
            return median
        else :
            left = nums[len(nums) // 2 - 1]
            right = nums[len(nums) // 2]
            return (left + right) / 2.0
            