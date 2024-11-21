class Grafo:
    def __init__(self, n):
        self.n = n
        self.m = 0
        self.adj = [[0 for _ in range(n)] for _ in range(n)]

    def insereA(self, v, w):
        if self.adj[v][w] == 0:
            self.adj[v][w] = 1
            self.m += 1

    def removeA(self, v, w):
        if self.adj[v][w] == 1:
            self.adj[v][w] = 0
            self.m -= 1

    def showMin(self):
        print("\nMatriz de adjacência:")
        for i in range(self.n):
            print(" ".join(map(str, self.adj[i])))

    def conexidade(self):
        # Verificar se o grafo é conexo (não direcionado)
        visitados = [False] * self.n

        def dfs(v):
            visitados[v] = True
            for w in range(self.n):
                if self.adj[v][w] and not visitados[w]:
                    dfs(w)

        dfs(0)
        conexo = all(visitados)

        # Verificar componentes fortemente conexas para grafos direcionados
        def transpor():
            transposto = Grafo(self.n)
            for i in range(self.n):
                for j in range(self.n):
                    if self.adj[i][j]:
                        transposto.insereA(j, i)
            return transposto

        def kosaraju():
            ordem = []
            visitados[:] = [False] * self.n

            def dfs_ordem(v):
                visitados[v] = True
                for w in range(self.n):
                    if self.adj[v][w] and not visitados[w]:
                        dfs_ordem(w)
                ordem.append(v)

            def dfs_transposto(v):
                visitados[v] = True
                for w in range(self.n):
                    if transposto.adj[v][w] and not visitados[w]:
                        dfs_transposto(w)

            for v in range(self.n):
                if not visitados[v]:
                    dfs_ordem(v)

            transposto = transpor()
            visitados[:] = [False] * self.n
            componentes = 0

            while ordem:
                v = ordem.pop()
                if not visitados[v]:
                    dfs_transposto(v)
                    componentes += 1

            return componentes

        componentes = kosaraju()

        if conexo:
            print("O grafo é conexo.")
        else:
            print("O grafo não é conexo.")

        print(f"O grafo tem {componentes} componentes fortemente conexas.")

        if componentes > 1:
            print("Grafo reduzido:")
            transposto = transpor()
            transposto.showMin()

    def graus(self):
        graus_entrada = [0] * self.n
        graus_saida = [0] * self.n

        for i in range(self.n):
            for j in range(self.n):
                if self.adj[i][j]:
                    graus_saida[i] += 1
                    graus_entrada[j] += 1

        print("Graus de entrada:", graus_entrada)
        print("Graus de saída:", graus_saida)

    def euleriano(self):
        graus_impares = 0
        for i in range(self.n):
            grau = sum(self.adj[i]) + sum(self.adj[j][i] for j in range(self.n))
            if grau % 2 != 0:
                graus_impares += 1

        if graus_impares == 0:
            print("O grafo é Euleriano.")
        elif graus_impares == 2:
            print("O grafo possui um caminho Euleriano.")
        else:
            print("O grafo não é Euleriano.")

    def hamiltoniano(self):
        def ciclo_hamiltoniano(v, visitados, caminho):
            if len(caminho) == self.n:
                return caminho[0] in [w for w in range(self.n) if self.adj[v][w]]

            for w in range(self.n):
                if self.adj[v][w] and not visitados[w]:
                    visitados[w] = True
                    caminho.append(w)
                    if ciclo_hamiltoniano(w, visitados, caminho):
                        return True
                    visitados[w] = False
                    caminho.pop()
            return False

        for v in range(self.n):
            visitados = [False] * self.n
            visitados[v] = True
            caminho = [v]
            if ciclo_hamiltoniano(v, visitados, caminho):
                print("O grafo possui um ciclo Hamiltoniano.")
                return
        print("O grafo não possui um ciclo Hamiltoniano.")


