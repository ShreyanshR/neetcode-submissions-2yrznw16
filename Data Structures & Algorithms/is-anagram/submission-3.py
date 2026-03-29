class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        for ch in s:
            count_s[ch] = count_s.get(ch,0) + 1
        for ch in t:
            if ch not in count_s:
                return False
            count_s[ch] -= 1

            if count_s[ch] < 0:
                return False
        
        return True
        


      
            
        