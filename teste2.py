from basic_players import Player

class Jogador(Player):
    def play(self, board_extremes, play_hist):
        playable_tiles = self._tiles

        def melhor_numero(self): #
            if len(board_extremes) == 0:  # Condição para saber se o jogador é o primeiro a jogar.
                for tile in playable_tiles: # Confere se há alguma dupla em seuas peças.
                    if tile[0] == tile[1]:
                        return 1, tile
                    else: # Caso não tenha, a peça que tiver a maior soma de suas extremidades será escolhida.
                        contagem = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
                        for i, j in playable_tiles:
                            contagem[i] += 1
                            contagem[j] += 1

                        max_rep = max(contagem, key=contagem.get)
                        ocor = contagem[max_rep]
                        pecas_max = [tile for tile in playable_tiles if tile[0] == max_rep or tile[1] == max_rep]

                        maior_soma = 0
                        maior_tile = None

                        for tile in pecas_max:
                            if tile[0] + tile[1] > maior_soma:
                                maior_soma = tile[0] + tile[1]
                                maior_tile = tile
                        return 1, maior_tile

            if len(board_extremes) > 0:
                playable_tiles = [tile for tile in self._tiles if tile[0] in board_extremes or tile[1] in board_extremes]

                contagem = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
                for i, j in playable_tiles:
                    contagem[i] += 1
                    contagem[j] += 1

                max_rep = max(contagem, key=contagem.get)
                ocor = contagem[max_rep]

                # Verifica se há mais de duas peças com o mesmo número.
                if ocor > 4:
                    peças_k = []
                    for tile in playable_tiles:
                        if tile[0] == max_rep or tile[1] == max_rep:
                            peças_k.append(tile)
                    
                    menor_soma = peças_k[0][0] + peças_k[0][1]
                    menor_peça = peças_k[0]

                    for tile in peças_k:
                        if tile[0] + tile[1] < menor_soma:
                            menor_soma = tile[0] + tile[1]
                            menor_peça = tile

                    return 1, menor_peça
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
                    

    def estrategia2(self):
        my_tiles = self.tiles
        peças = {0:11, 1:11, 2:11, 3:11, 4:11, 5:11, 6:11, 7:11, 8:11, 9:11}
        for i,j in my_tiles:
            for k in peças:
                if i == k:
                    peças[k] -= 1
                elif j == k:
                    peças[k] -= 1
        return peças

# Função que define o nome da dupla:
def pair_name():
    return "BONECAS da COMP"

# Função que cria a dupla:
def create_pair():
    return (Jogador("123", 'Agnes'), Jogador('321', 'Marlon'))  # Defina aqui a dupla de jogadores. Deve ser uma tupla com dois jogadores.