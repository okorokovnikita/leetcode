class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n==1:
            return[0]
        result=[]
        for i in range(1,int(n/2)+1):
            result.append(i)
        for i in range(-1,-int(n/2)-1,-1):
            result.append(i)
        if n%2!=0:
            result.append(0)
        return result
