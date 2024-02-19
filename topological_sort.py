'''
1. Pattern
There are many real-world events where some events must happen before others. 
E.g. in the product development lifecycle, the planning meeting must happen before 
the eng planning meeting can happen. Topological sort questions usually ask you to 
find the universal ordering of a set of events or objects given some events or objects
happen or depend on others.

Prerequisites: DAG. Otherwise topological order cannot be established
'''

# 2. Pseudocode
# Indegree is the number of constraints (prerequisites) a vertex has 

# def topologicalSort(num_vertices: int, edges: List[int, int]) -> List[int]:
    # indegree = {c: 0 for c in range(num_vertices)}
    # adj_list = {c: [] for c in range(num_vertices)}

    # 1. build adjacency list and find indegree of each course
    # for source, destination in edges: 
        # adj_list[source].append(destination)
        # indegree[destination] += 1
    
    # 2. initialize a queue for DFS containing elements with no constraints on them (indegree = 0)
    # q = [v for v in range(num_vertices) if indegree[v] == 0]
    # ordering = []
    # while q: 
        # v = q.pop()
        # ordering.append(v)
        # for next_v in adj_list[v]:
            # indegree[next_v] -= 1
            # if indegree[next_v] == 0:
                # q.append(next_v)
    
    # 3. check if there's a cycle in graph (causes top ordering to be invalid)
    # if len(ordering) != num_vertices: 
        # return [] 
    
    # return ordering 

# 3. Example Usages
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = {c: 0 for c in range(numCourses)}
        adj_list = {c: [] for c in range(numCourses)}
        
        # 1. build adj_list and find indegree of each course
        for a, b in prerequisites: 
            adj_list[b].append(a)
            indegree[a] += 1

        # 2. do a topological sort on each element
        q = [c for c in range(numCourses) if indegree[c] == 0]
        ordering = [] 
        while q: 
            c = q.pop() 
            ordering.append(c)
            for next_course in adj_list[c]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)

        # 3. return the correct course ordering if its possible (no cycles) otherwise []
        if len(ordering) != numCourses: 
            return [] 
        return ordering 
        
