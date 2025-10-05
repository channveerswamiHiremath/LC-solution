class Solution(object):
    def plusOne(self, digits):
        total = 0
        for i in range(len(digits)):
            total = total * 10 + digits[i]
        temp = total + 1
        re = 0
        listf = []
        while temp > 0:
            d = temp % 10
            listf.append(d)
            temp //= 10
        return listf[::-1]
