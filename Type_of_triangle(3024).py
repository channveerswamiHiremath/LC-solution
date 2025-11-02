class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums.sort()

        if nums[0] + nums[1] <= nums[2]:
            return "none"

        if nums[0] == nums[1] == nums[2]:
            return "equilateral"

        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return "isosceles"

        a = nums[0] + nums[1] 
        b = nums[0] + nums[2]
        c = nums[1] + nums[2] 

        if a > nums[2] and b > nums[1] and c > nums[0]:
            return "scalene"
        