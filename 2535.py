class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        el_sum = sum(nums)
        total = 0
        for val in nums:
            if val > 9:
                num = func(val)
                total += num
            else :
                total += val
        return abs(el_sum - total)

def func(val):
    temp = val
    summ = 0
    while temp > 0:
        num = temp % 10
        summ += num
        temp = temp // 10
    return summ 
    