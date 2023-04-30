# =========================================================================================================================
# Beecrowd - 1583 - Contaminacao
# =========================================================================================================================
# Teoria: grafo nao direcionado
# Algoritmo utilizado: busca em largura com Flood Fill
# =========================================================================================================================
# Para facilitar a correçao, foram incluidos no codigo comentarios detalhados, mesmo se desnecessarios :)
# =========================================================================================================================

def busca_em_largura(matriz_pixels):      # metodo que realiza a busca em largura no grafo
    fila = []
    N_linhas = len(matriz_pixels)
    M_colunas = len(matriz_pixels[0])
    for i in range(N_linhas):
        for j in range(M_colunas):
            if matriz_pixels[i][j] == 'T':
                fila.append((i, j))
    while fila:
        x, y = fila.pop()
        if matriz_pixels[x][y] == 'A':
            matriz_pixels[x][y] = 'T'
        # Adiciona células vizinhas à fila
        if x > 0 and matriz_pixels[x-1][y] == 'A':      # x=0 - borda superior
            fila.append((x-1, y))
        if x < N_linhas-1 and matriz_pixels[x+1][y] == 'A':    # x=n-1 - borda inferior
            fila.append((x+1, y))
        if y > 0 and matriz_pixels[x][y-1] == 'A':      # y=0 - lateral esquerda
            fila.append((x, y-1))
        if y < M_colunas-1 and matriz_pixels[x][y+1] == 'A':    # y=m-1 - lateral direita
            fila.append((x, y+1))
     
    return matriz_pixels


                                                # =========================================================================
if __name__ == "__main__":
                                                # =========================================================================
                                                # Entrada
                                                # =========================================================================
                                                # A entrada é composta por vários mapas, sendo que a descrição de cada 
    N, M = input().split()                      # mapa começa com uma linha contendo dois inteiros N e M, correspondente 
    while (N != '0' and M != '0'):              # ao número de linhas e de colunas do mapa. As N linhas a seguir descrevem 
        N_linhas = int(N)                       # o mapa, cada linha contendo M caracteres, além do pulo de linha. 
        M_colunas = int(M)                      # A entrada termina quando N = M = 0, caso que não deve ser processado. 
                                                # Em todos os mapas, N e M são menores ou iguais a 50.
                                                # Os caracteres possíveis são: A, que representa uma célula contendo 
                                                # célula com agente contaminante.
        matriz = []
        for ind_linha in range(N_linhas):
            linha_completa = input().strip()
            matriz.append(list(linha_completa))
                                                # =========================================================================
                                                # Soluçao
                                                # =========================================================================
                                                # Eh necessario fazer uma busca em largura para 
                                                # determinar os componentes conexos
        matriz_contaminada = busca_em_largura(matriz)                                                
        
                                                # =========================================================================
                                                # Saida
                                                # =========================================================================
        for i in range(N_linhas):                      # Para cada mapa, imprima uma estimação da contaminação futura. 
            for j in range(M_colunas):                  # Esta estimação deverá corresponder ao mapa original (como visto na 
                print(matriz_contaminada[i][j], end='')  # entrada), porém trocando as células com água que foram contaminadas 
            print()                             # pelo caractere T. Deixe uma linha em branco após cada mapa (incluindo 
        print()                                 # o último mapa).

        N, M = input().split()