def cria_baralho():
    import random as rand
    lista_naipes = ['♠', '♣', '♦', '♥']
    lista_numeros = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    lista_cartas = []
    for naipe in lista_naipes:
        for numero in lista_numeros:
            carta = numero + naipe
            lista_cartas.append(carta)
    rand.shuffle(lista_cartas)
    return lista_cartas

interrupitor = True

while interrupitor == True:
    print('Paciência Acordeão\n==================\nSeja bem-vindo(a) ao jogo de Paciência Acordeão!\nO objetivo deste jogo é colocar todas as cartas em uma mesma pilha.\nExistem apenas dois movimentos possíveis:\n1. Empilhar uma carta sobre a carta imediatamente anterior;\n2. Empilhar uma carta sobre a terceira carta anterior.\nPara que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:\n1. As duas cartas possuem o mesmo valor\n2. As duas cartas possuem o mesmo naipe.\nDesde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.\nAperte [Enter] para iniciar o jogo...')
    a = input('')
    if a == '':
        print('O estado atual do baralho é:')
    baralho = cria_baralho()
    for i in range(len(baralho)):
        print('{0}. {1}'.format((i+1), baralho[i]))
    interrupitor = False