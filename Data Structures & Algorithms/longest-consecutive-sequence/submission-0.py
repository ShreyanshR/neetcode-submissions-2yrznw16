class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            #check if it's start of a sequence
            #and we do it by checking if n - 1 exists

            if n - 1 not in numSet:
                length = 0

                #now we check if the next element is in the set
                #we can do it by adding n + lenght: it means next element is just a
                # difference of 1

                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest
        