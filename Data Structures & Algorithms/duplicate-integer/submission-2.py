class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        is_duplicate = set(nums)

        return True if len(is_duplicate) != len(nums) else False 
        