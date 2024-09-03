produtos = {}
def cadastro_produto():
     codigo = input("Digite o codigo o produto: ")
     nome = input("Digite o nome do produto: ")
     preco = float(input("Digite o preço de venda: "))
     quantidade = int(input("Digite a quantidade em estoque: "))
     produtos[codigo] = {"Nome" : nome, "preço" : preco, "quantidade" : quantidade}
     print("Produto adicionado com sucesso")
     
def altera_preco():
    novo_preco = float(input("Digite o novo preço: "))
    codigo = input("Entre com o código do produto: ")
    if(codigo in produtos):
        produtos[codigo]["preço"] = novo_preco
        print("Preço alterado!")
        
def pesquisa_produto():
    codigo = input("Digite o codigo: ")
    produtosencontrado = produtos.get(codigo)
    if produtosencontrado:
        print("Produto encontrado")
        print(produtos)
    


while(True):
    print("Menu: ")
    print("1 - Adicionar produto")
    print("2 - Alterar preço produto")
    print("3 - Pesquisar por codigo")
    print("4 - Sair")
    print("----------------------------")
    opcao = int(input("Escolha uma opção: "))
    if(opcao == 1):
        cadastro_produto()
    elif(opcao == 2):
        altera_preco()
    elif(opcao == 3):
        pesquisa_produto()
    elif(opcao == 4):
        break
    else:
        print("Escolha a opção correta")