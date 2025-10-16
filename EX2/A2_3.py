"""
Atividade A2 - Exercício 3: Árvore Geradora Mínima
Algoritmo 23: Algoritmo de Kruskal
Baseado no pseudocódigo para encontrar a árvore geradora mínima em grafos não-dirigidos ponderados.
"""

from graph_utils import UndirectedGraph
import sys


def Kruskal(G):
    """
    Algoritmo 23: Algoritmo de Kruskal
    
    Input: um grafo G = (V, E, w)
    
    Retorna: A - conjunto de arestas da árvore geradora mínima
    """
    # 1. A ← {}
    A = []
    
    # 2. S ← vetor de |V| elementos vazios
    S = {}
    
    # 3. foreach v ∈ V do
    for v in G.get_all_vertices():
        # 4. S_v ← {v}
        S[v] = {v}
    
    # 5. E' ← lista de arestas ordenadas por ordem crescente de peso
    E_prime = sorted(G.edges, key=lambda edge: (edge[2], edge[0], edge[1]))
    
    # 6. foreach {u, v} ∈ E' do
    for u, v, w in E_prime:
        # 7. if S_u ≠ S_v then
        if S[u] != S[v]:
            # 8. A ← A ∪ {{u, v}}
            A.append((u, v, w))
            
            # 9. x ← S_u ∪ S_v
            x = S[u] | S[v]
            
            # 10. foreach y ∈ x do
            for y in x:
                # 11. S_y ← x
                S[y] = x
    
    # 12. return A
    return A


def calcular_peso_total(A):
    """
    Calcula o peso total das arestas na MST.
    """
    return sum(w for u, v, w in A)


def print_mst(A):
    """
    Imprime a árvore geradora mínima no formato especificado.
    Primeira linha: peso total
    Linhas seguintes: arestas no formato "u-v"
    """
    total_weight = calcular_peso_total(A)
    print(f"{total_weight:.1f}")
    
    # Imprime as arestas
    edge_strings = []
    for u, v, weight in A:
        # Garante que a aresta seja impressa na ordem correta (menor-maior)
        if u < v:
            edge_strings.append(f"{u}-{v}")
        else:
            edge_strings.append(f"{v}-{u}")
    
    print(', '.join(edge_strings))


def main():
    if len(sys.argv) < 2:
        print("Uso: python A2_3.py <arquivo_grafo>")
        print("Exemplo: python A2_3.py grafo_ponderado.txt")
        return
    
    arquivo = sys.argv[1]
    
    # Carrega o grafo não-dirigido ponderado
    graph = UndirectedGraph()
    graph.ler(arquivo)
    
    # Verifica se o grafo está vazio
    if graph.qtdVertices() == 0:
        print("Erro: O grafo está vazio.")
        return
    
    # Verifica se o grafo é conexo (simples verificação)
    if graph.qtdArestas() < graph.qtdVertices() - 1:
        print("Aviso: O grafo pode não ser conexo.")
    
    # Encontra a árvore geradora mínima usando o Algoritmo de Kruskal
    A = Kruskal(graph)
    
    # Verifica se conseguimos encontrar uma MST completa
    if len(A) < graph.qtdVertices() - 1:
        print("Erro: O grafo não é conexo. Não é possível encontrar uma MST que cubra todos os vértices.")
        return
    
    # Imprime o resultado
    print_mst(A)


if __name__ == "__main__":
    main()
