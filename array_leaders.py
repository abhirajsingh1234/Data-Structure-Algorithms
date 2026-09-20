class Solution:
    def leaders(self, arr):
        array_leaders = []
        largest_number = arr[len(arr)-1]
        print(largest_number)
        array_leaders.append(largest_number)

        print(array_leaders)
        
        for i in range(len(arr)-2, -1,-1):
            if arr[i]>=largest_number:
                array_leaders.append(arr[i])
                
                largest_number = arr[i]

        print(array_leaders)            
        return array_leaders[::-1]

obj = Solution()
print(obj.leaders([10, 4, 2, 4, 1]))