class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        counter=0
        l=[]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                l.append(matrix[i][j])
        return sorted(l)[k-1]
