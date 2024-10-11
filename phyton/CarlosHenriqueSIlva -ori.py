import os
import json
lista_aluno = []
lista_professor = []
lista_disciplina = []
lista_matricula = []
lista_turma = []
def limpar_tela():
     os.system('cls' if os.name == 'nt' else 'clear')
   
def menu_principal():
    print('-----------MEN PRINCIPAL-----------')
    print('|(1) Gerenciamento de estudante   |')
    print('|(2) Gerenciamento de professores |')
    print('|(3) Gerenciamento de disciplinas |')
    print('|(4) Gerenciamento de turmas      |')
    print('|(5) Gerenciamento de matriculas  |')
    print('|(9) Sair                         |')
    print('-----------------------------------')
    

def menu_estudante():
    print(' -------- [ESTUDANTES] MENU DE OPERAÇÕES --------')
    print('|                                                |')
    print('|       1-INCLUIR                                |')
    print('|                                                |')
    print('|       2-LISTAR                                 |')
    print('|                                                |')
    print('|       3-ATUALIZAR                              |')
    print('|                                                |')
    print('|       4-EXCLUIR                                |')
    print('|                                                |')
    print('|       5-SAIR                                   |')
    print('|                                                |')
    print(' ------------------------------------------------ ')
    
def menu_professores():
    print(' -------- [PROFESSORES] MENU DE OPERAÇÕES -------')
    print('|                                                |')
    print('|       1-INCLUIR                                |')
    print('|                                                |')
    print('|       2-LISTAR                                 |')
    print('|                                                |')
    print('|       3-ATUALIZAR                              |')
    print('|                                                |')
    print('|       4-EXCLUIR                                |')
    print('|                                                |')
    print('|       5-VOLTAR AO MENU PRINCIPAL               |')
    print('|                                                |')
    print(' ------------------------------------------------ ')

def menu_disciplinas():
        print(' -------- [DISCIPLINAS] MENU DE OPERAÇÕES -------')
        print('|                                                |')
        print('|       1-INCLUIR                                |')
        print('|                                                |')
        print('|       2-LISTAR                                 |')
        print('|                                                |')
        print('|       3-ATUALIZAR                              |')
        print('|                                                |')
        print('|       4-EXCLUIR                                |')
        print('|                                                |')
        print('|                                                |')
        print('|                                                |')
        print(' ------------------------------------------------ ')

def menu_turmas():
        print(' ---------- [TURMAS] MENU DE OPERAÇÕES ----------')
        print('|                                                |')
        print('|       1-INCLUIR                                |')
        print('|                                                |')
        print('|       2-LISTAR                                 |')
        print('|                                                |')
        print('|       3-ATUALIZAR                              |')
        print('|                                                |')
        print('|       4-EXCLUIR                                |')
        print('|                                                |')
        print('|                                                |')
        print('|                                                |')
        print(' ------------------------------------------------ ')

def menu_matriculas():
        print(' -------- [MATRÍCULAS] MENU DE OPERAÇÕES --------')
        print('|                                                |')
        print('|       1-INCLUIR                                |')
        print('|                                                |')
        print('|       2-LISTAR                                 |')
        print('|                                                |')
        print('|       3-ATUALIZAR                              |')
        print('|                                                |')
        print('|       4-EXCLUIR                                |')
        print('|                                                |')
        print('|                                                |')
        print('|                                                |')
        print(' ------------------------------------------------ ')

# Arquivo JSON onde os dados serão salvos
arquivo_json = 'alunos.json'

# Função para carregar os dados do arquivo JSON
def carregar_alunos(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)  # Tente carregar a lista de alunos
    except (FileNotFoundError, json.JSONDecodeError):  # Trate erros de arquivo não encontrado ou de JSON inválido
        return []  # Retorna uma lista vazia se o arquivo não existir ou for inválido

# Função para salvar os dados no arquivo JSON
def salvar_alunos(arquivo, lista_alunos):
    with open(arquivo, 'w') as f:
        json.dump(lista_alunos, f, indent=4)

# Carregar a lista de alunos do arquivo JSON no início do programa
lista_aluno = carregar_alunos(arquivo_json)

