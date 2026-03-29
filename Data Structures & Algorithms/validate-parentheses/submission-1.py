class Solution:
    def isValid(self, s: str) -> bool:
        #this is a hashmap, so we have key value pairs
        #this is to see if the last values are closed brackets or not
        closeToOpen = { ")" : "(", "]":"[", "}":"{"}
        stack = []

        for char in s:
            "The first char is from top i.e. it should be an open one ("
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(char)

        return True if not stack else False