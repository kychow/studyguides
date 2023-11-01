from typing import Dict, List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BFSTreeSolver:

	def bfs(self, root: Optional[TreeNode], adj_list) -> None:
		q = [root]
		visited = set()
		while q:
			node = q.pop(0)
			# do visit node logic
			for adj_node in adj_list:
				if adj_node not in visited:
					visited.add(adj_node)
					q.append(adj_node)
		return
