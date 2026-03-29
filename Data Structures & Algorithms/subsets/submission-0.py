class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curSet, subSet = [], []
        self.helper(0, nums, curSet, subSet)
        return subSet
    
    def helper(self, i, nums, curSet, subSet):
        if i >= len(nums):
            subSet.append(curSet.copy())
            return

        curSet.append(nums[i])
        #include teh element in the path
        self.helper(i + 1, nums, curSet, subSet)

        curSet.pop()

        #we popped, so we will not include the elements
        self.helper(i + 1, nums, curSet, subSet)

        return subSet

        