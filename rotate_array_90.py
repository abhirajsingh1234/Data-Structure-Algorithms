class Solution:
    def rotateMatrix(self, mat):
        # code here
        for i in range(len(mat)):
            mat[i] = mat[i][::-1]
        for i in range(len(mat)):
            for j in range(i,len(mat[0])):
                mat[i][j],mat[j][i] = mat[j][i], mat[i][j]
        return mat
obj = Solution()
print(obj.rotateMatrix([[0, 1, 2], 
                [3, 4, 5], 
                [6, 7, 8]]))
