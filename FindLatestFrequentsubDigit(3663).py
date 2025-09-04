class Solution(object):
    def getLeastFrequentDigit(self, n):
        nums = [int(d) for d in str(n)]
        nums.sort()
        if len(nums) == 0:
            return 0
        freq = []
        val = []
        for i in range(len(nums)):
            index = i 
            right = len(nums) - 1
            while right >= 0:
                if nums[index] == nums[right] and right != index:
                    count += 1
            val.append(count)
            if max(val) < count:
                val.append
        return min(freq)
            