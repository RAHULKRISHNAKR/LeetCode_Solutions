'''Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.'''

class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        mid = n//2
        sumn=0
        for i in range(n):
            sumn += (mat[i][i] + mat[n-i-1][i])
        if n%2==1:
            sumn-=mat[mid][mid]
        return sumn
        
