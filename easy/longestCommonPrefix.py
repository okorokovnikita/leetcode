class Solution:
    def longestCommonPrefix(self, strs):
        prefix = ''
        if len(strs) == 0:
            return prefix
        else:
            for i in range(len(min(strs))):
                c = strs[0][i]
                if all(a[i] == c for a in strs):
                    prefix = prefix + c
                else:
                    break
        return prefix
