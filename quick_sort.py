def partition(arr,low, high):
    pivot = arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1], arr[high] = pivot, arr[i+1]
    print(arr)
    return i+1

def quick(arr, low, high):
    if low<high:
        pivot = partition(arr,low, high)

        #left of pivot
        quick(arr, low, pivot-1)

        # right of pivot
        quick(arr,pivot+1, high)


quick([3,1,2,6,7,8,5],0,6)