while True:
    menu_principal()
    escolha = int(input('Informe a opção que deseja: '))

    if escolha == 9:
        print('-------------------')
        print('|                 |')
        print('|                 |')
        print('|     SAINDO      |')
        print('|                 |')
        print('|                 |')
        print('-------------------')
        break


    #MENU DE ESTUDANTE
    elif escolha == 1:
        limpar_tela()
        while True:
            menu_estudante()
            escolha_estudante = int(input('Digite a opçao que deseja '))    
            
            if escolha_estudante == 1:
                print('Incluir')
                while True:
                    limpar_tela()
                    try:
                        codigo = int(input('Digite o código do aluno(a): '))
                        nome = input('Digite o nome do aluno(a): ')
                        cpf = int(input('Digite o CPF do aluno(a): '))
                        
                        aluno = {
                            'codigo': codigo,
                            'nome': nome,
                            'cpf': cpf
                        }

                        lista_aluno.append(aluno)
                        salvar_alunos(arquivo_json, lista_aluno)
                        limpar_tela()
                        print('Aluno(a) adicionado com sucesso!!')
                        print('Pressione ENTER para seguir ')
                        input()
                        limpar_tela()
                        break
                    except ValueError:
                        print("Entrada errada. Por favor, insira novamente.")
            
            #LISTAR ALUNOS
            elif escolha_estudante == 2:
                    if len(lista_aluno) == 0:
                        print('Nenhum aluno(a) cadastrado!!!')
                    else:
                        print("Lista de alunos:")
                        for i, aluno in enumerate(lista_aluno, start=1):
                            print(f"{i}. Código: {aluno['codigo']}, Nome: {aluno['nome']}, CPF: {aluno['cpf']}")
                        
            #ATUALIZAR ALUNOS
            elif escolha_estudante == 3:
                limpar_tela()
                print('Opçao que deseja atualizar cadastro de alunos(a)')

                codigo_aluno = int(input('Digite o código do aluno(a) que deseja atualizar cadastro: ')) 
                aluno_encontrado = None

                for aluno in lista_aluno:
                    if aluno['codigo'] == codigo_aluno:
                        aluno_encontrado = aluno
                        break

                if aluno_encontrado:
                    print(f"Código: {aluno['codigo']}, Nome: {aluno['nome']}, CPF: {aluno['cpf']}")

                    print('Digite 1 para atualizar código do aluno(a)')
                    print('Digite 2 para atualizar nome do aluno(a)')
                    print('Digite 3 para atualizar CPF do aluno(a)')

                    atualizar_aluno =  int(input('Digite a opçao que deseja escolher: '))
                    
                    if atualizar_aluno == 1:
                        novo_codigo = int(input('Digite o novo código do aluno(a): '))
                        aluno_encontrado['codigo'] = novo_codigo
                    
                    elif atualizar_aluno == 2:
                        novo_nome = input('Digite o novo nome do aluno(a): ')
                        aluno_encontrado['nome'] = novo_nome

                    elif atualizar_aluno == 3:
                        novo_cpf = int(input('Digite o novo CPF do aluno(a): '))
                        aluno_encontrado['cpf'] = novo_cpf
                    
                    else:
                        print('Opçao invalida')   
                        break
                    
                    #salva arquivo de atualizaçao em json
                    salvar_alunos(arquivo_json,lista_aluno)

                    print('Cadastro atualizado!!!')
                    print(f"Código: {aluno['codigo']}, Nome: {aluno['nome']}, CPF: {aluno['cpf']}")

                else:
                    print('Aluno nao encontrado!!.') 
                  
            #EXCLUIR ALUNO      
            elif escolha_estudante == 4:
                limpar_tela()
                print('Opção de excluir alunos(a)')
    
                excluir_aluno = int(input('Digite o código do aluno(a) que deseja excluir: ')) 

                aluno_encontrado = None  # Variável para armazenar o aluno a ser removido

                # Procurar o aluno pelo código
                for i, aluno in enumerate(lista_aluno):
                    if aluno['codigo'] == excluir_aluno:
                        aluno_encontrado = i  # Armazenar o índice do aluno encontrado
                        break

                     # Se o aluno foi encontrado
                if aluno_encontrado is not None:
                 # Remover o aluno encontrado
                    aluno_removido = lista_aluno.pop(aluno_encontrado)
                    print(f"Aluno removido: Código: {aluno_removido['codigo']}, Nome: {aluno_removido['nome']}, CPF: {aluno_removido['cpf']}")
        
                    # Salvar a lista atualizada no arquivo JSON
                    salvar_alunos(arquivo_json, lista_aluno)
                    print('Aluno removido com sucesso!!!')

                else:
                    print('Código de aluno nao indentificado!.')
                limpar_tela()
                
            elif escolha_estudante == 5:
                break  

            else:
                print('Opção inválida. Tente novamente.')        
    #MENU DE ESTUDANTE

    #MENU DE PROFESSOR
    elif escolha == 2:
        limpar_tela()
        while True:
            menu_professores()
            escolha_professor = int(input('Digite a opção que deseja: '))
            
            if escolha_professor == 1:
                print('Incluir')
                while True:
                    limpar_tela()
                    try:
                        codigo = int(input('Digite o código do Professor(a): '))
                        nome = input('Digite o nome do Professor(a): ')
                        cpf = int(input('Digite o CPF do Professor(a): '))
                        
                        professor = {
                            'codigo': codigo,
                            'nome': nome,
                            'cpf': cpf
                        }

                        lista_professor.append(professor)
                        limpar_tela()
                        print('Professor adicionado com sucesso!!')
                        print('Pressione ENTER para seguir ')
                        input()
                        limpar_tela()
                        break
                    except ValueError:
                        print("Entrada errada. Por favor, insira novamente.")
            
            elif escolha_professor == 2:
                if lista_professor:  
                    print("Lista de Professores:")
                for professor in lista_professor:
                    print(f"Código: {professor['codigo']}, Nome: {professor['nome']}, CPF: {professor['cpf']}")
                    break
                else:
                     print('Nenhum professor esta cadastrado ')
                
            
            elif escolha_professor == 3:
                limpar_tela()
                print('Atualizar')

            
            elif escolha_professor == 4:
                limpar_tela()
                print('Excluir')
            
            elif escolha_professor == 5:
                limpar_tela()
                break  

            else:
                print('Opção inválida. Tente novamente.')

    elif escolha == 3:
        limpar_tela() 
        menu_disciplinas()

    elif escolha == 4:
        limpar_tela()
        menu_turmas()

    elif escolha == 5:
         limpar_tela()
         menu_turmas()
