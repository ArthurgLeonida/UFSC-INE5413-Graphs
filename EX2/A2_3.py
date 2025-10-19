from graph_utils import UndirectedGraph, UnionFind
import sys

def Kruskal(G):
    """
    Input: um grafo G = (V, E, w)
    
    Retorna: A - conjunto de arestas da árvore geradora mínima
    """
    A = []
    
    # Inicializa a estrutura Union-Find com todos os vértices do grafo
    dsu = UnionFind(G.get_all_vertices())
    
    # lista de arestas ordenadas por ordem crescente de peso
    E_prime = sorted(G.edges, key=lambda edge: (edge[2], edge[0], edge[1]))
    
    # Itera sobre as arestas ordenadas
    for u, v, w in E_prime:
        # Se u e v não estão no mesmo conjunto (não formam ciclo)
        # a função dsu.uniao retorna True e une os conjuntos.
        if dsu.uniao(u, v):
            # Adiciona a aresta à Árvore Geradora Mínima
            A.append((u, v, w))

    return A

def calcular_peso_total(A):
    """
    Calcula o peso total das arestas na MST.
    """
    return sum(w for u, v, w in A)


def print_mst(A):
    """
    Imprime a árvore geradora mínima no formato especificado.
    """
    total_weight = calcular_peso_total(A)
    print(f"{total_weight:.1f}")
    
    edge_strings = []
    for u, v, weight in A:
        if u < v:
            edge_strings.append(f"{u}-{v}")
        else:
            edge_strings.append(f"{v}-{u}")
    
    print(', '.join(edge_strings))


def main():
    if len(sys.argv) < 2:
        print("Uso: python A2_3.py <arquivo_grafo>")
        return
    
    arquivo = sys.argv[1]
    
    graph = UndirectedGraph()
    graph.ler(arquivo)
    
    if graph.qtdVertices() == 0:
        print("Erro: O grafo está vazio.")
        return
    
    if graph.qtdArestas() < graph.qtdVertices() - 1:
        print("Aviso: O grafo pode não ser conexo.")
    
    A = Kruskal(graph)
    
    if len(A) < graph.qtdVertices() - 1:
        print("Erro: O grafo não é conexo. Não é possível encontrar uma MST que cubra todos os vértices.")
        return
    
    print_mst(A)

if __name__ == "__main__":
    # TESTE: python .\EX2\A2_3.py .\EX2\test_mst_example.net
    main()
