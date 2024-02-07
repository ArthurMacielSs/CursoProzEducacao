"""Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto 
seja preenchido. """
erro = True
while erro:
    try:
        nome = str(input("Digite o seu nome completo: "))
        dataNascimento = int(input("Digite o ano do seu nascimento entre 1922 e 2021: "))
        if dataNascimento < 1922 or dataNascimento > 2021:
            raise ValueError("Você digitou um ano incorreto")
        else:
            idade = 2022 - dataNascimento
            print("Nesse ano de 2022 você:", nome, "completará", idade, "anos")
            erro = False
    except ValueError as err:
        print("Ocorreu um erro:")
        print(err)
        erro = True

        


