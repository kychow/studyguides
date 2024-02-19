# Chinese Remainder Theorem

## Itertools 
# https://docs.python.org/3/library/itertools.html#itertools.combinations
# * `permutations(range(n) or list)`
# * `product(*some_lists)`: generate all combinations of a bunch of lists, one item from eaach list

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        indices = list(permutations(range(len(nums))))
        return [[nums[i] for i in index] for index in indices]
    
    def generate_combinations(some_lists): 
        return list(product(*some_lists))


## Counting
# * [counter runtime][4]
# * dict[element]: frequency count
from collections import Counter

c = Counter([0, 0, 0, 1])
Counter[0] = 3
Counter[2] = 0 # 2 doesn't exist, default 0
c.most_common(5) = [(0, 3), (1, 2)] # 5 most common elements in counter
