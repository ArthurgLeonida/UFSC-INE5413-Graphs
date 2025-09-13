from graph_utils import Graph
from collections import deque, defaultdict
import sys

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

def main():
    file_path = sys.argv[1]
    start_vertex = int(sys.argv[2])

    g = Graph()
    g.ler(file_path)

    levels = bfs(graph=g, start=start_vertex)  
    for level in sorted(levels.keys()):
        vertices_str = ','.join(map(str, sorted(levels[level])))
        print(f"{level}: {vertices_str}")

if __name__ == "__main__":
    main()
    # COMANDO PARA TESTAR: python EX1/A1_2.py EX1/sample_graph.net 1
    # COMANDO PARA TESTAR: python EX1/A1_2.py EX1/ContemCicloEuleriano.net 1
    # COMANDO PARA TESTAR: python EX1/A1_2.py EX1/ContemCicloEuleriano2.net 1
    # COMANDO PARA TESTAR: python EX1/A1_2.py EX1/SemCicloEuleriano.net 1
