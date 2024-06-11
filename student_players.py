from basic_players import Player
from judge import * 

class Boneca(Player):
    def play(self, board_extremes, play_hist):
        playable_tiles = self._tiles
        hist = play_hist

        def contagem_o_que_tenho(self):
            contagem = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
            for i,j in playable_tiles:
                contagem[i] += 1
                contagem[j] += 1
            
            max_rep = max(contagem, key=contagem.get) # Retorna a peça que mais se repete.
            ocor = contagem[max_rep] # Retorna a quantidade de vezes que se repete.

            return contagem, max_rep, ocor 


        def analise_peças_disponíveis(self):
            
            peças = {0:11, 1:11, 2:11, 3:11, 4:11, 5:11, 6:11, 7:11, 8:11, 9:11}
            contagem = contagem()[0]
            peçasDisponíveis = {key: contagem[key] - peças[key] for key in contagem} #Conta as peças disponiveis p jogada tirando as suas

            for i,j in hist[-1][3]:
                peçasDisponíveis[i] -= 1
                peçasDisponíveis[j] -= 1


            return peçasDisponíveis



        def pluralidade(self):
            x,y,z = contagem(self)
            peças_max = [tile for tile in playable_tiles if tile[0] == y or tile[1] == y]

            # Armazenamento dos números adjascentes ao 'max_rep'.
            peças_adja = []
            for i,j in peças_max:
                if i != y:
                    peças_adja.append(i)
                elif j != y:
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


        def mais_repetiçao(self):
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


        if len(board_extremes) == 0:  # Condição para saber se o jogador é o primeiro a jogar.
            for tile in playable_tiles:
                if tile[0] == tile[1]:
                    x = contagem(self)
                    if x[tile[0]] == 2:
                        return 1, tile
                else:
                    x,y = mais_repetiçao(self)
                    return 1, y[0]

        if len(board_extremes) > 0:
            playable_tiles = [tile for tile in self._tiles if tile[0] in board_extremes or tile[1] in board_extremes]

            a,b,c = contagem(self)
            if b >= 5:
                x,y = pluralidade(self)
                return 1, y
            elif b < 5:
                x,y = mais_repetiçao(self)
                if len(y) > 0:
                    return 1, y[0]
            else:
                highest = -1
                tile_sum = -1
                for i in range(len(playable_tiles)):
                    if playable_tiles[i][0] + playable_tiles[i][1] > tile_sum:
                        tile_sum = playable_tiles[i][0] + playable_tiles[i][1]
                        highest = i
                if highest >= 0:
                    return 1, playable_tiles[highest]
                else:
                    return 1, None



# Função que define o nome da dupla:
def pair_name():
    return "BONECAS da COMP"

# Função que cria a dupla:
def create_pair():
    return (Boneca("123", 'Agnes'), Boneca('321', 'Marlon'))  # Defina aqui a dupla de jogadores. Deve ser uma tupla com dois jogadores.