import random
def cria_baralho():
    lista_naipes = ['♠', '♣', '♦', '♥']
    lista_numeros = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    lista_cartas = []
    for naipe in lista_naipes:
        for numero in lista_numeros:
            carta = numero + naipe
            lista_cartas.append(carta)
    random.shuffle(lista_cartas)
    return lista_cartas
def lista_movimentos_possiveis(baralho, posicao):
    lista_resultado = []
    carta_selec = baralho[posicao]
    if posicao > 0:
        carta_ant = baralho[posicao-1]
        if extrai_valor(carta_ant) == extrai_valor(carta_selec) or extrai_naipe(carta_ant) == extrai_naipe(carta_selec):
            lista_resultado.append(1)
    if posicao > 2:
        carta_terc_ant = baralho[posicao-3]
        if extrai_valor(carta_terc_ant) == extrai_valor(carta_selec) or extrai_naipe(carta_terc_ant) == extrai_naipe(carta_selec):
            lista_resultado.append(3)
    return lista_resultado
def possui_movimentos_possiveis(baralho):
    tamanho = len(baralho)
    for i in range(tamanho):
        lista = lista_movimentos_possiveis(baralho, i)
        if lista != []:
            return True
    return False
def empilha(baralho, origem, destino):
    carta_selec = baralho[origem]
    baralho[destino] = carta_selec
    del(baralho[origem])
    return baralho
    
def extrai_valor(carta):
    if carta[:2] == '10':
        return '10'
    return carta[0]

    
def extrai_naipe(carta):
    if carta[:2] == '10':
        return carta[2]
    return carta[1]





