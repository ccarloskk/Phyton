import random
import string

while True:
    print('-----BEM-VINDO AO GERADOR DE SENHA-----')
    n = int(input('-Digite o tamanho da senha que deseja: '))
    maiuscula = input('S/N. Você precisa de letra maiúscula? ').strip().lower()#Pergunta ao usuario se deseja letra maiúscula na senha.

    senha = ''
    caracteres = string.digits + string.punctuation + string.ascii_lowercase #Sistema básico com números, caracteres especiais e letras minúsculas

    if maiuscula == 's':
        caracteres += string.ascii_uppercase #Adiciona letra maiúscula na senha.
    
    # Gera a senha com o comprimento especificado
    for _ in range(n):
        senha += random.choice(caracteres)
    
    print(f'A sua senha é: {senha}')

    # Pergunta ao usuário se deseja continuar
    fechar = input('S/N. Deseja continuar o programa?: ').strip().lower()

    if fechar == 'n':
        print('Programa encerrado.')
        break
    else:
        print('Programa continuará.')
