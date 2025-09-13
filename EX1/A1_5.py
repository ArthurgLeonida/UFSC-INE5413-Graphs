import sys
from graph_utils import Graph

def floyd_warshall(graph):
    """
    Calcula os caminhos mais curtos entre todos os pares de vértices
    usando o algoritmo de Floyd-Warshall.
    """
    vertices = sorted(graph.get_all_vertices())
    
    # Inicializa o dicionário de distâncias
    dist = {u: {v: float('inf') for v in vertices} for u in vertices}

    # Define as distâncias iniciais com base nas arestas existentes
    for u in vertices:
        dist[u][u] = 0
        for v_neighbor, weight in graph.adjacency_list[u]:
            dist[u][v_neighbor] = weight

    # Algoritmo principal com três laços aninhados
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
            
    return dist

def main():
    file_path = sys.argv[1]
    g = Graph()
    g.ler(file_path)

    all_distances = floyd_warshall(g)
    sorted_vertices = sorted(g.get_all_vertices())

    for u in sorted_vertices:
        # Constrói a string para a linha atual
        distances_list = []
        for v in sorted_vertices:
            distance_val = all_distances[u][v]
            # Formata para inteiro se não houver parte decimal
            if distance_val == float('inf'):
                distances_list.append('inf')
            else:
                distances_list.append(str(int(distance_val) if distance_val.is_integer() else distance_val))

        distances_str = ",".join(distances_list)
        print(f"{u}:{distances_str}")

if __name__ == "__main__":
    main()
    # COMANDO PARA TESTAR: python EX1/A1_5.py EX1/fln_pequena.net