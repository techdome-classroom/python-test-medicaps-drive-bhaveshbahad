class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isValid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            return False
    
    return not stack
    
        pass
    



  

