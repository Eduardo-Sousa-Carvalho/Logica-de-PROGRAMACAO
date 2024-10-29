impar=0
par=0
for i in range(10):
    valor=int(input('informe um numero '))
    if(valor%2==0):
        par=par+1
    else:
        impar=impar+1
print('pars : ',par)
print('impares :',impar)

