def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida")
    return a / b

# Exemplo de uso
try:
    resultado = dividir(10, 0)
    print(resultado)
except ZeroDivisionError as e:
    print("Ocorreu um erro:", e)
