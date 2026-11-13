class Solution:
    def canPairs(self, arr, k):
        # If the array length is odd, it's impossible to pair up all elements
        if len(arr) % 2 != 0:
            return False
            
        remainder_count = {}
         
        # Count the frequency of each remainder
        for num in arr:
            rem = num % k
            remainder_count[rem] = remainder_count.get(rem, 0) + 1
            
        for rem in remainder_count:
            # 1. Remainder 0 must have an even count
            if rem == 0:
                if remainder_count[rem] % 2 != 0:
                    return False
            # 2. If remainder is exactly half of k (e.g., k=4, rem=2), its count must be even
            elif 2 * rem == k:
                if remainder_count[rem] % 2 != 0:
                    return False
            # 3. For any other remainder, count(rem) must equal count(k - rem)
            else:
                complement = k - rem
                if remainder_count.get(rem, 0) != remainder_count.get(complement, 0):
                    return False
                    
        return True

obj = Solution()
print(obj.canPairs([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10))  # Output: True
