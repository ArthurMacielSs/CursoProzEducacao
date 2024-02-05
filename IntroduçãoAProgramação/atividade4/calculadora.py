""" Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá 
a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0."""

def soma(n1,n2):
    return n1+n2
def subrt(n1,n2):
    return n1-n2
def divisao(n1,n2):
    return n1/n2
def multiply (n1, n2):
    return n1*n2

print("digite dois numeros que você quer fazer a operação")
numero1 =int(input("digite o primeiro"))
numero2 =int(input("digite o segundo"))
print("digite a operação desejada de acordo com essa tabela")
print("1. Soma \n2. Subtração \n3. Multiplicação \n4. Divisão")
op=int(input())

if(op==1):
    result=soma(numero1,numero2)
elif(op==2):
    result=subrt(numero1,numero2)
elif(op==3):
    result=multiply(numero1,numero2)
elif(op==4):
    result=divisao(numero1,numero2)
else:
    result=0
print(" o resultado eh ",result)