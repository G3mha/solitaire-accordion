import random
import mecanicas
llll = 0
print('Paciência Acordeão\n==================\nSeja bem-vindo(a) ao jogo de Paciência Acordeão!\nO objetivo deste jogo é colocar todas as cartas em uma mesma pilha.\nExistem apenas dois movimentos possíveis:\n1. Empilhar uma carta sobre a carta imediatamente anterior;\n2. Empilhar uma carta sobre a terceira carta anterior.\nPara que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:\n1. As duas cartas possuem o mesmo valor\n2. As duas cartas possuem o mesmo naipe.\nDesde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.\nAperte [Enter] para iniciar o jogo...')
a = input('')
if a == '':
    liga = True
while liga == True:
    baralho = mecanicas.cria_baralho()
    pode_mover = True
    while pode_mover == True:
        pode_mover = mecanicas.possui_movimentos_possiveis(baralho)
        if pode_mover == False:
            break
        lista_numeros = range(1, len(baralho)+1)
        print('O estado atual do baralho é:')
        for i in range(max(lista_numeros)):
            ind = lista_numeros[i]
            cart = baralho[i]
            print('{0}. {1}'.format(ind, cart))
        k = input('Escolha uma carta (digite um número entre 1 e {}): '.format(max(lista_numeros)))
        while int(k) not in range(1, (max(lista_numeros)+1)):
            k = input('Posição inválida. Por favor, digite um número entre 1 e {}): '.format(max(lista_numeros)))
        index_selec = int(k) - 1
        lista_mov = mecanicas.lista_movimentos_possiveis(baralho, index_selec)
        carta_selec = baralho[index_selec]
        while lista_mov == []:
            k = input('Movimento não permitido, por favor insira um número de 1 a {}: '.format(max(lista_numeros)))
            pode_mover = mecanicas.possui_movimentos_possiveis(baralho)
            if pode_mover == False:
                llll = 1
                break
            index_selec = int(k) - 1
            lista_mov = mecanicas.lista_movimentos_possiveis(baralho, index_selec)
        if llll == 1:
            break
        if lista_mov == [1]:
            carta_ant = baralho[index_selec-1]
            baralho = mecanicas.empilha(baralho, index_selec, (index_selec-1))
        if lista_mov == [3]:
            carta_terc_ant = baralho[index_selec-3]
            baralho = mecanicas.empilha(baralho, index_selec, (index_selec-3))
        if lista_mov == [1, 3]:
            carta_ant = baralho[index_selec-1]
            carta_terc_ant = baralho[index_selec-3]
            print('Sobre qual carta você quer empilhar o {}?'.format(carta_selec))
            print('1. {}'.format(carta_ant))
            print('2. {}'.format(carta_terc_ant))
            numero_digitado = int(input('Digite 1 ou 2: '))
            if numero_digitado == 1:
                baralho = mecanicas.empilha(baralho, index_selec, (index_selec-1))
            if numero_digitado == 2:
                baralho = mecanicas.empilha(baralho, index_selec, (index_selec-3))
    if len(baralho) == 1:
        print('Parabéns você venceu!')
    if len(baralho) != 1:
        print('Treine mais, você perdeu.')
    muda = input('Você quer jogar novamente (s/n)? ')
    if muda == 's':
        liga = True
    if muda != 's':
        liga = False