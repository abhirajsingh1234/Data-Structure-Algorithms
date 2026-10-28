def insertion(arr, index):
    """
    Insertion Sort Helper Function:
    Takes an element at the specified 'index' (the 'key') and moves it 
    backward into its correct sorted position within the left subarray.
    """
    for i in range(index, -1, -1):  # Loop backward from the target index down to 0
        if i > 0:
            # Compare the current element with its left neighbor
            if arr[i] < arr[i - 1]:
                # If smaller, swap them (moving the element leftward)
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
            else:
                # If it's no longer smaller than the neighbor, it's in the right spot
                pass
        else:
            # Reached the very beginning of the array
            return arr


# The array we want to sort
arr = [7, 6, 5, 4, 8, 3]

# Ensure the array has enough elements to sort
if len(arr) - 1 > 0:
    # Main Loop: Treats each element one-by-one as an 'unsorted' item 
    # to be inserted into the growing sorted portion on the left.
    for i in range(len(arr) - 1):
        # Pass the array and the next index to be sorted (i + 1)
        arr = insertion(arr, i + 1)
        print(f"After processing index {i + 1}: {arr}")

print("Final Sorted Array:", arr)