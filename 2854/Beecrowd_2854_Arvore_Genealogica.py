# =========================================================================================================================
# Beecrowd - 2854 - Arvore Genealogica
# =========================================================================================================================
# =========================================================================================================================
# Teoria: grafo nao direcionado
# Algoritmo utilizado: busca em largura com contagem de componentes conexas
# =========================================================================================================================
# Para facilitar a correçao, foram incluidos no codigo comentarios detalhados, mesmo se desnecessarios :)
# =========================================================================================================================

                                                # =========================================================================
class Celula:                                   # classe que instancia cada celula da lista encadeada
    def __init__(self, posicao, nome):          # construtor da classe definido com o metodo init recebe parametro "valor"
        self.posicao = posicao                  # posicao que o nome ocupa no vetor de listas de adjacências
        self.nome = nome                        # pessoa que se relaciona com a pessoa "dona" daquela lista encadeada
        self.prox = None                        # None = NULL

                                                # =========================================================================
class ListaEncadeada:                           # classe que inicializa a lista encadeada com a celula cabeca vazia
    def __init__(self, nome):                   # construtor da classe definido com o metodo init
        self.nome = nome                        # nome da pessoa que se relaciona (noh adjacente)
        self.prox_cabeca = None                 # quando a lista eh construida ela possui apenas a celula cabeca que aponta 
                                                # para NULL e contem dado vazio


                                                # =========================================================================
    def inserir_no_inicio(self, posicao, nome): # metodo que insere apos cabeca e antes do resto da lista
        nova_celula = Celula(posicao, nome)     # instancia a nova celula com os valores passados
        nova_celula.prox = self.prox_cabeca     # faz a nova celula apontar para quem a cabeca aponta
        self.prox_cabeca = nova_celula          # e faz a celula cabeca apontar para a nova celula


                                                # =========================================================================
    def iterar(self):                           # metodo que cria lista de iteraveis com os dados das celulas
        celula_atual = self.prox_cabeca         # celula atual eh a celula para qual a cabeca aponta (ultimo inserido)
        while celula_atual is not None:         # enquanto não chega na celula "rabo"
            yield celula_atual.posicao          # yield cria um gerador (sequencia de valores que podem ser iterados)
            celula_atual = celula_atual.prox    # passa pra proxima celula ate o fim

                                                # =========================================================================
    def imprimir(self):                         # metodo de teste para verificar a criacao correta da lista encadeada
        if self.prox_cabeca is None:            # verifica se a lista encadeada esta vazia
            print()   
        else:
            celula_atual = self.prox_cabeca       # celula atual eh a celula para qual a cabeca aponta (ultimo inserido)
            while celula_atual is not None:       # enquanto não chega na celula "rabo"
                print(celula_atual.nome, end="-") # imprime na mesma linha, separados por -
                celula_atual = celula_atual.prox  # passa pra proxima celula ate o fim
            print()

                                                # =========================================================================
class VetorDeListasEnc:                         # classe que instancia o vetor de listas encadeadas
    def __init__(self, tam):                    # construtor da classe recebe parametro "tam" que eh o tamanho do vetor
        self.tamanho = tam                      # guarda o tamanho do vetor no atributo tamanho
        self.vetor_LE = [ListaEncadeada("") for i in range(tam)] 
                                                # cria o vetor do tamanho especificado usando o construtor
                                                # e inicializando todos elementos com nome vazio e com a celula 
                                                # cabeca apontando para NULL

                                                # =========================================================================
    def busca_em_largura(self, qtde_nohs):      # metodo que realiza a busca em largura no grafo
        vert_visitado = [False] * qtde_nohs     # cria lista de booleanos inicializados com F do tamanho do vetor de nohs
        qtd_componentes_conectados = 0
        for i in range(qtde_nohs):              # for every vertex s of G not explored yet
            if not vert_visitado[i]:            # noh marcado com False siginifica que ainda nao foi visitado
                fila = [i]                      # fila implementada com uma lista - enfileira i - do Enqueue(S,s)
                vert_visitado[i] = True         # mark vertex s as visited - noh na camada zero
                                                # so sai do while se houver mais de uma componente conexa
                while fila:                     # enquanto tiver elemento na fila - while S is not empty do
                    vertice = fila.pop(0)       # desenfileira o primeiro a entrar (fila) - u ← Dequeue(S); 
                                                # metodo iterar() retorna sequencia dos nohs vizinhos
                    for adjacente in self.vetor_LE[vertice].iterar():  # For each v in Adj[u] then
                        if not vert_visitado[adjacente]:    # if v is unexplored then
                            fila.append(adjacente)          # Enqueue(S,v) - enfileira vizinho (adjacente)
                            vert_visitado[adjacente] = True # mark vertex v as visited
                qtd_componentes_conectados += 1                    
    
        return qtd_componentes_conectados

                                                # =========================================================================
