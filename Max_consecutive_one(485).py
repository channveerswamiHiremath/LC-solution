class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_one = 0
        count = 0
        if len(nums) == 1:
            if nums[0] == 1:
                return 1
            else:
                return 0
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                count += 1
                max_one = max(max_one, count)
            if nums[i] == 0:
                count = 0
            i += 1
        return max_one
        