def carregar_grafo(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        tipo = int(f.readline().strip())
        n_vertices = int(f.readline().strip())
        grafo = Grafo(n_vertices)
        vertices = {}
        # Ler vértices
        for _ in range(n_vertices):
            linha = f.readline().strip()
            if linha:  # Verifica se a linha não está vazia
                partes = linha.split()
                if len(partes) >= 2:  # Certifique-se de que há pelo menos dois elementos
                    id_vertice = int(partes[0])
                    nome = " ".join(partes[1:])
                    vertices[id_vertice] = nome

        # Ler arestas
        for linha in f:
            linha = linha.strip()
            if linha:  # Verifica se a linha não está vazia
                partes = linha.split()
                if len(partes) == 3:  # Certifique-se de que há exatamente três elementos
                    v1, v2, peso = map(float, partes)  # Tenta converter para float/int
                    grafo.insereA(int(v1), int(v2))
    return grafo, vertices

def salvar_grafo(arquivo, grafo, vertices):
    with open(arquivo, "w", encoding="utf-8") as f:
        f.write("2\n")
        f.write(f"{len(vertices)}\n")
        for id_vertice, nome in vertices.items():
            f.write(f"{id_vertice} \"{nome}\"\n")
        for i in range(grafo.n):
            for j in range(grafo.n):
                if grafo.adj[i][j]:
                    f.write(f"{i} {j} {grafo.adj[i][j]}\n")

def menu():
    print("\nMenu:")
    print("a) Ler dados do arquivo grafo.txt")
    print("b) Gravar dados no arquivo grafo.txt")
    print("c) Inserir vértice")
    print("d) Inserir aresta")
    print("e) Remover vértice")
    print("f) Remover aresta")
    print("g) Mostrar conteúdo do arquivo")
    print("h) Mostrar grafo")
    print("i) Apresentar conexidade do grafo e o reduzido")
    print("j) Verificar Eulerianidade")
    print("k) Verificar ciclo Hamiltoniano")
    print("l) Determinar graus de entrada e saída")
    print("m) Encerrar a aplicação")

def main():
    arquivo = "grafo.txt"
    grafo = None
    vertices = {}

    while True:
        menu()
        opcao = input("Escolha uma opção: ").lower()

        if opcao == "a":
            grafo, vertices = carregar_grafo(arquivo)
            print("Grafo carregado com sucesso!")
        elif opcao == "b":
            if grafo and vertices:
                salvar_grafo(arquivo, grafo, vertices)
                print("Grafo salvo com sucesso!")
            else:
                print("Nenhum grafo carregado para salvar.")
        elif opcao == "c":
            if grafo:
                nome = input("Nome do vértice: ")
                id_vertice = len(vertices)
                vertices[id_vertice] = nome
                grafo.n += 1
                print(f"Vértice '{nome}' adicionado com sucesso!")
            else:
                print("Carregue o grafo antes de adicionar vértices.")
        elif opcao == "d":
            if grafo:
                v1 = int(input("ID do vértice de origem: "))
                v2 = int(input("ID do vértice de destino: "))
                grafo.insereA(v1, v2)
                print("Aresta adicionada com sucesso!")
            else:
                print("Carregue o grafo antes de adicionar arestas.")
        elif opcao == "e":
            if grafo:
                id_vertice = int(input("ID do vértice a remover: "))
                if id_vertice in vertices:
                    del vertices[id_vertice]
                    for i in range(grafo.n):
                        grafo.removeA(i, id_vertice)
                        grafo.removeA(id_vertice, i)
                    print("Vértice removido com sucesso!")
                else:
                    print("Vértice não encontrado.")
            else:
                print("Carregue o grafo antes de remover vértices.")
        elif opcao == "f":
            if grafo:
                v1 = int(input("ID do vértice de origem: "))
                v2 = int(input("ID do vértice de destino: "))
                grafo.removeA(v1, v2)
                print("Aresta removida com sucesso!")
            else:
                print("Carregue o grafo antes de remover arestas.")
        elif opcao == "g":
            with open(arquivo, "r", encoding="utf-8") as f:
                print(f.read())
        elif opcao == "h":
            if grafo:
                grafo.showMin()
            else:
                print("Carregue o grafo antes de exibi-lo.")
        elif opcao == "i":
            if grafo:
                grafo.conexidade()
            else:
                print("Carregue o grafo antes de verificar a conexidade.")
        elif opcao == "j":
            if grafo:
                grafo.euleriano()
            else:
                print("Carregue o grafo antes de verificar a Eulerianidade.")
        elif opcao == "k":
            if grafo:
                grafo.hamiltoniano()
            else:
                print("Carregue o grafo antes de verificar ciclos Hamiltonianos.")
        elif opcao == "l":
            if grafo:
                grafo.graus()
            else:
                print("Carregue o grafo antes de verificar graus.")
        elif opcao == "m":
            print("Encerrando a aplicação.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
