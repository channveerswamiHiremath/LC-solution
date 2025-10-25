class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        single = 0
        double = 0

        if len(nums) == 0:
            return 
            
        for val in nums:
            if val // 10 == 0:
                single += val
            else :
                double += val
            
        if single > double :
            return True
        else:
            if (double - single) >= 1:
                return True
            else:
                return False  
