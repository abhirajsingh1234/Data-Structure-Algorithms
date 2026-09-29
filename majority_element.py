##By Abhiraj 

# class Solution:
#     def majorityElement(self, arr):
#         #code here
#         return_val = -1
#         if len(arr) == 1:
#              return arr[0]
#         if len(arr)==0:
#              return -1
#         count = {}
#         for i in arr:
#                 if i in count.keys():
#                     count[i] = count[i] + 1
#                 else:
#                     count[i] = 1
#         print(count)
#         for k,v in count.items():
#              if v > len(arr)/2:
#                 return_val = k
#         return return_val

# obj = Solution()
# print(obj.majorityElement([1, 1, 2, 1, 3, 5, 1]))


##boyer moore voting algorithm

class Solution:
    def majorityElement(self, arr):
        
        candidate = None
        count = 0

        # Find a possible majority element
        for num in arr:
            print('candidate : ',candidate)
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        # Verify that candidate is actually a majority
        count = 0
        for num in arr:
            if num == candidate:
                count += 1

        if count > len(arr) // 2:
            return candidate

        return -1

obj = Solution()
print(obj.majorityElement([2, 1, 2, 1, 5, 1, 3]))