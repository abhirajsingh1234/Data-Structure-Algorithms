class Solution:
    def getSubArrays(self, arr):
        #code here
        output = []
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                print(f"arr[{i}:{j+1}] = {arr[i:j+1]}")
                output.append(arr[i:j+1])
        return output
    
obj = Solution()
print(obj.getSubArrays([1, 2, 3]))