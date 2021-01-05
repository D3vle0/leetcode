class Solution:
    def reverse(self, x: int) -> int:
        if (x>=0):
            val = int(str(x)[::-1])
        else:
            val = -1*int(str(x)[::-1][:-1])
        return val if -2**31<=val<=2**31 else 0
        