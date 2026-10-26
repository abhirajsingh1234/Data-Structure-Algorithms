def Merge(arr, left, mid, right):
    print("-" * 30)
    L = mid - left + 1
    R = right - mid
    print(f"{left},{mid},{right}")
    print("length of Left and Right")
    print(f"L : {L}")
    print(f"R : {R}")

    # Copy data to temporary subarrays left_array[] and right_array[]
    left_array = [0] * L
    right_array = [0] * R
    
    for i in range(L):
        left_array[i] = arr[left + i]

    for i in range(R):
        right_array[i] = arr[mid + 1 + i]

    print(f"initialized left and right subarrays: left_array : {left_array}, right_array : {right_array}")

    i = 0  # Initial index of first subarray (left_array)
    j = 0  # Initial index of second subarray (right_array)
    k = left  # Initial index of merged subarray (arr)

    # --------------------------------------------------------------------------
    # MERGE LOGIC FOR ODD / EVEN ARRAYS:
    # Recursion guarantees that 'left_array' and 'right_array' are ALREADY SORTED
    # before entering this Merge step.
    #
    # Example (Odd-length array [5, 4, 3, 2, 1]):
    # When merging left side [4, 5] (len 2) with right side [3] (len 1):
    # - The main comparison loop runs until one array exhausts all elements.
    # - If right_array [3] completes first (since it has only 1 element),
    #   left_array [4, 5] still has remaining elements.
    # - Because [4, 5] is LOGICALLY ALREADY SORTED by prior recursive calls,
    #   we don't need any more comparisons! We simply flush remaining left elements
    #   directly into 'arr' in order.
    # --------------------------------------------------------------------------

    # Main comparison loop: Compare elements from left and right arrays
    while i < L and j < R:
        if left_array[i] <= right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1
        print(f"looping : array : {arr}")

    # Copy remaining elements of left_array[], if any.
    # (Triggered when right_array finishes first, e.g., in odd splits where right side has fewer elements)
    while i < L:
        arr[k] = left_array[i]
        i += 1
        k += 1
        print(f"looping : after adding left array : {arr}")

    # Copy remaining elements of right_array[], if any.
    # (FIXED BUG: index updated from 'i' to 'j' for right_array)
    while j < R:
        arr[k] = right_array[j]
        j += 1
        k += 1
        print(f"looping : after adding right array : {arr}")


def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        # ----------------------------------------------------------------------
        # RECURSION HAPPENING HERE:
        # Divide phase: Split the array recursively into halves until single-element
        # subarrays are reached (base case: left >= right).
        # ----------------------------------------------------------------------

        # 1. Recursive call for the left half:
        #    Drills down left subtree to isolate left individual elements.
        mergeSort(arr, left, mid)

        # 2. Recursive call for the right half:
        #    Drills down right subtree to isolate right individual elements.
        mergeSort(arr, mid + 1, right)

        # ----------------------------------------------------------------------
        # Conquer/Combine phase:
        # After both recursive calls return (meaning left and right halves are sorted),
        # Merge() combines them back into a single sorted range [left...right].
        # ----------------------------------------------------------------------
        Merge(arr, left, mid, right)


arr = [5, 4, 3, 2, 1]
mergeSort(arr, 0, len(arr) - 1)
print("Final Sorted Array:", arr)