# array de objetos personalizados
nomes = ['Rafael', 'Artur', 'Karen', 'Júlia']
 
def achar_elemento(arr):
  sair=False
  while(sair == False):
    elemento =str(input("digite o nome que você quer pesquisar e digite sair para fechar o programa "))
    if elemento in arr:
      print("Achamos o nome: " + elemento)
    elif (elemento=="sair"):
      print("fechando o programa")
      sair=True
    else:
      print("Não achamos o nome: " + elemento)
  




   



 
achar_elemento(nomes)

















def manipular_estoque(arr):
  fechar = False
 
  while fechar == False:
    print("O que você deseja fazer? Digite um número: ")
    print("1. Ver produtos em estoque")
    print("2. Alterar produto")
    print("3. Fechar")
    print("------------------------")
    acao = input()
 
    if acao == "1":
      print("------------------------")
      print("Produtos em estoque: ")
      for i in range(len(arr)):
        print(str(i) + "-" + arr[i])
 
    elif acao == "2":
      print("------------------------")
      print("Qual é o índice do produto que eu quero alterar")
      indice = int(input())
      print("Qual é o novo produto?")
      novo_produto = input()
      arr[indice] = novo_produto
      print("Produto " + novo_produto + "adiconado com sucesso")
      print("------------------------")
 
    elif acao == "3":
      print("------------------------")
      print("Fechando o sistema...")
      fechar = True
 
    else:
      print("------------------------")
      print("Por favor informe um código válido (1,2 ou 3)")
      print("------------------------")
 
 
produtos = ["leite", "pão", "manteiga", "queijo"]
manipular_estoque(produtos)





















def manipular_estoque(arr):
  fechar = False
  while(fechar == False):
    print("_______________________")
    print("O que deseja fazer? Digite o número:")
    print("_______________________")
    print("1. Ver produtos em estoque")
    print("2. Alterar produto")
    print("3. Adicionar produto")
    print("4. Fechar o sistema")
    print("_______________________")
    acao = input()
 
 
    if (acao == "1"):
      print("_______________________")
      print("Produtos em estoque: ")
      for i in range (len(arr)):
        print(str(i) + " - " + arr[i])
 
    elif(acao == "2"):
      print("_______________________")
      print("Qual é o índice do produto que deseja alterar?")
      indice = int(input())
      print("Qual é o novo produto?")
      novo_produto = input()
      arr[indice] = novo_produto
      print("Produto '" + novo_produto + "' adicionado com sucesso")
 
    elif(acao == "3"):
      print("_______________________")
      print("Qual produto deseja adicionar?")
      novo_produto = input()
      arr.append(novo_produto)
      print("Produto '" + novo_produto + "' adicionado com sucesso")
 
    elif(acao == "4"):
      print("Fechando sistema...")
      fechar = True
 
    else:
      print("_______________________")
      print("Por favor informe um código válido")
      print("_______________________")
 
produtos = ["leite", "pão", "manteiga", "queijo"]
manipular_estoque(produtos)