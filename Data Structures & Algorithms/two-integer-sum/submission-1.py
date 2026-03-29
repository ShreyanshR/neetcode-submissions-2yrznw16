class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevList = {}

        for i, n in enumerate(nums):
            diff = target - n #the difference b/w the target and the 
            # number, so we have to look if the number existes in teh preveMap

            if diff in prevList:
                return [prevList[diff], i]
            prevList[n] = i

        return  

        