class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        m=n/2
        d={}
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]=d[nums[i]]+1
        for el in d:
            if d[el]>m:
                return el
