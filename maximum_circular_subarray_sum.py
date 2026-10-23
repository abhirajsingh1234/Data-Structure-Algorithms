## time complexity = O(N^2), space complexity = O(1)

# class Solution:
#     def maxCircularSum(self, arr):
#        max_output = None
#        length = len(arr)
#        for i in range(length):
#            current_sum = 0
#            for j in range(length):
#                if j+i<=length-1:
#                    j = i+j
#                else:
#                    j = j+i-(length-1)-1
#                current_sum+=arr[j]
#                if max_output is not None:
#                 max_output = max(max_output,current_sum)
#                else:
#                   max_output = current_sum
#        return max_output
        

# obj = Solution()
# print(obj.maxCircularSum([8, -8, 9, -9, 10, -11, 12]))


## time complexity = O(N), space complexity = O(1)

class Solution:
    def maxCircularSum(self, arr):
        if not arr:
            return 0
        positive_sum = 0
        maximum_sum = float("-inf")
        negative_sum = 0
        minimum_sum = float("inf")
        sum = 0
        for i in arr:
            positive_sum = max(i,i+positive_sum)
            maximum_sum = max(maximum_sum, positive_sum)

            negative_sum = min(i,i+negative_sum)
            minimum_sum = min(minimum_sum,negative_sum)

            sum+=i
        if maximum_sum<0:
            return maximum_sum
        
        curcular_max = sum - minimum_sum
        return  max(maximum_sum,curcular_max)
obj = Solution()
print(obj.maxCircularSum([1,-10,4,5]))
