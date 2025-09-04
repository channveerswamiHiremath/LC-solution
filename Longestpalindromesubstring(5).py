class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        longest = ""

        for i in range(n):
            # ----- odd ----- #
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                current = s[left:right+1]
                if len(current) > len(longest):
                    longest = current
                left -= 1
                right += 1

            # ----- even ----- #
            left, right = i, i+1
            while left >= 0 and right < n and s[left] == s[right]:
                current = s[left:right+1]
                if len(current) > len(longest):
                    longest = current
                left -= 1
                right += 1

        return longest
