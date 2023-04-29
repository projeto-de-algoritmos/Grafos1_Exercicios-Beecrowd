# =========================================================================================================================
# Beecrowd - 1979 - Salas Separadas
# =========================================================================================================================
# Teoria: grafo nao direcionado
# Algoritmo utilizado: busca em largura com verificacao de grafo bipartido
# =========================================================================================================================
# Para facilitar a correçao, foram incluidos no codigo comentarios detalhados, mesmo se desnecessarios :)
# =========================================================================================================================

                                                # =========================================================================
class Celula:                                   # classe que instancia cada celula da lista encadeada
    def __init__(self, valor):                  # construtor da classe definido com o metodo init recebe parametro "valor"                  
        self.dado = valor                       # atributos de cada celula - dado e prox
        self.prox = None                        # NULL

                                                # =========================================================================
class ListaEncadeada:                           # classe que inicializa a lista encadeada com a celula cabeca vazia
    def __init__(self):                         # construtor da classe definido com o metodo init sem parametros
        self.prox_cabeca = None                 # quando a lista eh construida ela possui apenas a celula cabeca que 
                                                # aponta para NULL e nao contem dado

                                                # =========================================================================
    def inserir_no_inicio(self, valor):         # metodo que recebe "valor" e insere apos cabeca e antes do resto da lista
        nova_celula = Celula(valor)             # instancia a nova celula com o valor passado
        nova_celula.prox = self.prox_cabeca     # faz a nova celula apontar para quem a cabeca aponta 
        self.prox_cabeca = nova_celula          # e faz a celula cabeca apontar para a nova celula

                                                # =========================================================================
    def imprimir(self):                         # metodo de teste para verificar a criacao correta da lista encadeada
        if self.prox_cabeca is None:            # verifica se a lista encadeada esta vazia
            print()   
        else:
            celula_atual = self.prox_cabeca     # celula atual eh a celula para qual a cabeca aponta (ultimo inserido)
            while celula_atual is not None:     # enquanto não chega na celula "rabo"
                print(celula_atual.dado + 1, end="-") # imprime uma por uma na mesma linha, separados por -
                celula_atual = celula_atual.prox      # passa pra proxima celula ate o fim
            print()
    
                                                # =========================================================================
class VetorDeListasEnc:                         # classe que instancia o vetor de listas encadeadas
    def __init__(self, tam):                    # construtor da classe recebe parametro "tam" que eh o tamanho do vetor
        self.tamanho = tam                      # guarda o tamanho do vetor no atributo tamanho
        self.vetor_LE = [ListaEncadeada() for i in range(tam)] 
                                                # cria o vetor do tamanho especificado usando o construtor
                                                # e inicializando todos elementos so com celula cabeca apontando para NULL

                                                # =========================================================================
    def busca_em_largura_G(self, grafo):        # metodo que realiza a busca em largura no grafo
        qtde_nohs = grafo.tamanho               # grafo - vetor de listas encadeadas
        noh_visitado = [-1] * qtde_nohs         # cria lista de booleanos inicializados com -1 do tamanho do vetor de nohs
                                                # que vai receber o numero da camada a qula o noh pertence
        flag_eh_bipartido = True                # considera por padrao que o grafo eh bipartido
        for i in range(0, qtde_nohs):           # for every vertex s of G not explored yet
            if noh_visitado[i] == -1:           # noh marcado com -1 siginifica que ainda nao foi visitado
                fila = [i]                      # fila implementada com uma lista - enfileira i - do Enqueue(S,s)
                noh_visitado[i] = 0             # mark vertex s as visited - noh na camada zero
                                                # so sai do while se houver mais de uma componente conexa
                while fila:                     # enquanto tiver elemento na fila - while S is not empty do
                    noh_em_analise = fila.pop(0)            # desenfileira o primeiro a entrar (fila) - u ← Dequeue(S); 
                    celula_atual = self.vetor_LE[noh_em_analise].prox_cabeca
                    while celula_atual is not None:         # percorre lista de vizinhos - For each v in Adj[u] then
                        noh_vizinho = celula_atual.dado
                        if noh_visitado[noh_vizinho] == -1: # if v is unexplored then
                            fila.append(noh_vizinho)        # Enqueue(S,v)
                            noh_visitado[noh_vizinho] = noh_visitado[noh_em_analise] + 1    # mark vertex v as visited
                                                            # marca a camada do noh vizinho como a camada seguinte
                        else:                   # se o noh ja foi visitado e esta na mesma camada - grafo nao eh bipartido
                            if (noh_visitado[noh_vizinho] == noh_visitado[noh_em_analise]):
                                flag_eh_bipartido = False
                        celula_atual = celula_atual.prox    # continua percorrendo lista de vizinhos

        return noh_visitado, flag_eh_bipartido
    
                                                # =========================================================================
