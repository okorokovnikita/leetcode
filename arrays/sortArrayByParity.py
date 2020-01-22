class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even=[]
        not_even=[]
        for el in A:
            if el%2==0:
                even.append(el)
            else:
                not_even.append(el)
        return even+not_even
