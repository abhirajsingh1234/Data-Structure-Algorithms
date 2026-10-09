class Solution:
    def countIncreasing(self, arr):
        # code here
        start = 0
        end = 0
        sum = 0
        for i in range(0,len(arr)):
            # print(i)
            if i == len(arr)-1 or arr[i]>=arr[i+1]:
                end= i
                # print(start ,end)
                # print(f"({(end-start)}*{((end-start)+1)})/2")
                sum+=((end-start)*((end-start)+1))/2
                start = i+1
            
        return int(sum)
obj = Solution()
print(obj.countIncreasing([1,2,1,4,5,6]))


#first we split the array if there is any condition where i>=i+1  so we get multiple increasing subarray

# eg - [1,2,1,4,5,6] will become [1,2] and [1,4,5,6]

#now second we need to find all subarrays for splitted arrays
# formula for finding subarrays for an array is n(n+1)/2 
# for subarray [1,2] 2(2+1)/2 = 3 [ [1], [2], [1,2]] so its 2 but we need to find only subarrays that are having len >1 as we  single element subarray will not have incremental behaviour for that we need 2 elements 
# so now what we can do... count of single element subarrays will always be equal to len of array len([1,2]) = COUNT([1][2]) 
# we can create a formula for like n(n+1)/2 - n)[!!len(arr) = n!!] so using this formula we can get the answer correct .
# but in this code we have done something else .. if we notice ... n(n+1)/2 - n = (n-1)((n-1)+1) ..[!!len(arr) = n!!]
#Conclusion is ..after splitting our main array with the i>=i+1 logic all we need is now to count how much is count of subarrays in each splitteed subarray where subarray length is more than 2

# Solution :- split array on basis (i>=i+1 )
#             for each subarray get subarray count using - (n-1)((n-1)+1)/2
#             sum up each splitted array count and that is the answer