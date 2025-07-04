def bubbleSort(arr):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]

def insertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(i, -1, -1):
            if arr[i] < arr[i-j]:
                arr[i-j], arr[i] = arr[i], arr[i-j]

def selectionSort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

def mergeSort(arr):
    pass

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
    bubbleSort(arr)
    print(arr)