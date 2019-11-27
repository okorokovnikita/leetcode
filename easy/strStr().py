class Solution:
    def strStr(self, haystack, needle):
        if haystack == needle:
            return 0
        else:
            l = len(needle)
            for i in range(len(haystack)):
                if haystack[i:i+l] == needle:
                    return i
                else:
                    i=i+1
        return -1