class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curr = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return curr
            curr += strs[0][i]
        return curr
