class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = { ")" : "(", "]" : "[", "}" : "{" }
        stack = deque()

        for p in s:
            if p not in hashmap:
                stack.append(p)
            elif stack and hashmap[p] == stack[-1]:
                stack.pop()
            else:
                return False

        return True if not stack else False