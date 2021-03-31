class Vertice():
    def __init__(self, chave):
        self.chave      = chave
        self.grau       = 0
        self.adjacentes = None
        self.anterior   = {}#Ex: {v1: [v2,v4]} = [anterior, proximo]
        self.marcado    = False

class Grafo_ListAdj():
    def __init__(self, numVert, direcionado = False):
        self.vetor = []
        self.qtdVertices = numVert
        self.qtdArestas  = 0
        self.direcionado = direcionado
        for i in range(numVert):
            #alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            #novoVert = Vertice(alfabeto[i])
            novoVert = Vertice(str(i))
            self.vetor.append(novoVert)

    def verificar_vertice(self, vertTemp):
        for v in self.vetor:
            if v.chave == vertTemp:
                return v
        return False

    def verificar_aresta(self, vertTemp, ref = None):
        vertTemp = vertTemp.split()
        v1 = self.verificar_vertice(vertTemp[0])
        v2 = self.verificar_vertice(vertTemp[1])
        achou = True
        if v1 == False or v2 == False:
            achou = False
        if achou and v1 in v2.anterior:
            if ref is None:
                print(True)
                return
            return True
        if ref is None:
            print(False)
            return
        return False

    def adicionarAdjacente(self, vertTemp):
        v1, v2 = vertTemp[0], vertTemp[1]
        if v1.adjacentes is None:
            v1.adjacentes = v2
            v1.grau += 1
            v2.anterior[v1] = [None, None]
        else:
            cont = 0
            vTemp = v1.adjacentes
            while cont < v1.grau:
                if vTemp.anterior[v1][1] is None:
                    vTemp.anterior[v1][1] = v2
                    v2.anterior[v1] = [vTemp, None]
                    v1.grau += 1
                    cont = v1.grau
                else:
                    vTemp = vTemp.anterior[v1][1]
                    cont += 1

    def inserir_aresta(self, vertices):
        vertTemp = vertices.split()
        vertTemp[0], vertTemp[1] = self.verificar_vertice(vertTemp[0]), self.verificar_vertice(vertTemp[1])
        if vertTemp[0] == False or vertTemp[1] == False:
            print('Erro: Vértice não encontrado')
            return
        existe = self.verificar_aresta(vertices, ref = 'ins_aresta')
        if not existe:
            self.qtdArestas += 1
            self.adicionarAdjacente(vertTemp)
            if not self.direcionado:
                if vertTemp[0] != vertTemp[1]:
                    vertTemp[0], vertTemp[1] = vertTemp[1], vertTemp[0]
                    self.adicionarAdjacente(vertTemp)
            print('Aresta Inserida')
        else:
            print('Erro: Aresta já existente')

    def vertices_adjacentes(self, vert):
        v = self.verificar_vertice(vert)
        if not v:
            print('Erro: Vértice não encontrado')
            return
        adj, cont, vTemp = '', 0, None
        while cont < v.grau:
            if cont == 0:
                adj += v.adjacentes.chave+' '
                vTemp = v.adjacentes
            else:
                adj += vTemp.anterior[v][1].chave+' '
                vTemp = vTemp.anterior[v][1]
            cont += 1
        print(f'{v.chave}: {adj}')

    def dfs(self, origem = None):
        if origem == None:
            origem = self.vetor[0]
        else:
            origem = self.verificar_vertice(origem)
            if type(origem) is bool and origem is False:
                return
        global ciclo
        ciclo = 'NÃO POSSUI CICLO'
        antecessor = {}
        for i in self.vetor:
            antecessor[i.chave] = -1
        self._dfs(origem, antecessor) #print antecessor
        for v in self.vetor:
            if v.marcado == False:
                self._dfs(v, antecessor)
        for vertices in self.vetor:
            vertices.marcado = False
        print(list(antecessor.values()))
        print(ciclo)
        del antecessor

    def _dfs(self, vertice, antecessor):
        vertice.marcado = True
        i = 1
        while i <= vertice.grau:
            if i == 1:
                if not vertice.adjacentes.marcado:
                    vTemp = vertice.adjacentes
                    antecessor[vTemp.chave] = vertice.chave
                    self._dfs(vTemp, antecessor)
                vTemp = vertice.adjacentes.anterior[vertice][1]
            else:
                if not vTemp.marcado:
                    antecessor[vTemp.chave] = vertice.chave
                    self._dfs(vTemp, antecessor)
                else:
                    global ciclo
                    ciclo = 'POSSUI CICLO(S)'
                vTemp = vTemp.anterior[vertice][1]
            i += 1

    def bfs(self):
        antecessor = {}
        for i in self.vetor:
            antecessor[i.chave] = -1
        self._bfs(self.vetor[0],antecessor)
        for vertices in self.vetor:
            vertices.marcado = False
        print(list(antecessor.values()))
        del antecessor

    def _bfs(self, vertice, antecessor):
        vertice.marcado = True
        i = 1
        while i <= vertice.grau:
            if i == 1:
                if not vertice.adjacentes.marcado:
                    vProx = vertice.adjacentes
                    vProx.marcado = True
                    antecessor[vProx.chave] = vertice.chave
                    vTemp = vProx.anterior[vertice][1]
                else:
                    i = vertice.grau
                    vProx = vertice.adjacentes.anterior[vertice][1]
                    if vProx is not None:
                        antecessor[vProx.chave] = vertice.chave
                    else:
                        return
            else:
                vTemp.chave
                vTemp.marcado = True
                antecessor[vTemp.chave] = vertice.chave
                vTemp = vTemp.anterior[vertice][1]
            i += 1
        self._bfs(vProx, antecessor)


g = Grafo_ListAdj(13)
g.inserir_aresta('0 1')
g.inserir_aresta('0 2')
g.inserir_aresta('0 5')
g.inserir_aresta('0 6')
g.inserir_aresta('3 4')
g.inserir_aresta('4 6')
g.inserir_aresta('5 3')
g.inserir_aresta('5 4')
g.inserir_aresta('7 8')
g.inserir_aresta('9 10')
g.inserir_aresta('9 11')
g.inserir_aresta('9 12')
g.inserir_aresta('11 12')
print('\n')
g.dfs()
g.bfs()



