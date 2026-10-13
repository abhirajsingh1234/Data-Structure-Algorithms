class Solution:
    def setMatrixZeroes(self, mat):
        # code here
        row_ind = []
        column_ind = []
        for i in range(len(mat)):
            for  j in range(len(mat[0])):
                if mat[i][j] ==0:
                    row_ind.append(i)
                    column_ind.append(j)
        for i in row_ind:
            for j in range(len(mat[0])):
                mat[i][j] = 0
        
        for i in column_ind:
            for j in range(len(mat)):
                mat[j][i] = 0
        return mat

obj = Solution()
print(obj.setMatrixZeroes([[1, -1, 1], [-1, 0, 1], [1, -1, 1]]))