# Range Queries 
'''
Ch 9 of Programmers' handbook. 
Range queries are a set of tasks where you calculate a value based on a subarray of an array. 

Range queries typically ask for a [sum, min, max] values in a range [a, b]. 

The brute force approach is to loop through all array values in a given range (O(n) time).

1. Static array queries
Given a static array (i.e. array values remain constant between queries), sum queries can be done with 
* Prefix sum array: each value in array = sum i mvalues up to that point. Can be constructed in O(n) time.
    * any sum can be calculated in O(1) time. 
    * prefix sums can be generalized to higher dimensions
    * TODO 2D prefix sum array problem
* Minimum queries (sparse table method): slightly more difficult, calculate all values of min(a, b) where b - a + 1 is a power of 2.
    * the number of precalculated values is O(n log n) because 
    there are o(log n) range lengths that are powers of two. 
    * preprocessing time: O(n log n)
    * query time: O(1)
* Binary indexed tree (Fenwick Tree): dynamic variation of a prefix sum array
    * binary index trees (fenwick trees) basically same purpose as prefix sum tree except you can update array values between range sum queries
    * O(n) prefix update time -> O(log n) update time 
    * preprocessing time: O(log n)?
    * query time: O(2 log n)
    * drawback: insert and delete are slow 

* Segment tree: binary tree where leaf nodes are array elements and parent nodes are used to calculate range queries.
    * It's most convenient to  build segment trees for arrays with lengths that are powers of two. 
    * if array is not length 2**n, pad the array.
    * any range [a, b] can be divided into O(log n) ranges whose values are stored in tree nodes. 
    * the parent of tree[k] is tree[floor(k/2)]
    * the child of tree[k] is tree[2k] and tree[2k+1]
'''