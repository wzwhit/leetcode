# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        if exponent < 0:
            exp = -exponent
        else: exp = exponent
        if exp % 2 == 1:
            return base * (self.Power(base, exp>>1) ** 2) if exponent > 0 else 1 / (base * (self.Power(base, exp>>1) ** 2))
        else:
            return (self.Power(base, exp>>1) ** 2) if exponent > 0 else 1 / ((self.Power(base, exp>>1) ** 2))

print(Solution().Power(1.2221, -4))