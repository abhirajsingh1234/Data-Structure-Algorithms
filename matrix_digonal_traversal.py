class Solution:
    def diagView(self, mat): 
        # code here 
        loop = len(mat[0])+len(mat)
        curr_row = 0
        curr_col = 0
        output = []
        for i in range (loop):
            using_row = curr_row
            using_col = curr_col
            while using_col>=curr_row:
                # print(f'row : {using_row}, column {using_col}')
                output.append(mat[using_row][using_col])
                using_col-=1
                using_row+=1
            if curr_col<len(mat[0])-1:
                # print(f"{curr_col}<{len(mat[0])}")
                curr_col+=1
            else:
                curr_row+=1
        return output

obj = Solution()
obj.diagView([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])        
