
                                                                                 
n1=float(input("informe sua 1 nota: "))
n2=float(input("informe sua 2 nota: "))
n3=float(input("informe sua 3 nota: "))
soma=(n1+n2+n3)/3
print(soma)

if (soma<7):
    print('você esta de recuperação')
if (soma>7):
    print('você foi aprovado')