<br />
<p align="center">
  <h1 align="center">Scott Caputo | Algorithmic Sorting Visualizer</h1>

  <p align="center">
    + Created using Python
  </p>
  <p align="center">
    + Animated Visualization using Matplotlib
  </p>
  <p align="center">
    + Multiple Highly Used Sorting Algorithms
  </p>
  <p align="center">
    <a href="https://github.com/scottvcaputo">scottvcaputo.github.io</a>
    <br />
    <br />
  </p>
</p>

<p align="center">
    <img src="https://media.giphy.com/media/j32hdrc5bkTxJuAW5i/giphy.gif" alt="Demo" />
</p>

## Langauge:
+ Python

## Modules and Packages 
+ random
+ time
+ matplotlob.pyplot
+ matplotlib.animation

## Introduction & Inspiration
+ When designing this project I wanted to gather a better understanding of some of the more commonly used algorithms. The goal was to successully implement the algorithms while creating a visualized explanation displaying how the algorithms are processing information.
+ This project was written out in Python
+ Inspiration was taken from three different repositories, which helped in provide inspiration in terms of algorithmic implementation as well as appealing visual represention.
1. [JS-Sorting-Algorithm](https://github.com/hustcc/JS-Sorting-Algorithm)
2. [Sorting-Visualizer](https://github.com/clementmihailescu/Sorting-Visualizer)
3. [sorts](https://github.com/nrsyed/sorts)

## Algorithms Implemented

### 1. Bubble Sort
+ Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

**Worst and Average Case Time Complexity:** O(n*n). Worst case occurs when array is reverse sorted.

**Best Case Time Complexity:** O(n). Best case occurs when array is already sorted.

**Auxiliary Space:** O(1)

**Boundary Cases:** Bubble sort takes minimum time (Order of n) when elements are already sorted.

**Sorting In Place:** Yes

**Stable:** Yes

[More Information: Bubble Sort](https://www.geeksforgeeks.org/bubble-sort/)

### 2. Merge Sort
+ Like QuickSort, Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.

**Auxiliary Space:** O(n)

**Algorithmic Paradigm:** Divide and Conquer

**Sorting In Place:** No in a typical implementation

**Stable:** Yes

[More Information: Merge Sort](https://www.geeksforgeeks.org/merge-sort/)

### 3. Insertion Sort
+ Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

**Time Complexity:** O(n*2)

**Auxiliary Space:** O(1)

**Boundary Cases:** Insertion sort takes maximum time to sort if elements are sorted in reverse order. And it takes minimum time (Order of n) when elements are already sorted.

**Algorithmic Paradigm:** Incremental Approach

**Sorting In Place:** Yes

**Stable:** Yes

**Online:** Yes

[More Information: Insertion Sort](https://www.geeksforgeeks.org/insertion-sort/)

### 4. Selection Sort
+ The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

+ 1) The subarray which is already sorted.
+ 2) Remaining subarray which is unsorted.

+ In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

**Time Complexity:** O(n2) as there are two nested loops.

**Auxiliary Space:** O(1) The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is a costly operation.

[More Information: Selection Sort](https://www.geeksforgeeks.org/selection-sort/)

### 5. Heap Sort
+ Heap sort is a comparison based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the maximum element and place the maximum element at the end. We repeat the same process for remaining element.

**Notes:**
- Heap sort is an in-place algorithm.
- Its typical implementation is not stable, but can be made stable (See this)

**Time Complexity:** Time complexity of heapify is O(Logn). Time complexity of createAndBuildHeap() is O(n) and overall time complexity of Heap Sort is O(nLogn).

[More Information: Heap Sort](https://www.geeksforgeeks.org/heap-sort/)

### 6. Quick Sort
+ Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

1. Always pick first element as pivot.
2. Always pick last element as pivot (implemented below)
3. Pick a random element as pivot.
4. Pick median as pivot.

**Analysis of QuickSort:** Time taken by QuickSort in general can be written as following.

[More Information: Quick Sort](https://www.geeksforgeeks.org/quick-sort/)

