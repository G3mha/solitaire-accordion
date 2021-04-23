import random
import mecanicas

interrupitor = True
while interrupitor == True:
    lista_numeros = range(1, 53)
    interrupitor = False
    print('Paciência Acordeão\n==================\nSeja bem-vindo(a) ao jogo de Paciência Acordeão!\nO objetivo deste jogo é colocar todas as cartas em uma mesma pilha.\nExistem apenas dois movimentos possíveis:\n1. Empilhar uma carta sobre a carta imediatamente anterior;\n2. Empilhar uma carta sobre a terceira carta anterior.\nPara que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:\n1. As duas cartas possuem o mesmo valor\n2. As duas cartas possuem o mesmo naipe.\nDesde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.\nAperte [Enter] para iniciar o jogo...')
    a = input('')
    if a == '':
        baralho = mecanicas.cria_baralho()
        pode_mover = True
        while pode_mover == True:
            print('O estado atual do baralho é:')
            for i in range(max(lista_numeros)):
                ind = lista_numeros[i]
                cart = baralho[i]
                print('{0}. {1}'.format(ind, cart))
            while True:
                index_selec = int(input('Escolha uma carta (digite um número entre 1 e {}): '.format(index_selec))) - 1
                carta_selec = baralho[index_selec]
                lista_mov = lista_movimentos_possiveis(baralho, carta_selec)
                if lista_mov == [1]:
                    carta_ant = baralho[posicao-1]
                    baralho = empilha(baralho, index_selec, carta_ant)
                if lista_mov == [3]:
                    carta_terc_ant = baralho[posicao-3]
                    baralho = empilha(baralho, index_selec, carta_terc_ant)
                if lista_mov == [1, 3]:
                    carta_ant = baralho[posicao-1]
                    carta_terc_ant = baralho[posicao-3]
                    print('Sobre qual carta você quer empilhar o {}?'.format(carta_selec))
                    print('1. {}'.format(carta_ant))
                    print('2. {}'.format(carta_terc_ant))
                    numero_digitado = int(input('Digite 1 ou 2: '))
                    if numero_digitado == 1:
                        baralho = empilha(baralho, index_selec, carta_ant)
                    if numero_digitado == 2:
                        baralho = empilha(baralho, index_selec, carta_terc_ant)
            pode_mover = mecanicas.possui_movimentos_possiveis(baralho)


    muda = input('Você quer jogar novamente (s/n)? ')
    if muda == 's':
        interrupitor = True