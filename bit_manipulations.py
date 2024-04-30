'''
Bit manipulations 
1. typically improves runtime by 1 order of magnitude. 
2. Most commonly to iterate through permutations and as bitmasks. 
1. Array bitmasks are most commonly build with XOR

* a & (1 << i) get the ith bit of a 
* a ^= 1 << i flips the ith bit of a
* a |= 1 << i set the ith bit of a
* a &= ~(1 << i) clear the ith bit of a
* a & (a - 1) remove the rightmost signifcant bit in x
* a & -a sets all the one bits except last one bit to 0


Brian Kernighan's Algorithm: counting the number of 1-bits of an integer.
Opierates directly on bits and runs in O(k) time, where k is the number of bits 
set to 1.  Kernighan's algorithm works by repeatedly flipping the last signifigant 
1-bit of the numberto 0 and counting operations until the number becomes 0. 


'''