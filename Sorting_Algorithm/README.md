# Sorting Algorithms
In this part, different sorting algorithms such as bubble, selection, insertion, merge, quick, counting, radix, bucket, heap and shell sortings are presented. 
Each sorting algorithms has its own time and space complexities.

## Bubble Sort
Bubble sort is a sorting algorithm that compares two adjacent elements and swaps them until they are in the intended order. The time complexity of this algorithm in worst case is in order of $n^2$.

## Selection Sort
Selection sort is a sorting algorithm that selects the smallest element from an unsorted list in each iteration and places that element at the beginning of the unsorted list. To do so, it consider the first element as the minimun value and compared other ones with it till it find another element that is smaller than this first element. Then it will replace the first element with the smallest element in the list and go to the second element and will do the same thing till the whole array becomes sorted. The time complexity of this algorithm in worst case is in order of $n^2$.

## Insertion Sort
Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration.
Insertion sort works similarly as we sort cards in our hand in a card game.
We assume that the first card is already sorted then, we select an unsorted card. If the unsorted card is greater than the card in hand, it is placed on the right otherwise, to the left. In the same way, other unsorted cards are taken and put in their right place. The time complexity of this algorithm in worst case is in order of $n^2$.

## Merge Sort
Merge sort is one of the most popular sorting algorithms that is based on the principle of Divide and Conquer Algorithm. The time complexity of this algorithm is $(n\times \log n)$.

## Quick Sort
Quicksort is a sorting algorithm based on the divide and conquer approach. The time complexity of this algorithm is $(n\times \log n)$ on average and its space complexity is $(\log n)$.

## Count Sort
Counting sort is a sorting algorithm that sorts the elements of an array by counting the number of occurrences of each unique element in the array. The count is stored in an auxiliary array and the sorting is done by mapping the count as an index of the auxiliary array.

## Input-Output
Input: The integer arrays separated by ',' should be insrted by user. The type of sorting algorithm shall be inserted by user.

Output: The ascending sorted arrays of integers.