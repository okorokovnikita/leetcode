class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result=[]
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j]==arr2[i]:
                    result.append(arr1[j])
        for el in sorted(arr1):
            if el not in arr2:
                result.append(el)
        return result
