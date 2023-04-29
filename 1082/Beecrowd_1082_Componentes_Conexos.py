# =========================================================================================================================
# Beecrowd - 1082 - Componentes Conexos
# =========================================================================================================================
# Teoria: grafo nao direcionado
# Algoritmo utilizado: busca em profundidade com contagem e indicacao dos elementos das componentes conexas
# =========================================================================================================================
# Para facilitar a correçao, foram incluidos no codigo comentarios detalhados, mesmo se desnecessarios :)
# =========================================================================================================================

                                                # =========================================================================
class Celula:                                   # classe que instancia cada celula da lista encadeada
    def __init__(self, valor):                  # construtor da classe definido com o metodo init recebe parametro "valor"
        self.dado = valor                       # atributos de cada celula - dado e prox
        self.prox = None                        # None = NULL

                                                # =========================================================================
class ListaEncadeada:                           # classe que inicializa a lista encadeada com a celula cabeca vazia
    def __init__(self):                         # construtor da classe definido com o metodo init sem parametros
        self.prox_cabeca = None                 # quando a lista eh construida ela possui apenas a celula cabeca que aponta 
                                                # para NULL e nao contem dado

                                                # =========================================================================
    def inserir_no_inicio(self, valor):         # metodo que recebe "valor" e insere apos cabeca e antes do resto da lista
        nova_celula = Celula(valor)             # instancia a nova celula com o valor passado
        nova_celula.prox = self.prox_cabeca     # faz a nova celula apontar para quem a cabeca aponta
        self.prox_cabeca = nova_celula          # e faz a celula cabeca apontar para a nova celula

                                                # =========================================================================
    def iterar(self):                           # metodo que cria lista de iteraveis com os dados das celulas
        celula_atual = self.prox_cabeca         # celula atual eh a celula para qual a cabeca aponta (ultimo inserido)
        while celula_atual is not None:         # enquanto não chega na celula "rabo"
            yield (ord(celula_atual.dado) - 97) # yield cria um gerador (sequencia de valores que podem ser iterados)
            celula_atual = celula_atual.prox    # passa pra proxima celula ate o fim

                                                # =========================================================================
    def imprimir(self):                         # metodo de teste para verificar a criacao correta da lista encadeada
        if self.prox_cabeca is None:            # verifica se a lista encadeada esta vazia
            print()   
        else:
            celula_atual = self.prox_cabeca       # celula atual eh a celula para qual a cabeca aponta (ultimo inserido)
            while celula_atual is not None:       # enquanto não chega na celula "rabo"
                print(celula_atual.dado, end="-") # imprime na mesma linha, separados por -
                celula_atual = celula_atual.prox  # passa pra proxima celula ate o fim
            print()

                                                # =========================================================================
class VetorDeListasEnc:                         # classe que instancia o vetor de listas encadeadas
    def __init__(self, tam):                    # construtor da classe recebe parametro "tam" que eh o tamanho do vetor
        self.tamanho = tam                      # guarda o tamanho do vetor no atributo tamanho
        self.vetor_LE = [ListaEncadeada() for i in range(tam)] 
                                                # cria o vetor do tamanho especificado usando o construtor
                                                # e inicializando todos elementos so com celula cabeca apontando para NULL

                                                # =========================================================================
                                                # metodo que realiza a DFS recursiva
    def busca_em_profundidade_recursiva(self, noh, noh_visitado, qtd_comp_conexos, componente):
        noh_visitado[noh] = True                   # Marque v como visitado
        for vizinho in self.vetor_LE[noh].iterar(): # Para todo w em Adj(v) - iterar() retorna sequencia orgaos vizinhos
            if not noh_visitado[vizinho]:          # Se w não visitado então
                componente[qtd_comp_conexos].append(chr(vizinho+97))    # Insira aresta (v, w) na árvore
                self.busca_em_profundidade_recursiva(vizinho, noh_visitado, qtd_comp_conexos, componente) # DFS-Visit(G,w) 
                                                
                                                # =========================================================================
    def busca_em_profundidade(self, qtde_nohs): # metodo que realzia a DFS
        noh_visitado = [False] * qtde_nohs      # cria lista de booleanos inicializados com False do tamanho do vetor 
        qtd_componentes_conexos = 0             # contador de componentes conexos
        componentes = {}                        # matriz que ira receber os vetores de componentes conexas
        for i in range(0, qtde_nohs):           # Para todo vem G
            if not noh_visitado[i]:             # Se v não visitado então
                componentes[qtd_componentes_conexos] = []
                componentes[qtd_componentes_conexos].append(chr(i+97))
                                                # DFS-Visit(G, v)
                self.busca_em_profundidade_recursiva(i, noh_visitado, qtd_componentes_conexos, componentes) 
                qtd_componentes_conexos = qtd_componentes_conexos + 1                    
        return componentes, qtd_componentes_conexos

                                                # =========================================================================
