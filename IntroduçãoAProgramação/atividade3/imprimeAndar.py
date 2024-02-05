#SOLUÇÃO1
print("EX COM O FOR")
for i in range(20):
    if(i==13):
        continue
    print(i)

#SOLUÇÃO2
print("EX COM O WHILE")
contador =1
while(contador<20):
    if(contador==13):
        contador+=1
        continue
    print(contador)
    contador+=1
    
#SOLUÇÃO3
print("EX A PARTIR DE 20")
contador =20
while(contador>=1):
    if(contador==13):
        contador-=1
        continue
    print(contador)
    contador-=1