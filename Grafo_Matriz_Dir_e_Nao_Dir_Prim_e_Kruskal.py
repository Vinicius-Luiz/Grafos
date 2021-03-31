def main():
    class Grafo_Matriz():
        def __init__(self, numVert, ponderado = False, direcionado = False):
            self.vertices     = numVert
            self.arestas      = 0
            self.matriz       = []
            self.legenda      = {}
            self.ponderado    = ponderado
            self.direcionado  = direcionado
            nomes = []
            for n in qtdVertices.keys():
                nomes.append(n)
            if self.direcionado:
                for i in range(numVert):
                    m = [None]*numVert
                    self.matriz.append(m)
                    self.legenda[i] = [nomes[i],[]]
            else:
                cont = numVert
                for i in range(numVert):
                    m    = [None]*cont
                    self.matriz.append(m)
                    self.legenda[i] = [nomes[i],[]]
                    cont -= 1
                del cont

        def imprimir_grafo(self):
            cont = 0
            numVert = self.vertices
            while cont < numVert:
                print(self.legenda[cont][0], self.matriz[cont])
                cont += 1

        def aux_iTemp(self, vert):
            for t in self.legenda:
                if self.legenda[t][0] == vert:
                    iTemp = t
                    return iTemp
            return False

        def verificar_peso(self, v1, v2):
            if self.direcionado:
                peso = self.matriz[v1][v2]
            else:
                min_i, max_i = min([v1,v2]), max([v1,v2])
                peso = self.matriz[min_i][max_i - min_i]
            return peso

        def inserir_aresta(self, v1, v2, peso = None):
            ref = 0
            vertTemp = [v1,v2]
            for t in self.legenda:
                if vertTemp[0] == self.legenda[t][0]:
                    vertTemp[0] = t
                    ref += 1
                if vertTemp[1] == self.legenda[t][0]:
                    vertTemp[1] = t
                    ref += 1
                if ref == 2:
                    break
                
            if type(vertTemp[0]) is str or type(vertTemp[1]) is str:
                return
            else:
                if not self.direcionado:
                    min_i, max_i = min(vertTemp), max(vertTemp)
                else:
                    origem, destino = vertTemp[0], vertTemp[1]
                if peso is None:
                    if self.ponderado:
                        return
                    else:
                        if not self.direcionado:
                            if self.matriz[min_i][max_i-min_i] is None:
                                self.arestas += 1
                                self.legenda[min_i][1].append(self.legenda[max_i][0])
                                if self.legenda[min_i][0] != self.legenda[max_i][0]:
                                    self.legenda[max_i][1].append(self.legenda[min_i][0])
                            self.matriz[min_i][max_i - min_i] = 1
                        else:
                            if self.matriz[origem][destino] is None:
                                self.arestas += 1
                                self.legenda[origem][1].append(self.legenda[destino][0])
                            self.matriz[origem][destino] = 1
                else:
                    if not self.ponderado:
                        return
                    else:
                        if not self.direcionado:
                            if self.matriz[min_i][max_i-min_i] is None:
                                self.arestas += 1
                                self.legenda[min_i][1].append(self.legenda[max_i][0])
                                self.legenda[max_i][1].append(self.legenda[min_i][0])
                            self.matriz[min_i][max_i - min_i] = peso
                        else:
                            if self.matriz[origem][destino] is None:
                                self.arestas += 1
                                self.legenda[origem][1].append(self.legenda[destino][0])
                            self.matriz[origem][destino] = peso

        def prim(self):
            global inf
            inf     = 10**6
            global rotulos
            rotulos = {}
            iVert = 0
            listAdjacentes = []
            S = []
            for i in range(self.vertices):
                rotulos[i] = inf
            rotulos[0] = 0

            while len(S) < self.vertices-1:
                adjs = self.legenda[iVert][1]
                (v1, v2, p) = self.selecionarAresta(iVert, adjs, listAdjacentes, 'prim')
                S.append((v1, v2, p))
                rotulos[v2] = p
                iVert = v2

            menorCaminho = 0
            for caminho in S:
                menorCaminho += caminho[2]
            print(menorCaminho)
            del rotulos
            del listAdjacentes

        def kruskal(self):
            global inf
            inf = 10**6
            listAdjacentes = []
            for c in self.legenda.keys():
                v1 = c
                adjs = self.legenda[v1][1]
                for adj in adjs:
                    adj = self.aux_iTemp(adj)
                    p = self.verificar_peso(v1, adj)
                    if (adj, v1, p) not in listAdjacentes:
                        listAdjacentes.append((v1, adj, p))

            global adjacentes
            adjacentes = {}
            for i in range(self.vertices):
                adjacentes[i] = []
            S = []
            while len(S) < self.vertices-1:
                v1, v2, p = self.selecionarAresta(None, None, listAdjacentes, 'kruskal')
                S.append((v1,v2,p))
                adjacentes[v1].append(v2), adjacentes[v2].append(v1)
            menorCaminho = 0
            for caminho in S:
                menorCaminho += caminho[2]
            print(menorCaminho)
            del adjacentes
            del listAdjacentes

        def selecionarAresta(self, iVert, adjs, listAdjacentes, referencia):
            if referencia == 'prim':
                for adj in adjs:
                    adj = self.aux_iTemp(adj)
                    if rotulos[adj] == inf:
                        peso = self.verificar_peso(iVert, adj)
                        listAdjacentes.append((iVert, adj, peso))

                arestaSegura = (None, None, inf)
                for aresta in listAdjacentes:
                    if aresta[2] < arestaSegura[2]:
                        if rotulos[aresta[0]] == inf or rotulos[aresta[1]] == inf:
                            arestaSegura = aresta
                listAdjacentes.remove(arestaSegura)
                return arestaSegura

            else:
                arestaSegura = (None, None, inf)
                for aresta in listAdjacentes:
                    v1, v2, p = aresta[0], aresta[1], aresta[2]
                    if p < arestaSegura[2]:
                        ciclo = self.verificarCiclo(v1,v2)
                        if not ciclo:
                            arestaSegura = aresta
                listAdjacentes.remove(arestaSegura)
                return arestaSegura

        def verificarCiclo(self, v1, v2):
            marcado = [False]*self.vertices
            ciclo = self.vC(v1, v2, marcado)
            if ciclo is None:
                ciclo = False
            return ciclo

        def vC(self, v1, vTemp, marcado):
            marcado[vTemp] = True
            if v1 == vTemp:
                return True
            if v1 in adjacentes[vTemp]:
                return True

            else:
                i = 0
                while i < len(adjacentes[vTemp]):
                    vProx = adjacentes[vTemp][i]
                    if i == 0 and not marcado[vProx]:
                        ciclo = self.vC(v1, vProx, marcado)
                        if ciclo:
                            return ciclo
                    else:
                        i += 1
                    if i == len(adjacentes[vTemp]):
                        if not marcado[vProx]:
                            ciclo = self.vC(v1, vProx, marcado)
                            if ciclo:
                                return ciclo

    programa = True
    arestas  = {}
    qtdVertices = {}
    while programa:
        try:
            aresta = input()
            if aresta != '':
                aresta = aresta.split(', ')
                v1, v2, p = aresta[0], aresta[1], int(aresta[2])
                if (v1,v2) in arestas:
                    if p < arestas[(v1,v2)]:
                        arestas[(v1,v2)] = p
                elif (v2, v1) in arestas:
                    if p < arestas[(v2,v1)]:
                        arestas[(v2,v1)] = p
                else:
                    arestas[(v1,v2)] = p
                if v1 not in qtdVertices:
                    qtdVertices[v1] = True
                if v2 not in qtdVertices:
                    qtdVertices[v2] = True
        except EOFError:
            g = Grafo_Matriz(len(qtdVertices), ponderado=True)
            for i in arestas.keys():
                v1, v2 = i[0], i[1]
                p = arestas[(v1,v2)]
                g.inserir_aresta(v1, v2, p)
            g.kruskal()
            programa = False

if __name__ == '__main__':
    main()


#g = Grafo_Matriz(8, ponderado = True)
#g.inserir_aresta(0, 7, 16)
#g.inserir_aresta(0, 2, 26)
#g.inserir_aresta(0, 4, 38)
#g.inserir_aresta(6, 0, 58)
#g.inserir_aresta(1, 7, 19)
#g.inserir_aresta(5, 7, 28)
#g.inserir_aresta(2, 7, 34)
#g.inserir_aresta(4, 7, 37)
#g.inserir_aresta(1, 3, 29)
#g.inserir_aresta(1, 5, 32)
#g.inserir_aresta(1, 2, 36)
#g.inserir_aresta(2, 3, 17)
#g.inserir_aresta(6, 2, 40)
#g.inserir_aresta(3, 6, 52)
#g.inserir_aresta(4, 5, 35)
#g.inserir_aresta(6, 4, 93)
#g.kruskal()
