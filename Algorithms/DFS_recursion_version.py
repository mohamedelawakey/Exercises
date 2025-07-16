def dfs_recursion(graph, node, visited):
    if node in visited:
        return 
    print('visited ', node)
    visited.add(node)
    for naighbor in graph[node]:
        dfs_recursion(graph, naighbor, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()
dfs_recursion(graph, 'A', visited)