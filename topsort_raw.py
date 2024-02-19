from collections import deque
from typing import List

def topologicalSort(num_vertices: int, edges: List[int, int]) -> List[int]:
    indegree = {c: 0 for c in range(num_vertices)}
    adj_list = {c: [] for c in range(num_vertices)}

    for a, b in edges: 
        indegree[b] += 1
        adj_list[a].append(b)

    # initialize queue with indegrees 0 
    q = deque([c for c, degree in indegree.items() if degree == 0])
    ordering = []
    while q: 
        v = q.pop()
        ordering.append(v)
        for next_v in adj_list: 
            indegree[next_v] -= 1
            if indegree[next_v] == 0: 
                q.append(next_v)

    if len(ordering) != num_vertices: 
        return -1

    return ordering