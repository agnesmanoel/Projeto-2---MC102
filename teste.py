def contagem(playable_tiles):
    contagem = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    for i,j in playable_tiles:
        contagem[i] += 1
        contagem[j] += 1
    return contagem

#####################################################################################################
#####################################################################################################

def pluralidade(self):
    x = contagem(playable_tiles)

    max_rep = max(x, key=contagem.get) # Retorna a peça que mais se repete.
    ocor = x[max_rep] # Retorna a quantidade de vezes que se repete.
    peças_max = [tile for tile in playable_tiles if tile[0] == max_rep or tile[1] == max_rep]

    # Armazenamento dos números adjascentes ao 'max_rep'.
    peças_adja = []
    for i,j in peças_max:
        if i != max_rep:
            peças_adja.append(i)
        elif j != max_rep:
            peças_adja.append(j)

    # Analisa qual número adjascente mais se repete.
    maior_soma = None
    maior_contagem = 0
    for n in peças_adja:
        if x[n] > maior_contagem:
            maior_contagem = x[n]
            maior_soma = n

    for i, j in peças_max:
        if i == maior_soma or j == maior_soma:
            return peças_max, (i, j)

#####################################################################################################
#####################################################################################################

def mais_repetição(playable_tiles):
    repeticao = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
    
    for i, j in playable_tiles:
        for chave in repeticao.keys():
            if i == chave or j == chave:
                repeticao[chave].append((i, j))
    
    for chave, valores in list(repeticao.items()):  # Convertendo para lista para poder modificar o dicionário durante a iteração
        if len(valores) < 2:
            del repeticao[chave]

    soma_maxima = 0
    peças_max = []
    for valores in repeticao.values():
        for peças in valores:
            s = sum(peças)
            if s > soma_maxima:
                soma_maxima = s
                peças_max = [peças]
            elif s == soma_maxima:
                peças_max.append(peças)

    return repeticao, peças_max


def menos_repetição(playable_tiles):
    repeticao = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
    
    for i, j in playable_tiles:
        for chave in repeticao.keys():
            if i == chave or j == chave:
                repeticao[chave].append((i, j))
    
    for chave, valores in list(repeticao.items()):  
        if len(valores) > 2:
            del repeticao[chave]

    min_ocorrencias = float('inf')  # Começa com um valor infinito para garantir que qualquer valor seja menor
    peças_min = []
    for valores in repeticao.values():
        for peças in valores:
            ocorrencias = len([x for x in valores if x == peças])
            if ocorrencias < min_ocorrencias:
                min_ocorrencias = ocorrencias
                peças_min = [peças]
            elif ocorrencias == min_ocorrencias:
                peças_min.append(peças)

    return repeticao, peças_min


#####################################################################################################
#####################################################################################################

def muitas_ocorrencias(self):
    x = contagem(playable_tiles)

    max_rep = max(x, key=x.get)
    ocor = x[max_rep]

    if ocor >= 5:
        y, z = pluralidade(self)
        return z

#####################################################################################################
#####################################################################################################

def contagem(self):
    contagem = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    for i,j in playable_tiles:
        contagem[i] += 1
        contagem[j] += 1
    return contagem