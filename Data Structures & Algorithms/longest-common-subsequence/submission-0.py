class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        prev = [0] * (len(text2) + 1)
        curr = [0] * (len(text2) + 1)

        for i in range(len(text1)-1, -1,-1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    #move diagonally
                    curr[j] = 1 + prev[j+1]
                else:
                    #take max of right and down
                    right = curr[j+1]
                    down = prev[j]
                    curr[j] = max(right, down)

            prev, curr = curr, prev
        
        return prev[0]
        