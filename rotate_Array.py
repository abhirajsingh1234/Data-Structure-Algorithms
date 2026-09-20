class Solution:
    def rotateArr(self, arr, d):
        # code here
        d = d% len(arr)
        print(d)
        first_d_elements,remaining_elements = arr[0:d],arr[d:]
        arr[:]= remaining_elements + first_d_elements
        return arr


obj = Solution()
print(obj.rotateArr([10, 4, 1], 2))