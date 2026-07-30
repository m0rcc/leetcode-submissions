class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = collections.Counter(s)
        second = collections.Counter(t)

        return first.items() == second.items()