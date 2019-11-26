class Solution:
    def isValid(self, s):
        map = {'(': ')', '[': ']', '{': '}'}
        open = set(['(', '[', '{'])
        stack=[]
        for el in s:
            if el in open:
                stack.append(el)
            elif stack and el == map[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []