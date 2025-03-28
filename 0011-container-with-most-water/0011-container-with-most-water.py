class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxv = 0
        lp, rp = 0, len(height) - 1
        while lp < rp:
            cv = (rp - lp) * min(height[lp], height[rp])
            maxv = max(cv, maxv)
            if height[lp] < height[rp]:
                lp += 1
            else:
                rp -= 1
        return maxv
