class Solution:
    def isValid(self, s: str) -> bool:

        ans = []

        valid = {')' : '(', '}':'{', ']' : '['}

        for char in s:
            if char in valid:
                if ans and ans[-1] == valid[char]:
                    ans.pop()
                else:
                    return False
            else:
                ans.append(char)

        return True if not ans else False
        