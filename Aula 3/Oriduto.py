produtos = {}

i = 3
while True:
 codigo = input("Digite o codigo o produto: ")
 nome = input("Digite o nome do produto: ")
 preco = float(input("Digite o preço de venda: "))
 quantidade = int(input("Digite a quantidade em estoque: "))
 produtos[codigo] = {"Nome" : nome, "preço" : preco, "quantidade" : quantidade}
 print("Produto adicionado com sucesso")
 print(produtos)
 
 i+=3
 
 Opçao = input("1- Repetir 2- Não repetir: ")

 if (Opçao == 1):
    print(produtos)
    break
    
    

