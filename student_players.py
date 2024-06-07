from basic_players import Player
class Xerecuda(Player):
def play(self, board_extremes, play_hist):
playable_tiles = self._tiles
if len(board_extremes) > 0:
# Filtrando as peças jogáveis
playable_tiles = [tile for tile in self._tiles if tile[0] in

board_extremes or tile[1] in board_extremes]
else:
return 1, None
# Verificação de quantas peças com extremidades iguais.
contagem = {}
for p in playable_tiles:
for n in p:
if n in contagem:
contagem[n] += 1
else:
contagem[n] = 1

k_rep = None
ocor = 0
if contagem:
k_rep = max(contagem, key=contagem.get) # Peça que mais se

repete

ocor = contagem[k_rep] # Ocorrências da repetição
# Verifica se há mais de duas peças com o mesmo número.
if ocor > 2:
# Armazena as peças de extremidade igual a 'k_rep'.
pecas_k = []
for tile in playable_tiles:
if tile[0] == k_rep or tile[1] == k_rep:
pecas_k.append(tile)

menor_soma = pecas_k[0][0] + pecas_k[0][1]
menor_peca = pecas_k[0]
for tile in pecas_k:

if tile[0] + tile[1] < menor_soma:
menor_soma = tile[0] + tile[1]
menor_peca = tile
return 1, menor_peca
else:
highest = -1
tile_sum = -1
for i in range(len(playable_tiles)):
if playable_tiles[i][0] + playable_tiles[i][1] >

tile_sum:

tile_sum = playable_tiles[i][0] +

playable_tiles[i][1]

highest = i
if highest >= 0:
return 1, playable_tiles[highest]
else:
return 1, None

class Pingueluda(Player):
def play(self, board_extremes, play_hist):
playable_tiles = self._tiles
if len(board_extremes) > 0:
# Filtrando as peças jogáveis
playable_tiles = [tile for tile in self._tiles if tile[0] in

board_extremes or tile[1] in board_extremes]
else:
return 1, None
# Verificação de quantas peças com extremidades iguais.
contagem = {}
for p in playable_tiles:
for n in p:
if n in contagem:
contagem[n] += 1
else:
contagem[n] = 1

k_rep = None
ocor = 0

if contagem:
k_rep = max(contagem, key=contagem.get) # Número que mais se

repete

ocor = contagem[k_rep] # Ocorrências da repetição
# Verifica se há mais de duas peças com o mesmo número.
if ocor > 2:
# Armazena as peças de extremidade igual a 'k_rep'.
pecas_k = []
for tile in playable_tiles:
if tile[0] == k_rep or tile[1] == k_rep:
pecas_k.append(tile)

menor_soma = pecas_k[0][0] + pecas_k[0][1]
menor_peca = pecas_k[0]
for tile in pecas_k:
if tile[0] + tile[1] < menor_soma:
menor_soma = tile[0] + tile[1]
menor_peca = tile
return 1, menor_peca
else:
highest = -1
tile_sum = -1
for i in range(len(playable_tiles)):
if playable_tiles[i][0] + playable_tiles[i][1] >

tile_sum:

tile_sum = playable_tiles[i][0] +

playable_tiles[i][1]

highest = i
if highest >= 0:
return 1, playable_tiles[highest]
else:
return 1, None
# Função que define o nome da dupla:
def pair_name():
return "BONECAS"
# Função que cria a dupla:
def create_pair():

return (Xerecuda("123", 'Agnes'), Pingueluda('321', 'Marlon')) #
Defina aqui a dupla de jogadores. Deve ser uma tupla com dois
jogadores.