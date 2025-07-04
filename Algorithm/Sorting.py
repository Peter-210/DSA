def bubbleSort(input):
    arr = input.copy()
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

def insertionSort(input):
    arr = input.copy()
    for i in range(1, len(arr)):
        for j in range(i, -1, -1):
            if arr[i] < arr[i-j]:
                arr[i-j], arr[i] = arr[i], arr[i-j]
    return arr

def selectionSort(input):
    arr = input.copy()
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def mergeSort(arr):
    # Check for base case (One element in array)
    if len(arr) <= 1:
        return arr
    
    # Recursively split array until base case
    mid = len(arr) // 2
    leftArr = mergeSort(arr[:mid])
    rightArr = mergeSort(arr[mid:])

    # Merge the sub-arrays together in sorted order
    l = r = 0
    result = []
    while l < len(leftArr) and r < len(rightArr):
        if leftArr[l] <= rightArr[r]:
            result.append(leftArr[l])
            l += 1
        else:
            result.append(rightArr[r])
            r += 1

    # Append the rest of the array (sorted) to the resulting array
    result.extend(leftArr[l:])
    result.extend(rightArr[r:])
    
    return result

def quickSort(arr):
    pass

def heapSort(arr):
    pass

def countingSort(arr):
    pass

def radixSort(arr):
    pass

if __name__=="__main__":
    arr = [9, 1, 4, 2, 6, 4, 7, 9, 10, 11, 2]
    print(arr)
    arr = bubbleSort(arr)
    print(arr)