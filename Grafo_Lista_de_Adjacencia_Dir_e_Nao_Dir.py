class Vertice():
    def __init__(self, chave):
        self.chave      = chave
        self.grau       = 0
        self.adjacentes = None
        self.anterior   = {} #Ex: {v1: [v2,v4]} = [anterior, proximo]
        self.pesos      = {} #Ex: {v2: 10, v4: 5}
        self.marcado    = False

class Grafo_ListAdj():
    def __init__(self, numVert, ponderado = False, direcionado = False):
        self.vetor = []
        self.qtdVertices = numVert
        self.qtdArestas  = 0
        self.ponderado   = ponderado
        self.direcionado = direcionado
        for i in range(numVert):
            alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            novoVert = Vertice(alfabeto[i])
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
        
    def inserir_aresta(self, vertices, peso = None):
        if peso is not None and not self.ponderado:
            print('Erro: Grafo não é ponderado')
            return
        elif peso is None and self.ponderado:
            print('Erro: Grafo é ponderado')
            return
        elif self.ponderado and peso < 0:
            print('Erro: O Algoritmo de Dijkstra não permite pesos negativos')
            return
        vertTemp = vertices.split()
        vertTemp[0], vertTemp[1] = self.verificar_vertice(vertTemp[0]), self.verificar_vertice(vertTemp[1])
        if vertTemp[0] == False or vertTemp[1] == False:
            print('Erro: Vértice não encontrado')
            return
        existe = self.verificar_aresta(vertices, ref = 'ins_aresta')
        if not existe:
            vertTemp[0].pesos[vertTemp[1]] = peso
            self.qtdArestas += 1
            self.adicionarAdjacente(vertTemp)
            if not self.direcionado:
                if vertTemp[0] != vertTemp[1]:
                    vertTemp[1].pesos[vertTemp[0]] = peso
                    vertTemp[0], vertTemp[1] = vertTemp[1], vertTemp[0]
                    self.adicionarAdjacente(vertTemp)
            print('Aresta Inserida')
        else:
            print('Erro: Aresta já existente')

    def remover_aresta(self, vertices, ref = None):
        vertTemp = vertices.split()
        vertTemp[0] = self.verificar_vertice(vertTemp[0])
        vertTemp[1] = self.verificar_vertice(vertTemp[1])
        if not vertTemp[0] or not vertTemp[1]:
            print('Erro: Aresta não encontrada')
        else:
            v1, v2 = vertTemp[0], vertTemp[1]
            vTemp  = v1.adjacentes
            cont   = 0
            while cont < v1.grau:
                if vTemp == v2:
                    if cont == 0:
                        v1.adjacentes = vTemp.anterior[v1][1]
                        del vTemp.anterior[v1]
                    else:
                        if vTemp.anterior[v1][1] is not None:
                            vTemp.anterior[v1][0].anterior[v1][1] = vTemp.anterior[v1][1]
                            vTemp.anterior[v1][1].anterior[v1][0] = vTemp.anterior[v1][0]
                        else:
                            vTemp.anterior[v1][0].anterior[v1][1] = None
                        del vTemp.anterior[v1]
                    cont = v1.grau+1
                else:
                    vTemp = vTemp.anterior[v1][1]
                    cont += 1
            if cont == v1.grau:
                print('Erro: Aresta não encontrada')
            else:
                self.qtdArestas -= 1
                v1.grau -= 1
                del v1.pesos[v2]
                if ref is None:
                    print('Aresta Removida')
                    if not self.direcionado:
                        vertices = vertices.split()
                        if vertices[0] == vertices[1]:
                            return
                        vertices = vertices[1]+' '+vertices[0]
                        self.remover_aresta(vertices, ref = 'dir')
                    
    def qtd_vertices_arestas(self):
        print(f'Quantidade de vértices: {self.qtdVertices}\nQuantidade de arestas: {self.qtdArestas}')

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
        
    def imprimir_grafo(self):
        for v in self.vetor:
            adj, cont, vTemp = '', 0, None
            while cont < v.grau:
                if cont == 0:
                    adj += v.adjacentes.chave+f'[{v.pesos[v.adjacentes]}]'+' '
                    vTemp = v.adjacentes
                else:
                    adj += vTemp.anterior[v][1].chave+f'[{v.pesos[vTemp.anterior[v][1]]}]'+' '
                    vTemp = vTemp.anterior[v][1]
                cont += 1
            print(f'{v.chave}\t grau: {v.grau}\t adjacentes: {adj}')

    def menor_aresta(self):
        if not self.ponderado:
            print('Erro: Grafo não é ponderado')
            return
        menor = [10**5, []]
        for v in self.vetor:
            for vTemp in v.pesos:
                if v.pesos[vTemp] < menor[0]:
                    menor[0] = v.pesos[vTemp]
                    menor[1] = [v, vTemp]
        print(f'Menor aresta: {menor[1][0].chave} {menor[1][1].chave}\nPeso: {menor[0]}')

    def dfs(self):
        antecessor = {}
        for i in self.vetor:
            antecessor[i.chave] = -1
        self._dfs(self.vetor[0], antecessor)
        for vertices in self.vetor:
            vertices.marcado = False
        antecessorTemp = [None] * len(antecessor)
        cont = 0
        for n in antecessor:
            antecessorTemp[cont] = antecessor[n]
            cont += 1
        print(antecessorTemp)
        del antecessor
        del antecessorTemp
        del cont

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
                    vTemp = vertice.adjacentes.anterior[vertice][1]
            else:
                if not vTemp.marcado:
                    antecessor[vTemp.chave] = vertice.chave
                    self._dfs(vTemp, antecessor)
                    vTemp = vTemp.anterior[vertice][1]
                else:
                    vTemp = vTemp.anterior[vertice][1]
            i += 1

    def bfs(self):
        antecessor = {}
        for i in self.vetor:
            antecessor[i.chave] = -1
        self._bfs(self.vetor[0],antecessor)
        for vertices in self.vetor:
            vertices.marcado = False
        antecessorTemp = [None]*len(antecessor)
        cont = 0
        for n in antecessor:
            antecessorTemp[cont] = antecessor[n]
            cont +=1
        print(antecessorTemp)
        del antecessor
        del antecessorTemp
        del cont

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

    def relaxamento(self, v1, v2, peso, infoVertices):
        if infoVertices[v2][1] > infoVertices[v1][1]+peso:
            infoVertices[v2][0] = v1
            infoVertices[v2][1] = infoVertices[v1][1]+peso

    def menor_caminho(self, vertice):
        vertice = self.verificar_vertice(vertice)
        global vInicial
        vInicial = str(vertice.chave)
        if type(vertice) is bool and not vertice:
            print('ERRO: Vértice não encontrado')
            return
        caminho      = [vertice.chave]
        infoVertices = {}
        contMarcado  = 0
        i            = 1
        vProx        = [None, 10**8]
        for v in self.vetor:
            if v == vertice:
                infoVertices[v] = [-1, 0, True]
            else:
                infoVertices[v] = [-1, 10**8, False] #[antecessor, peso, marcado]
        contErro = 0
        
        while i <= vertice.grau and contErro < 10:
            print(caminho)
            if i == 1:
                if vertice.adjacentes.chave != vInicial:
                    vAdj = vertice.adjacentes
                    peso = vertice.pesos[vAdj]
                    print(f'\ni: {i}\nV: {vertice.chave}\nVdj: {vAdj.chave}\nPeso (V,vAdj) : {peso}\n')
                    self.relaxamento(vertice, vAdj, peso, infoVertices)
                else:
                    vAdj = vertice.adjacentes.anterior[vertice][1]
                    peso = vertice.pesos[vAdj]
                    self.relaxamento(vertice, vAdj, peso, infoVertices)
                    i += 1
            else:
                if vAdj.anterior[vertice][1].chave != vInicial:
                    vAdj = vAdj.anterior[vertice][1]
                    peso = vertice.pesos[vAdj]
                    self.relaxamento(vertice, vAdj, peso, infoVertices)
                    print(f'\ni:{i}\nV: {vertice.chave}\nVdj: {vAdj.chave}\nPeso (V,vAdj) : {peso}\n')
                else:
                    vAdj = vAdj.anterior[vertice][1]
                    vAdj = vAdj.anterior[vertice][1]
                    peso = vertice.pesos[vAdj]
                    self.relaxamento(vertice, vAdj, peso, infoVertices)
                    i += 1
                    

            if infoVertices[vAdj][1] < vProx[1]:
                vProx = [vAdj, infoVertices[vAdj][1]]
            i += 1
            contErro+= 1

            print(f'Novo Peso vAdj: {infoVertices[vAdj][1]}\nPeso vProx: {vProx[1]}')
            if vProx[0] is not None:
                print(f'vProx: {vProx[0].chave}')
            else:
                print(f'vProx: None')
                
            if i > vertice.grau:
                if vProx[0].chave == 'A':
                    print('Vprox é A')
                if vProx[0].chave not in caminho:
                    caminho.append(vProx[0].chave)
                    vertice, i = vProx[0], 1
                    infoVertices[vertice][2] = True
                    vProx = [None, 10**8]

        print('-'*80+'\n',caminho, 'fim')
        for i in infoVertices:
            print(infoVertices[i][1])



g = Grafo_ListAdj(5, True, True)
g.inserir_aresta('A B', 10)
g.inserir_aresta('A C', 5)
g.inserir_aresta('B C', 2)
g.inserir_aresta('B D', 1)
g.inserir_aresta('C B', 3)
g.inserir_aresta('C D', 9)
g.inserir_aresta('C E', 2)
g.inserir_aresta('D E', 4)
g.inserir_aresta('E A', 7)
g.inserir_aresta('E D', 6)
g.imprimir_grafo()
print('\n')
g.menor_caminho('A')

