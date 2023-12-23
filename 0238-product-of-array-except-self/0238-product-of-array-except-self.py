class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        
        left_product = [1] * size
        
        left_accumulator = 1
        for i in range(1, size):
            left_accumulator *= nums[i - 1]
            left_product[i] = left_accumulator
        
        right_accumulator = 1
        for i in range(size - 1, -1, -1):
            left_product[i] *= right_accumulator
            right_accumulator *= nums[i]
        
        return left_product