"""
Atividade A3 - Exercício 3: Coloração de Vértices
Implementação de algoritmo de coloração de vértices usando abordagem gulosa (Lawler).
Encontra uma coloração válida e imprime o número mínimo de cores e a coloração de cada vértice.
"""

from graph_utils import UndirectedGraph
import sys


def coloracao_lawler(grafo):
    """
    Algoritmo de coloração de vértices usando abordagem gulosa (Lawler).
    Ordena vértices por grau decrescente e atribui a menor cor possível.
    
    Args:
        grafo: UndirectedGraph
    
    Returns:
        num_cores: número de cores utilizadas
        cores: dicionário mapeando vértice -> cor
    """
    # Inicializa o dicionário de cores
    cores = {}
    
    # Ordena vértices por grau decrescente (heurística gulosa)
    vertices = sorted(grafo.get_all_vertices(), 
                     key=lambda v: grafo.grau(v), 
                     reverse=True)
    
    for vertice in vertices:
        # Encontra as cores usadas pelos vizinhos
        cores_vizinhos = set()
        for vizinho in grafo.vizinhos(vertice):
            if vizinho in cores:
                cores_vizinhos.add(cores[vizinho])
        
        # Atribui a menor cor disponível (começando de 1)
        cor = 1
        while cor in cores_vizinhos:
            cor += 1
        
        cores[vertice] = cor
    
    # Número de cores usadas
    num_cores = max(cores.values()) if cores else 0
    
    return num_cores, cores


def verificar_coloracao(grafo, cores):
    """
    Verifica se a coloração é válida (vértices adjacentes têm cores diferentes).
    """
    for u in grafo.get_all_vertices():
        for v in grafo.vizinhos(u):
            if cores[u] == cores[v]:
                return False
    return True


def main():
    if len(sys.argv) < 2:
        print("Uso: python A3_3.py <arquivo_grafo>")
        print("Exemplo: python A3_3.py grafo_coloracao.txt")
        return
    
    arquivo = sys.argv[1]
    
    # Carrega o grafo não-dirigido
    grafo = UndirectedGraph()
    grafo.ler(arquivo)
    
    # Calcula a coloração usando algoritmo de Lawler
    num_cores, cores = coloracao_lawler(grafo)
    
    # Verifica se a coloração é válida
    if not verificar_coloracao(grafo, cores):
        print("Erro: Coloração inválida gerada!")
        return
    
    # Imprime o número de cores (primeira linha)
    print(num_cores)
    
    # Imprime a coloração de cada vértice (segunda linha)
    # Formato: cor1, cor2, cor3, ...
    vertices_ordenados = sorted(grafo.get_all_vertices())
    coloracao_str = ", ".join(str(cores[v]) for v in vertices_ordenados)
    print(coloracao_str)


if __name__ == "__main__":
    # TESTE: python A3_3.py test_coloracao.net
    main()
