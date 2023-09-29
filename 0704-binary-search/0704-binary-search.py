class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bst(nums: List[int], target: int, prevLen: int) -> int:
            mid = len(nums) // 2

            if (target == nums[mid]):
                return prevLen + mid
            if (len(nums) == 1):
                return -1

            if (target < nums[mid]):
                return bst(nums[0:mid], target, prevLen)
            else:
                return bst(nums[mid:], target, prevLen + mid)
        
        return bst(nums, target, 0)