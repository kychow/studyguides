'''
Greedy
1. All greedy problem can be solved with dynamic programming. 
2. Greedy solutions take the best option at each step (no memoization)
3. Greey usually requires preprocessing the data: resorting, reranking, etc.

Pattern: 
Find [min / max / first]


Full workflow to solve Greedy / DP problems: 
1. brute-force recursion (that would be easy to memoize)
2. top-down DP (memoization)
3. bottom-up DP (tabulation)
4. greedy (at this point we want to get to < polynomial-time-complexity. 
A common pattern is to sort/reverse the array and iterate.

'''