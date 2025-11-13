"""
Atividade A3 - Exercício 1: Algoritmo de Edmonds-Karp
Implementação do algoritmo de Edmonds-Karp para encontrar o fluxo máximo em um grafo dirigido.
Baseado no algoritmo de Ford-Fulkerson usando BFS para encontrar caminhos aumentantes.
"""
from graph_utils import DirectedWeightedGraph
from collections import deque
import sys


def bfs_caminho_aumentante(grafo, origem, destino, pai, fluxo_residual):
    """
    BFS para encontrar um caminho aumentante da origem ao destino.
    Retorna True se existe caminho, False caso contrário.
    Armazena o caminho no dicionário pai.
    """
    visitados = set()
    fila = deque([origem])
    visitados.add(origem)
    
    while fila:
        u = fila.popleft()
        
        # Examina todos os vizinhos
        for v, _ in grafo.adjacency_list[u]:
            # Se não foi visitado e há capacidade residual
            if v not in visitados and fluxo_residual[(u, v)] > 0:
                visitados.add(v)
                pai[v] = u
                
                if v == destino:
                    return True
                
                fila.append(v)
    
    return False


def edmonds_karp(grafo, origem, destino):
    """
    Algoritmo de Edmonds-Karp para encontrar o fluxo máximo.
    
    Args:
        grafo: DirectedWeightedGraph com capacidades
        origem: vértice de origem
        destino: vértice de destino
    
    Returns:
        max_flow: valor do fluxo máximo
    """
    # Inicializa o grafo residual com as capacidades originais
    fluxo_residual = {}
    
    # Para cada aresta no grafo original
    for u in grafo.get_all_vertices():
        for v, cap in grafo.adjacency_list[u]:
            fluxo_residual[(u, v)] = cap
            # Aresta reversa (inicialmente 0)
            if (v, u) not in fluxo_residual:
                fluxo_residual[(v, u)] = 0
    
    # Adiciona arestas reversas ao grafo se não existirem
    for u in grafo.get_all_vertices():
        for v, _ in list(grafo.adjacency_list[u]):
            # Verifica se existe aresta reversa
            existe_reversa = False
            for vizinho, _ in grafo.adjacency_list[v]:
                if vizinho == u:
                    existe_reversa = True
                    break
            
            if not existe_reversa:
                grafo.adjacency_list[v].append((u, 0))
    
    pai = {}
    fluxo_maximo = 0
    
    # Enquanto existe caminho aumentante
    while bfs_caminho_aumentante(grafo, origem, destino, pai, fluxo_residual):
        # Encontra a capacidade mínima no caminho
        fluxo_caminho = float('inf')
        v = destino
        
        while v != origem:
            u = pai[v]
            fluxo_caminho = min(fluxo_caminho, fluxo_residual[(u, v)])
            v = u
        
        # Atualiza as capacidades residuais
        v = destino
        while v != origem:
            u = pai[v]
            fluxo_residual[(u, v)] -= fluxo_caminho
            fluxo_residual[(v, u)] += fluxo_caminho
            v = u
        
        fluxo_maximo += fluxo_caminho
        pai.clear()
    
    return fluxo_maximo


def main():
    if len(sys.argv) < 4:
        print("Uso: python A3_1.py <arquivo_grafo> <origem> <destino>")
        print("Exemplo: python A3_1.py grafo_fluxo.txt 1 6")
        return
    
    arquivo = sys.argv[1]
    origem = int(sys.argv[2])
    destino = int(sys.argv[3])
    
    # Carrega o grafo dirigido ponderado
    grafo = DirectedWeightedGraph()
    grafo.ler(arquivo)
    
    # Calcula o fluxo máximo usando Edmonds-Karp
    fluxo_maximo = edmonds_karp(grafo, origem, destino)
    
    # Imprime o resultado
    print(fluxo_maximo)


if __name__ == "__main__":
    # TESTE: python A3_1.py test_fluxo.net 1 6
    main()
