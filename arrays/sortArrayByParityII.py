class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        ans=[0]*len(A)
        m=0
        n=1
        for i in range(len(A)):
            if A[i]%2 ==0:
                ans[m]=A[i]
                m=m+2
            else:
                ans[n]=A[i]
                n=n+2
        return ans
