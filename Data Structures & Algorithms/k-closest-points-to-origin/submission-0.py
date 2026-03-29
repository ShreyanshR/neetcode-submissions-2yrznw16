class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for i, point in enumerate(points):
            
            dt = 0
            x, y = point
            dt = (x**2 + y**2)**0.5
            minHeap.append([dt,x,y])

        print(minHeap)

        heapq.heapify(minHeap)
        res = []

        while k > 0:
            dt, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k-=1

        return res

