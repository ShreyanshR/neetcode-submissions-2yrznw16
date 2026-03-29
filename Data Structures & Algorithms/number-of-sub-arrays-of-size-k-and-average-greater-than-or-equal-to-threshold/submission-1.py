class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        windowSum = 0
        L,count = 0,0

        for R in range(len(arr)):
            if R - L + 1 > k:
                windowSum -= arr[L]
                L += 1
            
            windowSum += arr[R]

            if R - L + 1 == k:
                avg = windowSum/k
                if avg >= threshold:
                    count += 1

        return count
