import random  
import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
dinheiro = {}
deposito = 10

while True:
    print(' ____________________')
    print('| Bem vindo ao jogo  |')
    print('|                    |')
    print('|  1- Jogar          |')
    print('|                    |')
    print('|  2- Depositar      |')
    print('|                    |')
    print('|  3- Regras         |')
    print('|                    |')
    print('|  4-Sair            |')
    print('|____________________|')
    opcao  = int(input('Digite a opçao que deseja: '))

    if opcao == 1:
        limpar_tela()
        print(' ___________________________________________________')
        print('|     Bem vindo                                     |')
        valor = float(input('|Insira o valor que deseja apostar: R$'))
        print('|                                                   |')
        print(' ___________________________________________________')

        if valor > deposito:
            print('ERRO de saldo, tente outro valor!!!')

        if valor <= deposito:
            limpar_tela()

            while True:
                resul_maqui = random.randint(2, 11)
                print(f'Máquina tirou {resul_maqui}')

                resul_usuario = resul_maqui = random.randint(1, 11)
                print(f'Você tirou {resul_usuario}')

                desistir = int(input('Deseja encerrar a aposta? (1-sim/2-nao): '))

                if desistir == 1:
                    limpar_tela()
                    resul_maqui2 = random.randint(2, 11)

                    soma_maqui = resul_maqui2 + resul_maqui2

                    print('')
                    print(f'Máquina tirou {resul_maqui2}')
                    print('')
                    print(f'Pontuaçao geral')
                    print(f'Casa pontuaçao: {soma_maqui}')
                    print(f'Sua pontuaçao: {resul_usuario} ')

                    if soma_maqui > resul_usuario:
                        print('Voce perdeu a aposta!!')
                        print(f'Perca de: R${valor}')

                elif desistir == 2:

                    resul_maqui2 = random.randint(2, 11)

                    soma_maqui = resul_maqui2 + resul_maqui2

                    print('')
                    print(f'Máquina tirou {soma_maqui}')
                    print('')
                    print(f'Pontuaçao geral')
                    print(f'Casa pontuaçao: {soma_maqui}')
                    print(f'Sua pontuaçao: {resul_usuario} ')
                    print('')

                    resul_maqui3 = random.randint(2, 11)
                    print(f'Máquina tirou {resul_maqui}')

                    resul_usuario2 = resul_maqui = random.randint(1, 11)
                    print(f'Você tirou {resul_usuario}') 
                    



                break
            


                

    elif opcao == 2:
        print

    elif opcao == 3:
        print

    elif opcao == 4:
        print



#criar um for que conte ate o momento que o usuario decida parar, ou que passe do limite da regra do jogo, que no caso é o número 21