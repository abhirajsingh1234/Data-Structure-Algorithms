class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        sum = arr[0]
        max = arr[0]
        subarray =[arr[0]] if arr[0]>0 else []
        for i in range(1,len(arr)):
            sum+=arr[i]
            subarray.append(arr[i])
            if sum>max:
                max = sum
            if  sum<0:
                subarray = []
                sum=0
        return max,subarray

obj = Solution()
print(obj.maxSubarraySum([2, 3, -8, 7, -1, 2, 3]))