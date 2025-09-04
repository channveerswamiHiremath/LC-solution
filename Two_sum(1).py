class Solution(object):
    def twoSum(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            s = nums[left] + nums[right]
            if s == target:
                return left, right
            right -= 1

            if right <= left:
                left += 1
                right = len(nums) - 1
        