if __name__ == "__main__":
                                                # =========================================================================
                                                # Entrada
                                                # =======
                                                # A entrada é composta de diversos casos de teste. 
    N_num_alunos = int(input())                 # A primeira linha de cada caso de teste consiste em um inteiro N (2 ≤ N ≤ 100) 
                                                # indicando o número de alunos que irão realizar a prova.
    while N_num_alunos != 0:                    # Cada N par de linhas seguintes descreve as relações de amizade de cada  
        vetor_amigos = VetorDeListasEnc(N_num_alunos) 
        for j in range (N_num_alunos):          # participante, de forma que a primeira linha consiste no identificador do  
            participante = int(input())         # participante, e a linha seguinte consiste em uma lista descrevendo uma 
            amigos = []                         # quantidade M de alunos (1 ≤ M < N) com os quais aquele participante possui
            amigos = input().split()            # uma relação de amizade.
            for i in range (len(amigos)):       
                vetor_amigos.vetor_LE[participante - 1].inserir_no_inicio(int(amigos[i]) - 1)
                vetor_amigos.vetor_LE[int(amigos[i]) - 1].inserir_no_inicio(participante - 1)
                                                # Considere que não é relevante o número de pessoas dispostas em cada sala,
                                                # e que, se existe uma relação de amizade entre alunos x e y, existe uma  
                                                # relação de amizade entre y e x. 

                                                # =========================================================================
                                                # Soluçao
                                                # =========================================================================
                                                # Eh necessario fazer uma busca em largura para 
                                                # determinar as camadas as quais cada noh pertence e
                                                # verificar se exite aresta entre dois nohs de mesma camada
                                                # o que caracteriza que ha pelo menos um ciclo impar,
                                                # ou seja, o grafo nao eh bipartido
        camada, flag_eh_bipartido = vetor_amigos.busca_em_largura_G(vetor_amigos)

                                                # =========================================================================
                                                # Saida
                                                # =========================================================================
                                                # Para cada caso de teste, deverá ser impressa uma linha contendo a  
                                                # resposta"SIM", caso seja possível dispor os alunos de forma que não hajam
                                                # dois amigos realizando a prova na mesma sala, e "NAO", caso contrário.
        if flag_eh_bipartido:
            print("SIM")
        else:
            print("NAO")

        # =================================================================================================================
        # PARA TESTAR: impressao das listas encadeadas de cada elemento do vetor
        # se quiser testar se a lista encadeada foi montada corretamente, basta tirar os comentarios do bloco abaixo
        # =================================================================================================================
        '''
        print("===========================================")
        print("Teste - Vetor de listas encadeadas criado:")
        for i in range(0, N_num_alunos):
            print(i + 1, end="-")
            vetor_amigos.vetor_LE[i].imprimir()
        '''
        # =================================================================================================================
        # PARA TESTAR: impressao do vetor que vai receber as listas encadeadas com as relacoes de amizade
        # se quiser testar que o vetor foi montado corretamente, basta tirar os comentarios do bloco abaixo
        # =================================================================================================================
        '''
        print("===========================================")
        print("Teste - Relacoes de amizade:")
        for i in range (len(amigos)):
            print(participante, amigos[i], end=" - ")
        print()
        '''
        # =================================================================================================================
        # PARA TESTAR: impressao do vetor que armazena os numeros das camadas dos nohs visitados
        # se quiser testar se as camadas foram marcadas corretamente, basta tirar os comentarios do bloco abaixo
        # =================================================================================================================
        '''
        print("===========================================")
        print("Teste - camadas as quais os nohs pertencem:")
        print(camada)
        print("===========================================")
        '''

        N_num_alunos = int(input())         # A entrada termina quando N = 0, e não deve ser processada. 

