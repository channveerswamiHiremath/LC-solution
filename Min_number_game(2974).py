class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        alice = []
        bob = []
        arr = []
        i = 0
        j = 1
        while j < len(nums):
            alice.append(nums[i])
            bob.append(nums[j])
            j += 2
            i += 2 
        i = 0
        while i < len(alice):
            arr.append(bob[i])
            arr.append(alice[i])
            i += 1
        return arr