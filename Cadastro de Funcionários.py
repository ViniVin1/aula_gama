# Dicionário que vai armazenar os valores
funcionarios = {}

# Função para cadastrar um novo funcionário
def cadastrar():
    nome = input("Digite o nome a ser cadastrado: ")
    idade = int(input("Digite a idade: "))
    funcao = input("Digite a função: ")
    
    funcionarios[len(funcionarios)+1] = [nome, idade, funcao]
    return print("Usuário cadastrado")

# Função que exibe os valores do dicionário
def ler_tudo():
    for x in funcionarios.values():
        print(x)

# Função que retorna apenas o funcionário selecionado    
def ler_id():
    id = int(input('Digite o id a ser buscado: '))
    
    return print(funcionarios[id])

# Função que deleta todos os valores pelo id
def deletar_func(id):
    funcionarios.pop(id)
    
    return print("Funcionário deletado")

# Função que deleta apenas o campo escolhido
def deletar_campo(id, campo):
    funcionarios[id].pop(campo)
    
    return print("Campo Deletado")

# Função que altera o campo escolhido
def modificar(id, campo, novo):
    funcionarios[id][campo] = novo
    
    return print("Campo alterado")


# Função principal
def programa():
    escolha = ""
    while escolha != 6:
        print('-------------------------------------')
        print("Escolha a opção abaixo")
        print("1 - Cadastrar Usuário")
        print("2 - Ler todos os registros")
        print("3 - Ler Registro por ID")
        print("4 - Modificar Registro por ID")
        print("5 - Excluir Registro por ID")
        print("6 - Sair")
        
        escolha = input("Escolha o número desejado: ")
        
        if escolha == '1':
            print('-------------------------------------')
            print("Cadastrar Usuário")
            cadastrar() # Chamamento da função cadastrar()
        
        elif escolha == '2':
            print('-------------------------------------')
            ler_tudo() # Chamamento da função ler_tudo()
            
        elif escolha == '3':
            print('-------------------------------------')
            print("Ler registro por ID");
            ler_id() # Chamamento da função ler_id()
            
        elif escolha == '4':
            print('-------------------------------------')
            print("Modificar Registro por ID");
            print("1 - Modificar o Nome")
            print("2 - Modificar a Idade")
            print("3 - Modificar a Função")

            id = int(input('Insira o ID: '))
            mod = input("Escolha a opção que deseja modificar: ")

            match mod:
                case '1':
                    nome = input('Insira o novo nome: ')
                    modificar(id, 0, nome) # Chamamento da função modificar() com os parâmetros necessários
                case '2':
                    idade = int(input('Insira a nova idade: '))
                    modificar(id, 1, idade) # Chamamento da função modificar() com os parâmetros necessários
                case '3':
                    funcao = input('Insira a nova função: ')
                    modificar(id, 2, funcao) # Chamamento da função modificar() com os parâmetros necessários
        
        elif escolha == '5':
            print('-------------------------------------')
            print("Excluir Registro por ID");
            id = int(input('Insira o ID: '))
                
                
            print("1- Excluir funcionário")
            print("2 - Excluir campo específico")
            opt = input("Escolha a opção: ")
                
            match opt:
                case "1":
                    deletar_func(id) # Chamamento da função deletar() com o id a ser deletado
                        
                case "2":
                    print("1- Excluir o Nome")
                    print("2 - Excluir a Idade")
                    print("3 - Excluir a Função")
                    campo = input("Insira a opção que deseja excluir: ")
                        
                    match campo:
                        case "1":
                            deletar_campo(id, 0) # Chamamento da função deletar() com o id e campo a ser deletado
                        case "2":
                            deletar_campo(id, 1) # Chamamento da função deletar() com o id e campo a ser deletado
                        case "3":
                            deletar_campo(id, 2) # Chamamento da função deletar() com o id e campo a ser deletado
                            
        elif escolha == '6':
            print('-------------------------------------')
            print("Saindo...")
            break
        
        else:
            print('-------------------------------------')
            print("Valor incorreto. Tente novamente")


# Chamamento da função principal que inicia o programa
programa()

