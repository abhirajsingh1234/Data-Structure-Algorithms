import math
import datetime

class Solution:
    def Reversal(self, arr: list) -> None:
        start_time = datetime.datetime.now()
        length = math.ceil(len(arr)/2) if len(arr) % 2 == 0 else len(arr)//2
        for i in range(length):
            arr[i],arr[len(arr)-1-i] = arr[len(arr)-1-i],arr[i]
        end_time = datetime.datetime.now()
        print(arr)
        print(f"Execution time: {end_time - start_time}")
obj = Solution()
obj.Reversal([1,2,3,4,5,6])


import math
class Solution:
    def reverse(self, arr: list) -> None:
        start_time = datetime.datetime.now()
        arr.reverse()
        print(arr)
        
        end_time = datetime.datetime.now()
        print(f"Execution time: {end_time - start_time}")

obj = Solution()
obj.reverse([1,2,3,4,5,6])