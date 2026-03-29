class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum = 0
        L , count = 0 , 0

        for R in range(len(arr)):
            print(L,R)
            if R - L + 1 > k:
                window_sum -= arr[L]
                L += 1

            window_sum += arr[R]

            if R - L + 1 == k:
                avg = window_sum/k
                #print(avg)
                if avg >= threshold:
                    print("greater than thres")
                    count += 1

        print(count)

        return count