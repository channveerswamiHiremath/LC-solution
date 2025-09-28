from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        left = 0
        tar = Counter(t)
        found = []
        res = ""

        for right in range(len(s)):
            if s[right] in tar:
                tar[s[right]] -= 1

            while all(v <= 0 for v in tar.values()):
                found.append(right - left + 1)

                if not res or (right - left + 1) < len(res):
                    res = s[left:right+1]

                if s[left] in tar:
                    tar[s[left]] += 1
                left += 1

        return res
