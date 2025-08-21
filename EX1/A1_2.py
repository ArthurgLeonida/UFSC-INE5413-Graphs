from graph_utils import Graph
from collections import deque, defaultdict

graph_file = 'EX1\sample_graph.txt'

graph = Graph()
graph.ler(graph_file)

#print(graph.vertices)

def bfs(graph: Graph, start):
    """Perform BFS and return vertices organized by levels"""
    visited = set()
    queue = deque([(start, 0)]) # (vertex, level)
    levels = defaultdict(list) # level -> [vertices]

    visited.add(start)

    while queue:
        vertex, level = queue.popleft()
        levels[level].append(vertex)

        # Add neighbours to queue
        neighbors_tuples = sorted(graph.adjacency_list.get(vertex, []))
        #print(f'Debbug: {neighbors_tuples}')
        for neighbor_vertex, _ in neighbors_tuples:
            if neighbor_vertex not in visited:
                visited.add(neighbor_vertex)
                queue.append([neighbor_vertex, level+1])
    
    #print(levels)

    return levels

levels = bfs(graph=graph, start=2)  

# Print results
for level in sorted(levels.keys()):
    vertices_str = ','.join(map(str, sorted(levels[level])))
    print(f"{level}: {vertices_str}")

