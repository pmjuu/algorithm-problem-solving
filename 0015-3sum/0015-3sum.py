class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            target = -nums[i]
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                curr_sum = nums[left] + nums[right]
                
                if curr_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # 중복된 두 번째 숫자 건너뛰기
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # 중복된 세 번째 숫자 건너뛰기
                    
                    left += 1
                    right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return result