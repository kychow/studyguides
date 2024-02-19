'''
# 1. Pattern
Backtracking iteratively builds a solution piece by piece.
After selecting the next step in a solution path, 
1. state variables are updated
2. backtracking is called, 
3. state update is undone (backtracked) to the most recent valid solution
4. the remaining possible next steps are explored

Key point for backtracking: early stop.
Find early pruning conditions to optimize runtime.

How can we determine complete solutions are impossible from a partial solution?

Runtime: 
Space: 
'''

# 2. Pseudocode
# def backtrack(path):
#     if path is a solution: 
#         report success and return 

    # for all_next_choices from current state: 
        # if next_choice is valid: 
            # add next_choice to path
            # continue exploring new solution by calling backtrack(new_path)
            # if path leads to a solution: 
                # return success
            # remove last choice from the path (backtrack)
    # return failure
