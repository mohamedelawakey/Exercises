def dfs_stack(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            print('visited ', node)
            
            for naighbor in reversed(graph[node]):
                if naighbor not in visited:
                    stack.append(naighbor)
                    
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs_stack(graph, 'A')