from collections import deque

def BFS(graph, start, goal):
    visited = set()
    queue = deque([[start]])
    
    while queue:
        path = queue.popleft()
        node = path[-1]
    
        if node == goal:
            print('Shortest Path:', path)
            return path
        
        if node not in visited:
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

BFS(graph, 'A', 'F')