class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = 0
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)

        return s == t
