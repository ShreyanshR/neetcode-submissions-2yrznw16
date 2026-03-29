class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for sen in strs:
            key = "".join(sorted(sen))
            res[key] = [sen] + res.get(key, [])

        return list(res.values())