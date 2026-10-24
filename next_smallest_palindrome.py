def next_palindrome(a):
    n = len(a)

    # Overflow case: if every digit is 9 (e.g. [9,9,9]), the next palindrome
    # is one digit longer: 1, then n-1 zeros, then 1 (e.g. [1,0,1]).
    # Handling this up front means the carry below can never fall off the left edge.
    if all(d == 9 for d in a):
        return [1] + [0] * (n - 1) + [1]

    # Work on a copy so the caller's array is not modified.
    a = a[:]

    # Starting positions for the comparison, moving outward from the middle.
    # i is the last element of the left half.
    # j is the first element of the right half:
    #   even length -> no center, so j = n//2 (right next to i)
    #   odd length  -> skip the center, so j = n//2 + 1
    i = n // 2 - 1
    j = n // 2 if n % 2 == 0 else n // 2 + 1

    # Walk outward while mirrored pairs are equal.
    # We stop at the first pair that differs, because that pair alone
    # decides whether the mirrored left half is bigger or smaller than the right.
    while i >= 0 and a[i] == a[j]:
        i -= 1
        j += 1

    # Decide whether the left half needs +1:
    #   i < 0         -> all pairs matched, already a palindrome, but we need
    #                    a strictly greater one, so we must add 1.
    #   a[i] < a[j]   -> mirroring the left half would give a number smaller
    #                    than the original, so we must add 1.
    #   a[i] > a[j]   -> mirroring the left half already gives a bigger number,
    #                    so no increment is needed.
    if i < 0 or a[i] < a[j]:
        # Start the increment at the middle of the left half.
        # For odd n this is the center element, (n-1)//2 = n//2.
        # For even n it is the last left-half element, (n-1)//2 = n//2 - 1.
        k = (n - 1) // 2
        carry = 1

        # Add 1 and propagate the carry leftward until it becomes 0.
        # Since the all-9s case was handled above, we always stop before k < 0.
        while k >= 0 and carry:
            a[k] += 1
            carry = a[k] // 10   # 1 if the digit became 10, else 0
            a[k] %= 10           # keep the digit in the 0-9 range
            k -= 1

    # Mirror the left half onto the right half.
    # Only the first n//2 elements are copied, so the center of an odd-length
    # array stays as it is.
    for k in range(n // 2):
        a[n - 1 - k] = a[k]

    return a