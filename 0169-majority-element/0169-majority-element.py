class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        c = Counter(nums)
        n = len(nums)
        for key,val in c.items():
            if val > n//2:
                return key
        
        