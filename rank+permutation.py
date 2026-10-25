from math import factorial   # factorial(k) = k * (k-1) * ... * 1


class Solution:
    def findRank(self, s):
        # GOAL: find the rank of s among all its permutations in dictionary order.
        # IDEA: don't generate permutations. COUNT how many come before s, then add 1.

        # STEP 0: convert letters to ASCII numbers.
        # Reason: numbers can be compared with "<", and a smaller number
        # means the letter comes earlier in the dictionary (a=97, b=98, ...).
        s = [ord(i) for i in s]
        n = len(s)

        # Letters already placed at earlier indices (0 .. i-1).
        # Reason: a placed letter is not available at the current index,
        # so it must not be counted as a "smaller choice".
        done_smaller = []

        # Running count of permutations that come before s.
        # (Note: `sum` shadows Python's built-in sum(); fine here, but
        # `total` would be a safer name.)
        sum = 0

        for i, v in enumerate(s):
            # i = current index, v = the letter at this index
            print(f"using element {v} at index {i}")

            # STEP 1: count how many blocks come before my block.
            # A letter makes a block before mine if it is
            #   (a) smaller than v, so its strings come earlier in the dictionary, and
            #   (b) not in done_smaller, so it is still available at this index.
            # Each such letter could have been put here instead of v.
            smaller_elements = [
                element for element in s
                if element < v and element not in done_smaller
            ]
            print(f"smaller elements are {smaller_elements}")

            # STEP 2: mark the current letter v as used.
            # Reason: from the next index onward, v is already placed.
            # Only PLACING a letter uses it up. Being counted as "smaller"
            # does not use it up, it can be counted again at later indices.
            done_smaller.append(v)

            # STEP 3: find the block size.
            # After fixing the letter at index i, (n - 1 - i) letters remain.
            # They can be arranged in (n - 1 - i)! ways, so every block
            # (all strings that start with the same prefix) has that many strings.
            # We use the FACTORIAL because the remaining letters can be
            # shuffled in every order, not just chosen one by one.
            block_size = factorial(n - 1 - i)
            print(f"smaller count is {len(smaller_elements)} and block size is {block_size}")

            # STEP 4: strings skipped at this index
            #   = (blocks before mine) x (strings in each block)
            sum += len(smaller_elements) * block_size
            print(f"sum is {sum}")

        # STEP 5: sum = number of permutations BEFORE s.
        # Rank starts from 1, so add 1 to count s itself.
        return sum + 1


obj = Solution()
print(obj.findRank('cadb'))   # 14
print(obj.findRank('dcba'))   # 24