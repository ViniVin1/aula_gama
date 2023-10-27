#!/usr/bin/env python
# coding: utf-8

# In[40]:


funcionarios = {}


# In[41]:


funcionarios


# In[46]:


def cadastrar():
    nome = input("Digite o nome a ser cadastrado: ")
    idade = int(input("Digite a idade: "))
    funcao = input("Digite a função: ")
    
    funcionarios[len(funcionarios)+1] = [nome, idade, funcao]
    return print("Usuário cadastrado")
    
def ler_tudo():
    for x in funcionarios.values():
        print(x)
    
def ler_id():
    id = int(input('Digite o id a ser buscado: '))
    
    return print(funcionarios[id])
    
def deletar_func(id):
    funcionarios.pop(id)
    
    return print("Funcionário deletado")

def deletar_campo(id, campo):
    funcionarios[id].pop(campo)
    
    return print("Campo Deletado")
    
def modificar(id, campo, novo):
    funcionarios[id][campo] = novo
    
    return print("Campo alterado")


# In[43]:


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
            cadastrar()
        
        elif escolha == '2':
            print('-------------------------------------')
            ler_tudo()
            
        elif escolha == '3':
            print('-------------------------------------')
            print("Ler registro por ID");
            ler_id()
            
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
                    modificar(id, 0, nome)
                case '2':
                    idade = int(input('Insira a nova idade: '))
                    modificar(id, 1, idade)
                case '3':
                    funcao = input('Insira a nova função: ')
                    modificar(id, 2, funcao)
        
        elif escolha == '5':
            print('-------------------------------------')
            print("Excluir Registro por ID");
            id = int(input('Insira o ID: '))
                
                
            print("1- Excluir funcionário")
            print("2 - Excluir campo específico")
            opt = input("Escolha a opção: ")
                
            match opt:
                case "1":
                    deletar_func(id)
                        
                case "2":
                    print("1- Excluir o Nome")
                    print("2 - Excluir a Idade")
                    print("3 - Excluir a Função")
                    campo = input("Insira a opção que deseja excluir: ")
                        
                    match campo:
                        case "1":
                            deletar_campo(id, 0)
                        case "2":
                            deletar_campo(id, 1)
                        case "3":
                            deletar_campo(id, 2)
                            
        elif escolha == '6':
            print('-------------------------------------')
            print("Saindo...")
            break
        
        else:
            print('-------------------------------------')
            print("Valor incorreto. Tente novamente")


# In[45]:


programa()

