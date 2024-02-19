# Py3 STDLIB 

## General 
* [T/F Value testing][3] 
    * `all()`: all values in iterable are True
* ints have unlimited size
* Tuples are immutable
* `float('inf’), float(‘-inf’)`: max float. Prints as inf (literally)
* `math.inf`: largest positive int value
* `chr()`: character
* `id()`: memory address of variable 

> Hash table vs. Dictionary: 
> 1. hash tables are loosely typed dictionaries.
> 2. Dictionaries have explicit types 

## Lists
* `**`: unpack mapping
* `*`: unpack list
* `zip()`: opposite of * 
* `List[:]`: modify elements in-place 
* `list.remove("a")`: remove by value 
* `list.pop(index=-1)`: remove by index, default -1 eol
* `list.del()`: remove by slice
* `list.clear()`: remove all items 
* `list.append()`:  
* `min()`: find min item in list
* `index()`: get index of value in list. -1 if not found
* checks if list is empty: if not list: # do stuff
    * `if []`: checks list existence
    * `if not list`: checks if list is empty. Else: not empty

## Insert and Set Operations
* `bisect()`: insertion order 
* `bisect_left()`:
* `bisect_right()`: 
* `set(a) & set(b)`: intersection of a and b

## Strings
* `''.join(char_list)`: string from list of chars
* `s1.find(s2, begin=0, end=len(s1))`: find s2 in s1[begin:end]
* `s.split(delimiter=“ “, num)`: split s by delimiter into `num` number of lines
* `s.replace()`: creates new object (strings are immutable)
    * usually inefficient, use slices instead
* `filter()`
* `s1.extend(s2)`
* `s.find(char)`: first index of char in s
* `s.rfind(char)`: first index of char from right 

## Itertools 
* `permutations()`
* `groupby()`: group list of items by sameness
```
def permute(nums: List[int]) -> List[List[int]]:
    indices = list(permutations(range(len(nums))))
    return [[nums[i] for i in index] for index in indices]

s = "aabbcca"
# 1. to get grouping 
substs = [''.join(group) for _, group in groupby(s)]
print(substrs) # substrs = ["aa", "bb", "cc", "a"]

# 2. to get key: 
groups = defaultdict{list} 
for k, group in groupby(s): 
    groups[k].append(group)

for i, group in groupby(s):
    print(i, list(group))
# a ['a', 'a']
# b ['b', 'b']
# c ['c', 'c']
# a ['a']
```

## Counting
### [Counter][1]
* [counter runtime][4]
* dict[element]: frequency count
```
From collections import Counter

c = Counter([0, 0, 0, 1])
Counter[0] = 3
Counter[2] = 0 # 2 doesn't exist, default 0
# returns a LIST of the most common items (num, count)
c.most_common(5) = [(0, 3), (1, 2)] # 5 most common elements in counter
```

## Sorting
* `nums.sorted()`: Sort in place (slightly faster, returns None)  
* `sorted()`: Sort by key, returns string 
    * `sorted(nums, key=lambda each_tuple: tuple[1])` # sort by number
    * `sorted(dict.items(), key = lambda x: x[0])` sort dictionary by key. 
        * `key lambda x: x[1]`: sort by value 

## Stack 
* In Python the best implementation of a stack is a list
* How to treat list like a stack: 
    * `stack.empty()`: bool if stack empty 
    * `stack.size()`: returns size of stack 
    * `stack.peek()`: return top element 
    * `stack.append()`: (push) insert element at top 
    * `stack.pop()`: delete topmost element 
## Queue / Deque
* `From collections import deque` 
* Deques are designed to have fast appends and pops from both ends 
    * `pop(0) `and `insert(0, v)` have `O(n)` runtime since the size of the underlying memory object changes with each operation 
    * `deque.append()`: (push) insert element at top 
    * `deque.pop()`:  delete topmost element 

## Heaps [2]
* `heapify()`: creates heap from list in linear time
* `heappop(heap)`: pops smallest val in O(log n) time 
* `heappush(heap, val)`: pushes val onto heap in O(log n) time

## Trees
* Binary tree: all nodes have 0-2 children
* In-order, preorder, postorder: 
* BST (Binary Search Tree):  all values in the left subtree are less than the value of the node 
    * All values in the right subtree are strictly greater than the value of the node. 

## Ascii
* `ascii()`: get ascii of char
* `ord('a': str)` = 97: get ascii of char 
* `chr(97: int)` = a: get char from ascii int 
* a = 97, A = 75, 0 = 48 

# Math 
https://docs.python.org/3/library/math.html#math.comb
* `math.comb(n, k)`: n choose k

# Bit Ops, Hex, & Bases 
* `//`: floor division (same as math.floor())
    * 7.5 // 2 = 3 
* `&`: bitwise AND
    * https://docs.python.org/3/library/operator.html#mapping-operators-to-functions
* `>>`: bitwise right shift
    * `n <<= 1`: multiply n by 2
    * `n <<= 2`: multiply n by 4
* `<<`: bitwise left shift 
    * `5 >> 2` = 5*4 = 20
* `isalnum()` checks if value is alphanumeric 
* `format(num, ‘b<new_base>’)` convert base 10 string to base(2 - 32) string 
* `bin()` cast to binary format with preceding ‘0b’  
    * `bin(5)` = ‘0b110’
* `hex()`, `oct()`: same but for base 6, 8
* `int(num, 2)`: convert binary number back to int

---
# Non-Interview 
## Command Line
* -m module 
* python -m timeit 's = "apple";"pl" in s'
* python -m timeit 's = "apple";"pl" in s

## Timer
```
From time import timeit
```

[1]: https://docs.python.org/3/library/collections.html#collections.Counter
[2]: https://docs.python.org/3/library/heapq.html
[3]: https://docs.python.org/3/library/stdtypes.html#truth
[4]: https://stackoverflow.com/questions/40513659/python-collections-counter-runtime 


