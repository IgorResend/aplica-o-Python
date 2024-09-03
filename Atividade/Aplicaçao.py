aluno = {}
def cadastro_aluno():
     nome = input("Digite o nome do aluno: ")
     data = input("Digite a data de nascimento: ")
     email = (input("Digite o email do aluno: "))
     telefone = float(input("Digite o telefone do aluno: "))
     endereço= input("Insira o endereço: ")
     aluno[nome] = {"Nome" : nome, "preço" : data, "Endereço" :endereço, "Email" :email, "Telefone" :telefone}
     print("Produto adicionado com sucesso")
     
def altera_endereço():
    novo_endereço = input("Digite o novo endereço ")
    endereço = input("Nome do aluno: ")
    if(endereço in aluno):
        aluno[endereço]["preço"] = novo_endereço
        print("Endereço alterado!")
        
def pesquisa_aluno():
    nome = input("Digite o nome: ")
    alunoencontrado = aluno.get(nome)
    if alunoencontrado:
        print("Produto encontrado")
        print(aluno)
    


while(True):
    print("Menu: ")
    print("1 - Insira os dados do aluno: ")
    print("2 - Alterar o endereço do aluno")
    print("3 - Listar todos os alunos")
    print("4 - Sair")
    print("----------------------------")
    opcao = int(input("Escolha uma opção: "))
    if(opcao == 1):
        cadastro_aluno()
    elif(opcao == 2):
        altera_endereço()
    elif(opcao == 3):
        pesquisa_aluno()
    elif(opcao == 4):
        break
    else:
        print("Escolha a opção correta")