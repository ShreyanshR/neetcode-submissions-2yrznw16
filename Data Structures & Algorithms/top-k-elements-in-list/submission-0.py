class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        t = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            t[num] = 1 + t.get(num, 0)

        for num, count in t.items():
            freq[count].append(num)
        
        #the freq is a count by bucket sort, each index is a frequency

        res = []

        ## let's sort now, we have the dict
        for i in range(len(freq) - 1, 0, -1):
            # we start from the end of the list as the count is in increasing order
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

