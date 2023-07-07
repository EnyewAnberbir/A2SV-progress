class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            is_negative = True
            x = abs(x)
        revers = int(str(x)[::-1])
        
        if is_negative:
            revers = -revers
        if revers < -2**31 or revers > 2**31 - 1:
            return 0
        
        return revers
