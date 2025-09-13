import sys
import heapq
from graph_utils import Graph

def dijkstra(graph, start_vertex):
    """
    Encontra o caminho mais curto de start_vertex para todos os outros vértices
    usando o algoritmo de Dijkstra.
    """
    # Fila de prioridade armazena tuplas de (distância, vértice)
    pq = [(0, start_vertex)]
    
    # Dicionário para armazenar a menor distância encontrada até agora para cada vértice
    distances = {v: float('inf') for v in graph.get_all_vertices()}
    distances[start_vertex] = 0
    
    # Dicionário para reconstruir o caminho
    predecessors = {v: None for v in graph.get_all_vertices()}

    while pq:
        current_dist, u = heapq.heappop(pq)

        # Se já encontramos um caminho mais curto, pulamos
        if current_dist > distances[u]:
            continue

        for v, weight in graph.adjacency_list[u]:
            distance_through_u = distances[u] + weight
            
            if distance_through_u < distances[v]:
                distances[v] = distance_through_u
                predecessors[v] = u
                heapq.heappush(pq, (distances[v], v))
                
    return distances, predecessors

def reconstruct_path(predecessors, start_vertex, end_vertex):
    """
    Reconstrói o caminho a partir do dicionário de predecessores.
    """
    path = []
    current = end_vertex
    # Retorna um caminho vazio se não houver caminho
    if predecessors[current] is None and current != start_vertex:
        return []
        
    while current is not None:
        path.append(current)
        current = predecessors[current]
    return path[::-1] # Retorna o caminho revertido (da origem ao destino)

def main():
    file_path = sys.argv[1]
    start_vertex = int(sys.argv[2])

    g = Graph()
    g.ler(file_path)

    if start_vertex not in g.vertices:
        print(f"Erro: O vértice {start_vertex} não existe no grafo.")
        return

    distances, predecessors = dijkstra(g, start_vertex)

    # Ordena os vértices por índice para uma saída consistente
    sorted_vertices = sorted(g.get_all_vertices())

    for v in sorted_vertices:
        dist = distances[v]
        # Só imprime se um caminho foi encontrado
        if dist != float('inf'):
            path = reconstruct_path(predecessors, start_vertex, v)
            path_str = ",".join(map(str, path))
            print(f"{v}: {path_str}; d={dist}")

if __name__ == "__main__":
    main()
    # COMANDO PARA TESTAR: python EX1/A1_4.py EX1/fln_pequena.net 1