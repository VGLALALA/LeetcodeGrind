class Solution(object):
    def productExceptSelf(self, nums):

        n = len(nums)

        # answer[i] first stores product of everything to the LEFT
        answer = [1] * n

        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        # Multiply by product of everything to the RIGHT
        right_product = 1

        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer

        