class Solution:

    def maxSubarraySum(self, arr):

        # Start with the first element as the current sum
        # and also assume it is the maximum sum initially
        sum = arr[0]
        max = arr[0]

        # Store elements of the current subarray
        # If the first element is positive, start the subarray with it
        subarray = [arr[0]] if arr[0] > 0 else []

        for i in range(1, len(arr)):

            # Add the current element to the current subarray sum
            sum += arr[i]

            # Add the current element to our current subarray
            subarray.append(arr[i])

            # If the current subarray has a greater sum,
            # update the maximum sum
            if sum > max:
                max = sum

            # Kadane's Algorithm:
            # If the current sum becomes negative,
            # there is no benefit in carrying this subarray forward.
            # So, discard the current subarray and start fresh
            # from the next element.
            if sum < 0:
                subarray = []
                sum = 0

        return max, subarray


obj = Solution()

print(obj.maxSubarraySum([2, 3, -8, 7, -1, 2, 3]))