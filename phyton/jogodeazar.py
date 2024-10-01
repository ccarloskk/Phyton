import random  
import os
import time 
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def sortea_pontuacao():
    return random.randint(2, 11)

def continuar():
    print('Aperte ENTER, para prosseguir em diante.')
    input('')

def voceperdeu():
    print('Voce perdeu a aposta!!!')
    print('A casa ganhou.')
    print(f'Voce perdeu R${valor}!!')

def voceganhou():
    print('Voce ganhou a aposta!!')
    ganhos = valor * 2
    print(f'Voce ganhou R${ganhos}')

dinheiro = []
ganhos = 0
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
        valor = float(input('|Insira o valor que deseja apostar:R$ '))
        print('|                                                   |')
        print('| __________________________________________________|')
        print('Logo iremos começar as apostas....')
        time.sleep(2)
        limpar_tela()
        if valor > deposito:
            print('ERRO de saldo, tente outro valor!!!')
            
        if valor <= deposito:
            soma_usuario = 0
            soma_casa = 0
            resultado_maquina = 0
            resultado_usuario = 0

            while soma_usuario < 21:
                desicao = int(input('Voce deseja encerrar a aposta (1-sim/2nao)?: '))
                resultado_usuario = sortea_pontuacao()
                soma_usuario += resultado_usuario
                print(f'Voce tirou: {soma_usuario}')
                resultado_maquina = sortea_pontuacao()
                soma_casa += resultado_maquina
                print(f'A casa tirou:{soma_casa}')

                if soma_casa == 21:
                    voceperdeu()
                    
                    continuar()
                    limpar_tela()
                    break

                elif soma_casa >= 22:
                    voceganhou()

                    continuar()
                    limpar_tela()
                    break

                elif soma_usuario == 21:
                    voceganhou()

                    continuar()
                    limpar_tela()

                    break

                elif soma_usuario >= 22:
                    voceperdeu()

                    continuar()
                    limpar_tela()

                elif desicao == 1:
                    print('Voce encerrou a aposta.')
                    
                    if soma_casa >= 22:
                        voceganhou()

                        continuar()
                        limpar_tela()

                        break
                    
                    elif soma_casa == 21:
                        voceperdeu()
                        
                        continuar()
                        limpar_tela()
                        break

                    elif soma_casa > soma_usuario:
                        voceganhou()

                        continuar()
                        limpar_tela()
                        break
                    
                    elif soma_usuario > soma_casa:
                        voceperdeu()
                    
                    elif soma_casa == soma_usuario:
                        print('EMPATE na rodada!!')
                        break
            