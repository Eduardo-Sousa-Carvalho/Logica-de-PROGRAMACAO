m=0
l=0
n=0
while(l<25):
    l+=1
    idade=float(input('infome o sua idade: '))
    peso=float(input('infome o seu peso em kg: '))
    altura=float(input('infome a sua altura em metros:'))
    if idade>50:
        m+=1
    else:
        n+=1
print('numero de pessoas com a idade maior que 50: ',m)
print('numero de pessoas com a idade menor que 50: ', n)
