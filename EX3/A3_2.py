"""
Atividade A3 - Exercício 2: Algoritmo de Hopcroft-Karp
Implementação do algoritmo de Hopcroft-Karp para encontrar o emparelhamento máximo 
em um grafo bipartido não-dirigido e não-ponderado.
"""

from graph_utils import BipartiteGraph
from collections import deque
import sys


def bfs_hopcroft_karp(grafo, pair_U, pair_V, dist, NIL):
    """
    BFS para construir níveis no grafo de emparelhamento.
    Retorna True se existe um caminho aumentante.
    """
    fila = deque()
    
    # Adiciona todos os vértices livres de U à fila
    for u in grafo.partition1:
        if pair_U[u] == NIL:
            dist[u] = 0
            fila.append(u)
        else:
            dist[u] = float('inf')
    
    dist[NIL] = float('inf')
    
    while fila:
        u = fila.popleft()
        
        if dist[u] < dist[NIL]:
            for v in grafo.vizinhos(u):
                if dist[pair_V[v]] == float('inf'):
                    dist[pair_V[v]] = dist[u] + 1
                    fila.append(pair_V[v])
    
    return dist[NIL] != float('inf')


def dfs_hopcroft_karp(grafo, u, pair_U, pair_V, dist, NIL):
    """
    DFS para encontrar caminho aumentante a partir de u.
    Retorna True se encontrou caminho aumentante.
    """
    if u != NIL:
        for v in grafo.vizinhos(u):
            if dist[pair_V[v]] == dist[u] + 1:
                if dfs_hopcroft_karp(grafo, pair_V[v], pair_U, pair_V, dist, NIL):
                    pair_V[v] = u
                    pair_U[u] = v
                    return True
        
        dist[u] = float('inf')
        return False
    
    return True


def hopcroft_karp(grafo):
    """
    Algoritmo de Hopcroft-Karp para encontrar emparelhamento máximo.
    
    Args:
        grafo: BipartiteGraph com duas partições definidas
    
    Returns:
        matching: número de arestas no emparelhamento máximo
        pairs: dicionário com os pares do emparelhamento
    """
    # NIL representa vértice nulo
    NIL = 0
    
    # Inicializa os emparelhamentos
    pair_U = {u: NIL for u in grafo.partition1}
    pair_V = {v: NIL for v in grafo.partition2}
    pair_U[NIL] = NIL
    pair_V[NIL] = NIL
    
    # Inicializa distâncias
    dist = {}
    
    matching = 0
    
    # Enquanto existe caminho aumentante
    while bfs_hopcroft_karp(grafo, pair_U, pair_V, dist, NIL):
        for u in grafo.partition1:
            if pair_U[u] == NIL:
                if dfs_hopcroft_karp(grafo, u, pair_U, pair_V, dist, NIL):
                    matching += 1
    
    return matching, pair_U


def detectar_biparticao(grafo):
    """
    Detecta se o grafo é bipartido e retorna as duas partições.
    Usa coloração com BFS.
    """
    cor = {}
    partition1 = []
    partition2 = []
    
    vertices = grafo.get_all_vertices()
    
    for start in vertices:
        if start in cor:
            continue
        
        fila = deque([start])
        cor[start] = 0
        
        while fila:
            u = fila.popleft()
            
            for v in grafo.vizinhos(u):
                if v not in cor:
                    cor[v] = 1 - cor[u]
                    fila.append(v)
                elif cor[v] == cor[u]:
                    return None, None  # Não é bipartido
    
    for v in vertices:
        if cor[v] == 0:
            partition1.append(v)
        else:
            partition2.append(v)
    
    return partition1, partition2


def main():
    if len(sys.argv) < 2:
        print("Uso: python A3_2.py <arquivo_grafo>")
        print("Exemplo: python A3_2.py grafo_bipartido.txt")
        return
    
    arquivo = sys.argv[1]
    
    # Carrega o grafo
    grafo = BipartiteGraph()
    grafo.ler(arquivo)
    
    # Detecta a bipartição
    partition1, partition2 = detectar_biparticao(grafo)
    
    if partition1 is None:
        print("Erro: O grafo não é bipartido.")
        return
    
    grafo.set_bipartition(partition1, partition2)
    
    # Calcula o emparelhamento máximo usando Hopcroft-Karp
    max_matching, pairs = hopcroft_karp(grafo)
    
    # Imprime o resultado: valor do emparelhamento máximo
    print(max_matching)
    
    # Imprime as arestas do emparelhamento (segunda linha)
    edges = []
    for u in sorted(grafo.partition1):
        v = pairs[u]
        if v != 0:  # NIL = 0
            # Garante ordem crescente
            if u < v:
                edges.append(f"{u}-{v}")
            else:
                edges.append(f"{v}-{u}")
    
    if edges:
        print(", ".join(edges))


if __name__ == "__main__":
    # TESTE: python A3_2.py test_bipartido.net
    main()
