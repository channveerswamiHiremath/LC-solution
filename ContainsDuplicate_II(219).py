class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        last_seen = {}
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] in last_seen and i - last_seen[nums[i]] <= k:
                return True
            last_seen[nums[i]] = i
            i += 1

        return False
