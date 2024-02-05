qtd_rodas=4
peso_bruto=400
qtd_pessoas=11

if(qtd_rodas==2 or qtd_rodas==3):
    print("sua categoria eh a A")
elif(qtd_pessoas<=8 and peso_bruto<3500):
    print("sua categoria eh a B")
elif(peso_bruto>=3500 and peso_bruto<=6000):
    print("sua categoria eh a C")
elif(qtd_pessoas>8):
    print("sua categoria eh a D")
elif(peso_bruto>6000):
    print("seu veiculo eh da categoria E")
else:
    print("veiculo invalido")