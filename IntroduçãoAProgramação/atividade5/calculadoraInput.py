'''Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. 
No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. 
Quando o usuário escolher a opção “Sair”, o sistema irá parar.

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. '''


def calculator (op, n1, n2):
    if(op==1):
        result= n1+n2
    elif(op==2):
        result= n1-n2
    elif(op==3):
        result= n1*n2
    elif(op==4):
        result=n1/n2
    else:
        print("\nEssa opção não existe")
        return 12
    return result

op=1
while(op!=0): 
    print("\ndigite a operação desejada de acordo com essa tabela")
    print("1. Soma \n2. Subtração \n3. Multiplicação \n4. Divisão \n0.sair ")
    op=int(input())
    if(op==0):
        print("\nsaindo...")
        break 
    print("\n \ndigite dois numeros que você quer fazer a operação")
    numero1 =int(input("\ndigite o primeiro"))
    numero2 =int(input("\ndigite o segundo"))
   
    resultado =calculator(op,numero1,numero2)
    if (resultado !=12):
        print("\no resultado eh ", resultado)