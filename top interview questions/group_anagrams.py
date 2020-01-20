class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
        for s in strs:
            x=''.join(sorted(s))
            if x in ans:
                ans[x].append(s)
            else:
                ans[x]=[s]
        return [ ans[x] for x in ans ]
