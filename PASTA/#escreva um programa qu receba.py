#escreva um programa qu receba
#com entrada um número e exiba
#uma entrada mensagem informando se ele
#é positivo,negativo ou neutro

n=int(input("informe o valor:"))
if (n<0):
    print('o numero é negativo')
elif(n==0):
    print('o numero é neutro')
if (n>0):
    print('o numero é positivo')
