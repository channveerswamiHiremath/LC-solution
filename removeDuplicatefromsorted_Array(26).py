class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        
        count = 1
        val = nums[0]
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                val = nums[count]
                count += 1            

        return count
