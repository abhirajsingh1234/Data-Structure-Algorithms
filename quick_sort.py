def partition(arr, low, high):
    # Step 1: Choose the last element of the current sub-array as our pivot
    pivot = arr[high]
    
    # Step 2: Initialize pointer 'i' to track the boundary for elements smaller than the pivot.
    # It starts at one position before 'low' (e.g., -1 for the first call).
    i = low - 1
    
    # Step 3: Scan through the sub-array from 'low' up to 'high - 1' using pointer 'j'
    for j in range(low, high):
        # Check: Is the current element smaller than the pivot?
        if arr[j] < pivot:
            # If yes, expand our 'smaller elements' boundary
            i += 1
            # Swap the smaller element at 'j' into the boundary position at 'i'
            arr[i], arr[j] = arr[j], arr[i]

    # Step 4: Finalize the pivot position.
    # Put the pivot into its exact correct sorted spot (at index i + 1) 
    # and move the displaced larger element to the end.
    arr[i + 1], arr[high] = pivot, arr[i + 1]
    
    # Print statement to visualize how the array changes after each partition
    print(f"After partition (Pivot = {pivot}): {arr}")
    
    # Return the permanent index where the pivot settled
    return i + 1


def quick(arr, low, high):
    # Base Case: If low < high, the sub-array has 2 or more elements.
    # If low >= high, the sub-array has 0 or 1 element, meaning it's already sorted.
    if low < high:
        # Step A: Partition the array and get the pivot's final index
        pivot = partition(arr, low, high)
        
        # Step B: Recursively sort the LEFT sub-array 
        # (everything to the left of the pivot)
        quick(arr, low, pivot - 1)

        # Step C: Recursively sort the RIGHT sub-array 
        # (everything to the right of the pivot)
        quick(arr, pivot + 1, high)


# --- Testing the Code ---
numbers = [3, 1, 2, 6, 7, 8, 5]
print(f"Original array: {numbers}\n--- Starting Quick Sort ---")
quick(numbers, 0, len(numbers) - 1)
print(f"\nFinal sorted array: {numbers}")