if __name__ == "__main__":
                                                # =========================================================================
                                                # Entrada
                                                # =========================================================================
    N_qtd_casos = int(input())                  # A primeira linha do arquivo de entrada contem um valor inteiro N 
                                                # que representa a quantidade de casos de teste que vem a seguir.
    for ind_caso in range(0, N_qtd_casos):      # Cada grafo tem no minimo 1 componente conexo.
        vetor_nohs = VetorDeListasEnc(26)       # cria o vetor de listas encadeadas do tamanho defindo pelo problema
        V, E = input().split()                  # Cada caso de teste contem dois valores V e E que sao, respectivamente,
        V_qtd_nohs = int(V)                     # a quantidade de nohs 
        E_qtd_arestas = int(E)                  # e arestas (Edges) do grafo. 
                                                # Seguem E linhas na sequencia, cada uma delas representando uma das arestas 
                                                # que ligam tais nohs. Cada vertice e representado por uma letra minuscula 
                                                # do alfabeto ('a'-'z'), ou seja, cada grafo pode ter no maximo 26 nohs. 
                                                # Obs: Os nohs de cada caso de teste sempre iniciam no 'a'. 
                                                # Isso significa que um caso de teste que tem 3 nohs, tem obrigatoriamente 
                                                # os nohs 'a', 'b' e 'c'.
        for idx_qtd_arestas in range(0, E_qtd_arestas):
            vertice_origem, vertice_destino = input().split()
            i_origem = ord(vertice_origem) - ord('a')   
                                                # numero ASCII da letra a eh 97 - ord retorna o numero ASCII do caracter
            vetor_nohs.vetor_LE[i_origem].inserir_no_inicio(vertice_destino)
            i_destino = ord(vertice_destino) - ord('a')
            vetor_nohs.vetor_LE[i_destino].inserir_no_inicio(vertice_origem)

                                                # =========================================================================
                                                # Soluçao
                                                # =========================================================================
                                                # Eh necessario fazer uma busca em largura para 
                                                # determinar os componentes conexos
        compon_conexos, qtd_conectados = vetor_nohs.busca_em_profundidade(V_qtd_nohs)

                                                # =========================================================================
                                                # Saida
                                                # =========================================================================
                                                # Para cada caso de teste da entrada, deve ser apresentada uma mensagem 
        print(f'Case #{ind_caso + 1}:')         # Case #n:, onde n indica o numero do caso de teste (conforme exemplo dado). 
        for i in compon_conexos:                # Obs: os nodos devem sempre ser apresentados em ordem crescente e
            compon_conexos[i].sort()            # se ha caminho de a ate b significa que ha caminho de b ate a.
            arvores = ','.join(compon_conexos[i])   
                                                # Segue a listagem dos nohs de cada segmento, um segmento por linha, 
            if arvores:                         # separados por virgula
                arvores += ','                  # (inclusive com uma virgula no final da linha).
                print(arvores)
        print(f'{qtd_conectados} connected components') 
                                                # Finalizando o caso de teste, deve ser apresentada uma mensagem indicando  
                                                # a quantidade de componentes conexos do grafo (em ingles).  Todo caso de 
        print()                                 # teste deve ter uma linha em branco no final, inclusive o ultimo caso.
                                                # =========================================================================
                                                
        # =================================================================================================================
        # PARA TESTAR: impressao das listas encadeadas de cada elemento do vetor
        # se quiser testar se a lista encadeada foi montada corretamente, basta tirar os comentarios do bloco abaixo
        # =================================================================================================================
        '''
        print("Teste - Vetor de listas encadeadas criado:")
        for i in range(0, V_qtd_nohs):
            letra = chr(i + 97)
            print(letra, end="-")
            vetor_nohs.vetor_LE[i].imprimir()
        '''
        # =================================================================================================================
