class Solution:
    def isValid(self, s: str) -> bool:
        maps = {']':'[','}':'{',')':'('}
        stack = []
        for c in s:
            #char is end bracket
            if c in maps:
                if not stack or stack[-1] != maps[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return not stack


        