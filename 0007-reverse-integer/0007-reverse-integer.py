class Solution:
    def reverse(self, x: int) -> int:
        sx = str(abs(x))
        rsx = sx[::-1]
        if x > 0:
            x = int(rsx)
        else:
            x = -int(rsx)
        if x > 2 ** 31 - 1 or x < -2 ** 31:
            return 0
        return x