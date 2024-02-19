# Graph Algorithms 
Following part II of programmers' handbook

### Terminology 
regular graph: every node in a graph has the same degree 

indegree: number of edges going into node
outdegree: number of edges going out of node

colorings: nodes are assigned color so no adjacent nodes have the same color 
bipartite graph: graph that can be colored with 2 colors
    Any graph that doesn't contain cycles with odd number of edges
    is a bipartite graphs. 

simple graph: no edge starts and ends at the same node
    - no two edges start and end at the same node 

## Graph Representation
How graphs are represented depends on the size of the graph and how we plan on processing it. 
Adjacency lists are useful when you want to find which node to go to next from a given node. (directed, sparse)
Adjacency matrices are optimized to check edge existence between two nodes. (good for grids, dense graphs)


Directed graphs
    [] topological sort 
    [] successor paths and graphs
    [] number of possible paths
    [] Floyd's cycle detection