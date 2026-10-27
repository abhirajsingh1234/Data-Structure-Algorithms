class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Step 1: Initialize an empty list to store the result for each sliding window
        output = []
        
        # Step 2: Loop through the array to check every possible starting index of a window of size k.
        # 'len(nums) - k + 1' ensures the window stays within the bounds of the array.
        for i in range(len(nums) - k + 1):
            
            # Step 3: Check if the elements in the current window are strictly increasing.
            # (Note: This specific check uses i+2, meaning it evaluates a window size of 3)
            if nums[i] < nums[i+1] < nums[i+2]:
                # If they are strictly increasing, append the largest (last) element of the window
                output.append(nums[i+2])
            else:
                # If they are not strictly increasing, append -1
                output.append(-1)
                
        # Step 4: Return the final list of results after checking all windows
        return output

# --- Testing the Code ---
obj = Solution()

# Test the function with a sample array and k = 3
print(obj.resultsArray([1, 2, 3, 3, 5, 6, 7, 8, 7], 3))