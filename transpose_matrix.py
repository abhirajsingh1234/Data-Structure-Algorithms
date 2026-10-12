class Solution:
    def transpose(self, mat):
        # code here
        for i in range(len(mat[0])):
            for j in range(i, len(mat[0])):
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
        return mat