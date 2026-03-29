class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isDuplicate = {}

        for num in nums:
            if num not in isDuplicate:
                isDuplicate[num] = 1
            else:
                return True
        return False
        
        