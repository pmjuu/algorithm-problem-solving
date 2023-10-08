class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return nums[0]

        current_max = nums[0]
        total_max = nums[0]
        
        for num in nums[1:]:
            current_max = max(num, current_max + num)
            total_max = max(total_max, current_max)
        
        return total_max