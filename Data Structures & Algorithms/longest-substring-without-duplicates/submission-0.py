class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, length = 0, 0
        seen = set()

        for R in range(len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1

            seen.add(s[R])
            length = max(length, R-L+1)

        return length
        