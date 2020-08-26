import random
import time

import matplotlib.pyplot as plt
import matplotlib.animation as animation




# yield:
        # The yield statement suspends function’s execution and sends a value back to the caller, but retains enough state to enable function to resume where it is left off. When resumed, the function continues execution immediately after the last yield run. This allows its code to produce a series of values over time, rather than computing them at once and sending them back like a list.




def swap(A, i, j):

    if i != j:
        A[i], A[j] = A[j], A[i]







# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent if they are in wrong order.
# defined is an optimized form of the Bubble Sorting algorithm
def bubbleSort(A):

    if len(A) == 1:
        return
   
    # sort through all array elements 
    for i in range(len(A)-1): 

        # to show that the plot has not been fully sorted yet
        swapped = False
  
        # Last i elements are already 
        #  in place 
        for j in range(0, len(A)-1-i): 
   
            # traverse the array. Swap when (j) is larger than (j + 1)
            if A[j] > A[j+1] : 
                A[j], A[j+1] = A[j+1], A[j] 
                swapped = True
            
            yield A
  
        # when no two elements were swapped in the inner loop, break
        if swapped == False: 
            break







# Merge Sort is a Divide and Conquer algorithm.
# It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one. See following C implementation for details.
def mergeSort(A, L, R):

    # broken up to compare the right and the left elements 
    if R <= L:
        return

    # here we define what the middle of the plot is
    M = L + ((R - L + 1) // 2) - 1
    # shows actions between left and middle along A
    yield from mergeSort(A, L, M)
    # shows actions between middle and right along A
    yield from mergeSort(A, M + 1, R)
    # shows the actions carried out by the helper function 
    yield from merge(A, L, M, R)
    # yield A
    yield A

def merge(A, L, M, R):
    """Helper"""

    sorted = []

    # the index of the right and left regions of the plot 
    LIdx = L
    RIdx = M + 1

    while LIdx <= M and RIdx <= R:
        if A[LIdx] < A[RIdx]:
            sorted.append(A[LIdx])
            LIdx += 1
        else:
            sorted.append(A[RIdx])
            RIdx += 1

    while LIdx <= M:
        sorted.append(A[LIdx])
        LIdx += 1

    while RIdx <= R:
        sorted.append(A[RIdx])
        RIdx += 1

    for i, element in enumerate(sorted):
        A[L + i] = element
        yield A







# Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.
def insertionSort(A): 
  
    # sort through 1 to len(A) 
    for i in range(1, len(A)): 
  
        ref = A[i] 
  
        # Move elements that are greater than ref, one position ahead in range 
        j = i-1

        while j >= 0 and ref < A[j] : 
                A[j + 1] = A[j] 
                j -= 1
                yield A

        A[j + 1] = ref 








# The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array:    
                # 1) The subarray which is already sorted.
                # 2) Remaining subarray which is unsorted.
def selectionsort(A):

    if len(A) == 1:
        return

    for i in range(len(A)):
        # address minimum unsorted value.
        minValue = A[i]
        minIdx = i
        for j in range(i, len(A)):
            if A[j] < minValue:
                minValue = A[j]
                minIdx = j
            yield A
        swap(A, i, minIdx)
        yield A








#Heap sort is a comparison based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the maximum element and place the maximum element at the end. We repeat the same process for remaining element.
def heapSort(A): 
    n = len(A) 
  
    # maxheap 
    for i in range(n//2 - 1, -1, -1): 
        heap(A, n, i) 
        yield A
  
    # element extraction 
    for i in range(n-1, 0, -1): 
        A[i], A[0] = A[0], A[i]
        heap(A, i, 0) 
        yield A

def heap(A, n, i): 
    """Helper"""
    # this function is rooted at the index 
    # n = heap size
    largest = i # initialize largest as root 
    L = 2 * i + 1
    R = 2 * i + 2
  
    # See if left child of root exists and is greater than root 
    if L < n and A[i] < A[L]: 
        largest = L
  
    # See if right child of root exists and is greater than root 
    if R < n and A[largest] < A[R]: 
        largest = R 
  
    # change root, if needed 
    if largest != i: 
        A[i],A[largest] = A[largest],A[i]
  
        # heaps the root 
        heap(A, n, largest) 







# quickSort is a Divide and Conquer algorithm
# It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.
def quickSort(A, L, R):

    if L >= R:
        return

    # pivot element and pivot index
    pivotEle = A[R]
    pivotIdx = L

    for i in range(L, R):
        if A[i] < pivotEle:
            swap(A, i, pivotIdx)
            pivotIdx += 1
        yield A
    swap(A, R, pivotIdx)
    yield A

    yield from quickSort(A, L, pivotIdx - 1)
    yield from quickSort(A, pivotIdx + 1, R)








if __name__ == "__main__":

    # UI information
    elements = int(input("Enter number of integers: "))
    N = elements
    message = "Please select algorithmic sorting method:\n\t bubble\n\t merge\n\t insertion\n\t selection\n\t heap\n\t quick\n\t"
    methodSelection = input(message)

    # create a randomly shuffled element list to feed the sorting algorithms
    A = [x + 1 for x in range(N)]
    random.seed(time.time())
    random.shuffle(A)

    # select sorting algorithm to display
    if methodSelection == "bubble":
        title = "Bubble sort"
        sortingAlgo = bubbleSort(A)

    elif methodSelection == "merge":
        title = "Merge sort"
        sortingAlgo = mergeSort(A, 0, N - 1)

    elif methodSelection == "insertion":
        title = "Insertion sort"
        sortingAlgo = insertionSort(A)

    elif methodSelection == "selection":
        title = "Selection sort"
        sortingAlgo = selectionsort(A)

    elif methodSelection == "heap":
        title = "Heap sort"
        sortingAlgo = heapSort(A)

    elif methodSelection == "quick":
        title = "Quick Sort"
        sortingAlgo = quickSort(A, 0, N - 1)

    else: print("Sorry, this option is not available \n Please select one of the sorting alogrithms listed")


    # figure and axis initialization
    fig, ax = plt.subplots(figsize=(12, 9))
    ax.set_title(title, fontsize=20)

    ax.spines["top"].set_visible(False)  
    ax.spines["right"].set_visible(False)  
    ax.spines["left"].set_visible(False)  

    ax.get_xaxis().tick_bottom()  
    ax.get_yaxis().set_ticks([])

    # set plot element characteristics 
    plotElements = ax.bar(range(len(A)), A, align="edge", color="#1F618D", edgecolor="#1C2833", linewidth = '1.5') 
    # color="#566573", edgecolor="#1F618D"

    ax.set_facecolor('#F2F3F4')

    # set boundary parameters 
    ax.set_xlim(-1, N + 1)
    ax.set_ylim(0, int(1.07 * N))


    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    # set iteration count to compliment yield 
    iteration = [0]

    def updatePlot(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("operations: {}".format(iteration[0]))

    animate = animation.FuncAnimation(fig, func=updatePlot, fargs=(plotElements, iteration),
                                    frames=sortingAlgo, interval=1, repeat=False)

    plt.show()