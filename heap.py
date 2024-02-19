'''
Heaps.
Heap is an implementation of the concept of a priority queue. 
1. Heaps are complete binary trees (every level except last is filled)
2. Each node is less than its child nodes

construction: O(n) (heapify) 
insertion: O(log n)
deletion: O(log n)
get min or max element: O(1)

min heap: first element is smallest 
max heap: first element is largest 

# Heapsort
# 1. Is an optimization of selection sort
# 2. Is performced inplace. 

1. Patterns
[min / max / top k] elements 
Organized by values 

Heap Sort
The Top-K problem
The K-th element

Some tricks: 
* take -index for a maxheap
* can embed tuples onto a heap 
'''

# Import the heapq module for heap operations
import heapq

# pops smallest item THEN pushes element onto heap
heapq.heapreplace(heap, element)

# pushes item THEN pops smallest element
heapq.heappoppush(heap, element)

# creates min-heap in place from a list of elements
heapq.heapify(heap)

# Function to insert an element into the heap
heapq.heappush(heap, element)

# Function to pop the smallest element from the heap
return heapq.heappop(heap)

# Function to push a new element and pop the smallest element. Useful for maintaining a fixed-size heap.
def pushpop(heap, element):
    return heapq.heappushpop(heap, element)

# Function to replace the smallest element with a new element
def replace(heap, element):
    return heapq.heapreplace(heap, element)

# Function to get the n largest or n smallest elements from a heap
def nlargest(n, heap):
    return heapq.nlargest(n, heap)

def nsmallest(n, heap):
    return heapq.nsmallest(n, heap)