if __name__ == "__main__":
                                                # =========================================================================
                                                # Entrada
                                                # =======
    M, N = input().split()                      # A entrada consiste de um único teste que contém muitas linhas de teste. 
    M_qtd_nohs = int(M)                         # A primeira linha contém dois inteiros M (1 < M ≤ 300) e N (1 < N ≤ 200)  
    N_qtd_arestas = int(N)                      # que indicam respectivamente a quantidade pessoas diferentes e a 
                                                # quantidade de relações existentes entre estas pessoas. 
    vetor_nohs = VetorDeListasEnc(M_qtd_nohs)   # cria o vetor de listas de adjacências chamando o construtor da classe
    i_posicao_vazia = 0                         # indice do vetor de nohs que indica a primeira posicao do vetor que 
                                                # ainda esta vazia (sem nome)
    for idx_qtd_arestas in range(0, N_qtd_arestas):
                                                # Cada uma destas N relações (listadas a seguir), contém três palavras: 
                                                # um nome próprio seguido de uma relação e de outro nome próprio, 
                                                # todos separados com espaço (náo tem espaço após o último nome).
        Nome1, Relacionamento, Nome2 = input().split()
                                                # Obs.: nunca existirá um nome representando duas pessoas diferentes. 
                                                # Se houver 2 Pedros, por exemplo, eles serão identificados por Pedro_1 e 
                                                # Pedro_2 e assim sucessivamente,
                                                # como o grafo eh nao direcionado e o relacionamento eh mutuo eh preciso 
                                                # salvar nas listas de adjacencias tanto Nome1->Nome2 (ida) quanto 
                                                # Nome2->Nome1 (volta)
        nao_achou_nome = True                   # ida - Nome1->Nome2
        for i in range(0, vetor_nohs.tamanho):          # procura no vetor de nohs se o nome ja existe para inserir 
            if (vetor_nohs.vetor_LE[i].nome == Nome1):  # na sua lista de adjacências
                i_ida = i
                nao_achou_nome = False
                break
        if nao_achou_nome:                          # se nao encontrou o nome, salva na primeira posicao vazia do vetor
            i_ida = i_posicao_vazia
            i_posicao_vazia += 1
            vetor_nohs.vetor_LE[i_ida].nome = Nome1
                                                # volta - Nome2->Nome1
        nao_achou_nome = True        
        for j in range(0, vetor_nohs.tamanho):          # procura no vetor de nohs se o nome ja existe para inserir 
            if (vetor_nohs.vetor_LE[j].nome == Nome2):  # na sua lista de adjacências
                i_volta = j
                nao_achou_nome = False
                break
        if nao_achou_nome:                      # se nao encontrou o nome, salva na primeira posicao vazia do vetor
            i_volta = i_posicao_vazia
            i_posicao_vazia += 1
            vetor_nohs.vetor_LE[i_volta].nome = Nome2
                                                # apos determinar a posicao do vetor que vai salvar o vizinho
                                                # chama o metodo para inserir a celula apos o no cabeca e antes do 
                                                # noh que ela aponta - ida e volta - Nome1->Nome2 e Nome2->Nome1   
        vetor_nohs.vetor_LE[i_ida].inserir_no_inicio(i_volta, Nome2)        
        vetor_nohs.vetor_LE[i_volta].inserir_no_inicio(i_ida, Nome1)
    

                                                # =========================================================================
                                                # Soluçao
                                                # =========================================================================
                                                # Eh necessario fazer uma busca em largura para 
                                                # contabilizar as componentes conexas existentes
                                                # a busca em largura retorna a quantidade de arvores geradas
                                                # cada arvore tem origem em uma componente conexa
    qtd_componentes_conexos = vetor_nohs.busca_em_largura(M_qtd_nohs)

                                                # =========================================================================
                                                # Saida
                                                # =========================================================================
                                                # A saída é composta de um único número inteiro que representa a quantidade de 
                                                # famílias diferentes encontradas com base nohs documentos fornecidos por Armindo.
                                                # cada familia eh um componente conexo do grafo
    print(qtd_componentes_conexos)

    # =================================================================================================================
    # PARA TESTAR: impressao das listas encadeadas de cada elemento do vetor
    # se quiser testar se a lista encadeada foi montada corretamente, basta tirar os comentarios do bloco abaixo
    # =================================================================================================================
    '''
    print("===========================================")
    print("Teste - Vetor de listas encadeadas criado:")
    for i in range(0, M_qtd_nohs):
        print(vetor_nohs.vetor_LE[i].nome, end="->")
        vetor_nohs.vetor_LE[i].imprimir()
    '''
