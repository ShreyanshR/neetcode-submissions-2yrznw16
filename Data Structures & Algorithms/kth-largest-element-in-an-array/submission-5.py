class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-s for s in nums]
        heapq.heapify(maxHeap)
        print(maxHeap)

        while k > 1:
            heapq.heappop(maxHeap)
            k-=1
        print(maxHeap)

        #maxHeap = [-s for s in maxHeap]

        return -maxHeap[0]
        