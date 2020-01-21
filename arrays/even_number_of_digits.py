class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter=0
        for el in nums:
            if len(str(el))%2==0:
                counter=counter+1
        return counter
