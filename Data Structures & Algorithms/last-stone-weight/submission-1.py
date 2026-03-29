class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        print(f'initial: {stones}')

        #iterate till we have only 1 or 0 element
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            #the elements are already popped, we will only push into the heap only if
            print(f'first: {first}')
            print(f'second: {second}')
            if abs(first) > abs(second):
                heapq.heappush(stones, first - second)
            print(f'after smashing: {stones}')
        
        #if there is no element the just return 0
        stones.append(0)
        return abs(stones[0])


        