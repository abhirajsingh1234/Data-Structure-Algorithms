# time complexity = O(N^2), space complexity = O(1)

class Solution:
    def maxCircularSum(self, arr):
       max_output = None
       length = len(arr)
       for i in range(length):
           current_sum = 0
           for j in range(length):
               if j+i<=length-1:
                   j = i+j
               else:
                   j = j+i-(length-1)-1
               current_sum+=arr[j]
               if max_output is not None:
                max_output = max(max_output,current_sum)
               else:
                  max_output = current_sum
       return max_output
        

obj = Solution()
print(obj.maxCircularSum([8, -8, 9, -9, 10, -11, 12]))