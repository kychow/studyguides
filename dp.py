'''
Dynamic usually implies that time is an element of the problem (as opposed to static).
How to recognize:
* overlapping subproblems 
* optimal substructure

Problem statement: 
Find the optimal [minimum / maximum / number of ways] to do something to an input.
This implies the problem can be solved by DP or by greedy.

DP vs. greedy: 
In DP, future decisions depend on past decisions. 
In greedy, a decision is made based only on the state variables at step t

Example of a DP problem: house robber 

There are two types of DP: 
1. Top-down (memoization)
2. bottom-up (tabulation) 

Bottom-up (tabulation) is usually faster.
Top-down (memoization) is usually easier to write because the ordering of subproblems doesn't matter.

DP improves backtracking (iteratively building partial solutions)
1. define backtracking solution
2. figure out how best to memoize update state calculations 
3. check optimization satisfies time and space constraints
'''