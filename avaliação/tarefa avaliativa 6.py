v1=float(input('insira o primeiro: '))
v2=float(input('insira o segundo valor: '))
v3=float(input('insira o terceiro valor:'))
if(v1<v2<v3):
    print(v1,v2,v3)
if(v1<v3<v2):
    print(v1,v3,v2)
if(v2<v1<v3):
    print(v2,v1,v3)
if(v2<v3<v1):
    print(v2,v3,v1)
if(v3<v2<v1):
    print(v3,v2,v1)
if(v3<v1<v2):
    print(v3,v1,v2)
if(v1==v2==v3):
    print('todos os valores são iguais')
