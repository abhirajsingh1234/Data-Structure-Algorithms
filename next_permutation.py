class Solution:
    def nextPermutation(self, arr):
        to_be_swapped = None
        arr_length = len(arr)

        for i in range(arr_length-1,0,-1):
            if arr[i]>arr[i-1]:
                to_be_swapped = i-1
                break
        if to_be_swapped is None:
            arr[:] = arr[::-1]
            return arr
        for i in range(arr_length-1,to_be_swapped,-1):
            if arr[i]>arr[to_be_swapped]:
                arr[i],arr[to_be_swapped] = arr[to_be_swapped], arr[i]
                break
        arr[to_be_swapped+1:] = arr[to_be_swapped+1:][::-1]

        return arr
        
obj = Solution()
print(obj.nextPermutation([1, 2, 3, 6, 5, 4]))