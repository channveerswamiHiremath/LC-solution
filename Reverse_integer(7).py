class Solution(object):
    def reverse(self, x):
        if x < 0:
            n = -x       
            re = 0
            while n > 0:
                d = n % 10
                re = re * 10 + d
                n //= 10   
            re = -re   
        else: 
            n = x
            re = 0
            while n > 0:
                d = n % 10
                re = re * 10 + d
                n //= 10
        
        if re < -2**31 or re > 2**31 - 1:
            return 0
        return re
        