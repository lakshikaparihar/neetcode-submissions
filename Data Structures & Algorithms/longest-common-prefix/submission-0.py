class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for group in zip(*strs):
            if len(set(group)) == 1:
                res += group[0]
            else:
                break

        return res