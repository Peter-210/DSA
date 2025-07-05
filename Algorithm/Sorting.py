import heapq

def bubbleSort(input):
    if len(input) <= 1:
        return input
    
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
    if len(input) <= 1:
        return input
    
    arr = input.copy()
    for i in range(1, len(arr)):
        for j in range(i, -1, -1):
            if arr[i] < arr[i-j]:
                arr[i-j], arr[i] = arr[i], arr[i-j]
    return arr

def selectionSort(input):
    if len(input) <= 1:
        return input
    
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
    # Check for base case (One element in array)
    if len(arr) <= 1:
        return arr
    
    # Move low values to the low array and high values to the high array
    mid = len(arr) // 2
    lowArr = []
    highArr = []
    for i in range(len(arr)):
        if i == mid:
            continue
        if arr[i] <= arr[mid]:
            lowArr.append(arr[i])
        else:
            highArr.append(arr[i])
    
    # Recursively sort low and high arrays
    left = quickSort(lowArr)
    right = quickSort(highArr)

    return left + [arr[mid]] + right

def heapSort(arr):
    if len(arr) <= 1:
        return arr

    # Alternative is to swap root with last element for in-place sort
    result = [0] * len(arr)
    heapq.heapify(arr)
    for i in range(len(arr)):
        result[i] = heapq.heappop(arr)
    
    return result

def countingSort(arr):
    if len(arr) <= 1:
        return arr
    
    # Get the min and max values
    min = arr[0]
    max = arr[0]
    for value in arr:
        if value < min:
            min = value
        if value > max:
            max = value
    
    # Calculate the offset for the size of counting array
    offset = min - 0
    count = [0] * (max - offset + 1)

    # Plot frequencies to counting array
    for value in arr:
        idx = value - offset
        count[idx] += 1

    # Append frequency values to resulting array
    # Alternate is to reuse the original array and override the values
    result = []
    for value in range(len(count)):
        while count[value] > 0:
            result.append(value + offset)
            count[value] -= 1
    
    return result


if __name__=="__main__":
    arr = [9, -1, 4, 2, 6, 4, 7, 9, 10, -11, 2]
    print(arr)
    arr = heapSort(arr)
    print(arr)