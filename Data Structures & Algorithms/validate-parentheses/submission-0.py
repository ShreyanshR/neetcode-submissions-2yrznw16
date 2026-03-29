class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}
        
        "()[]"
        for paran in s:
            if paran in closeToOpen:
                #this loop will only work when there is a close parenthesis as it's the key
                if stack and stack[-1] == closeToOpen[paran]:
                    #we will check if ther is a close parenthesis ans pop out the parenthesis
                    stack.pop()
                else:
                    #if there is no close parenthesis we will return False
                    return False
            else:
                #Will append the open parenthesis in the stack
                stack.append(paran)
                
            #only return true if it's empty
        return True if not stack else False