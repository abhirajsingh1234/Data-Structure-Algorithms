#time compleixty - O(n^3), Space complexity - O(1)

class Solution:
    def subarraySum(self, arr):
        # code here 
        summation = 0
        for i in range (len(arr)):
            for j in range(i,len(arr)):
                summation+=sum(arr[i:j+1])
        return summation

obj = Solution()
print(obj.subarraySum([1, 2, 3]))

#time compleixty - O(n^2), Space complexity - O(1)
class Solution:
    def subarraySum(self, arr):
        # code here 
        summation = 0
        for i in range (len(arr)):
            current = 0
            for j in range(i,len(arr)):
                current+= arr[j]
                summation+=current
            
        return summation

obj = Solution()
print(obj.subarraySum([1, 2, 3]))

#time compleixty - O(n), Space complexity - O(1)

class Solution:
    def subarraySum(self, arr):
        # code here 
        total = 0
        for i in range(len(arr)):
            total+=arr[i]*(i+1)*(len(arr)-i)
        return total

obj = Solution()
print(obj.subarraySum([1, 2, 3]))