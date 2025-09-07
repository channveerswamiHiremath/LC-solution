class Solution(object):
    def removeDuplicates(self, nums):

        for i in range(len(nums) - 1, 1, -1):
            if nums[i] == nums[i - 2]:
                nums[i] = -2**31   

        count = 0
        for i in range(len(nums)):
            if nums[i] != -2**31:
                nums[count] = nums[i]
                count += 1

        while len(nums) > count:
            nums.pop()
