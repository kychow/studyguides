''' 
# 1. Pattern
Min-max some heuristic for a 1-d data structure if you can do at most x operations on it. 

The input is usually a large array-like data structure such as a string, list, etc. 
Question statement is [longest, maximum] [subsequence, subarray, substring, subset] of a 
[string, list of numbers] given some number of operations you can do on array values 
[delete, swap with a neighbor, update] to reach a desired state. 

For [increment left until window is valid]: 
Only increment the left side if the window condition is *strictly* broken,
as the left pointer is always incremented inside this check. 
'''

# 2. Pseudocode
# function slidingWindow(array, windowSize):
#     initialize window start and end pointers
#     initialize variables to hold the computation result

#     while the end pointer is not at the end of the array:
#         expand the window by moving the end pointer and update the result computation

#         while the current window meets the condition (e.g., window size or a certain property):
#             update the computation result if necessary
#             contract the window by moving the start pointer

#     return computation result

# 3. Template 
def sliding_window(arr):
    l, curr_state, ans = 0, 0, 0
    # state-related variables, final answer-related var

    for r in range(len(arr)):
        # 1. update state variables at arr[r]

        # 2. increment left and state variables until window is valid
        while WINDOW_CONDITION_BROKEN:
            # remove arr[left] from curr
            l += 1

        # 3. Update answer variable w/ state-related var

    return ans

# 4. Example implementations
# 2024. Maximize the Confusion of an Exam
def maxConsecutiveAnswers(answers: str, k: int) -> int:
    l, max_same = 0, 0, 0
    majority = {"T": 0, "F": 0}
    for r in range(len(answers)):
        majority[answers[r]] += 1
        while min(majority.values()) > k:
            majority[answers[l]] -= 1
            l += 1
        max_same = max(max_same, r - l + 1)
    return max_same

# 5. Problem List 
https://leetcode.com/list/p9b40lce
# Longest Substring Without Repeating Characters
# Minimum Size Subarray Sum
# Longest Substring with At Most K Distinct Characters
# Longest Repeating Character Replacement
# Fruit Into Baskets
# Maximum Sum of Distinct Subarrays With Length K