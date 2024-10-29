#1) Tendo como dado de entrada a altura (h) de uma pessoa, construa 
# um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62,1*h) - 44,7

'''k=int(input('infome: Homen: 1   Mulher: 2. :  '))
a=float(input('infome a sua altura ? '))

if k == 1:
    ph=(72,7*a) -58
    print('seu peso ideal para você é: ',ph)
if k ==2:
    pm=(62,1*a) -58
    print('seu peso ideal para você é: ',pm)'''


#2) Faça um Programa que pergunte quanto você ganha por 
#hora e o número de horas trabalhadas no mês. Calcule e 
#mostre o total do seu salário no referido mês.

'''n=float(input(" Quanto você recebe por hora ? "))
k=int(input('Quantas horas você trabalhou esse mês ? '))
p=n*k
print('este mês você recebeu',p,' Reais')'''


#3) Faça um programa que leia e valide as seguintes informações:
#Nome: mais de 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

''',
 NBBn=str(input('infome o seu nome completo: '))
k=len(n)
if k<4:
    print('NOME COMPLETO!!!')
i=int(input('infome a sua idade: '))
if i>150 and i<0:
    print ('informe sua idade real')
s=int(input('informe os seu salário mensal: '))
if s<0:
   print('tu ta devendo pra empresa ?')
se=int(input('infome: Homen: 1   Mulher: 2. :  '))
if se<0 and se>2:
   print('isso não existe')
if se=='1':
   se='macho'
else:
   se='mulher'

es=str(input('infome o seu estado de acordo: Soltero=s,Casado=c,Viuvo=v,Divorciado=d'))
if es=='s':
   es='Soltero'
if es=='c':
    es=='Casada'
if es=='v':
   es=='Viuvo'
if es=='d':
   es=='Divorciado'

print(n,'tem',i,'recebe',s,'Reais por mês''é',se,'e está',es)'''




#4) Uma série de Fibonacci é formada pela sequência 
# 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que 
# gere uma série até que o valor seja maior que 500 5

'''pn=0
sn=1
tn=1
x=str(input('aperte a tecla K'))
if x=='k'and x=='K'
    pn+sn=tn
    tn+sn=pn
    pn+sn='''




#5) Faça um programa que peça um número inteiro e determine
# se ele é ou não um número primo. Um número primo é aquele 
# que é divisível somente por ele mesmo e por 1.

''''n=int(input('digite um numero: '))
if n>1:
    for i in range(2,n):
        print('não é primo')
        break
    else:
        print('é numero primo')
        break
else:
    print('não é um numero primo')'''

#6) Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o 
# segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número 
# do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.




#7) Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve 
# perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular
# o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno que utiliza o sistema 
# deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos responderam informar:
#Maior e Menor Acerto;
#Total de Alunos que utilizaram o sistema;
#A Média das Notas da Turma.Gabarito da Prova:

# 01 - A  02 - B  03 - C  04 - D  05 - E  06 - E  07 - D  08 - C  09 - B  10 - A
'''l=0
k=0
n=print('infome o seu nome')
g=print('informe o seu gabarito:')
G1=str(input('1: '))
G2=str(input('2: '))
G3=str(input('3: '))
G4=str(input('4: '))
G5=str(input('5: '))
G6=str(input('6: '))
G7=str(input('7: '))
G8=str(input('8: '))
G9=str(input('9: '))
G10=str(input('10: '))

if G1=='A':
   k=k+1
else:
    l=l+1
if G2=='B':
    k=k+1 
else:
    l=l+1
if G3=='G':
    k=k+1
else:
    l=l+1
if G4=='D':
    k=k+1
else:
    l=l+1
if G5=='E':
    k=k+1
else:
    l=l+1
if G6=='E':
    k=k+1
else:
    l=l+1
if G7=='D':
    k=k+1
else:
    l=l+1
if G8=='C':
    K=k+1  
else:
    l=l+1
if G9=='B':
    k=k+1 
else:
    l=l+1 
if G10=='A':
   k=k+1
else:
    l=l+1
j=k/2
print('você acertou: ',k,'você errou: ',l)
print('sua nota é: ',j)

for i in range(1,5):
    x=str(input('você gostaria de ultilizar o sistema ? '))
    if x=='não'and x=='Não'and x=='NÃO':
        print ('👍')
    if x=='Sim'and x=='sim'and x=='SIM':
        l=0
        k=0
n=print('infome o seu nome')
g=print('informe o seu gabarito:')
G1=str(input('1: '))
G2=str(input('2: '))
G3=str(input('3: '))
G4=str(input('4: '))
G5=str(input('5: '))
G6=str(input('6: '))
G7=str(input('7: '))
G8=str(input('8: '))
G9=str(input('9: '))
G10=str(input('10: '))

if G1=='A':
   k=k+1
else:
    l=l+1
if G2=='B':
    k=k+1 
else:
    l=l+1
if G3=='G':
    k=k+1
else:
    l=l+1
if G4=='D':
    k=k+1
else:
    l=l+1
if G5=='E':
    k=k+1
else:
    l=l+1
if G6=='E':
    k=k+1
else:
    l=l+1
if G7=='D':
    k=k+1
else:
    l=l+1
if G8=='C':
    K=k+1  
else:
    l=l+1
if G9=='B':
    k=k+1 
else:
    l=l+1 
if G10=='A':
   k=k+1
else:
    l=l+1
j=k/2
print('você acertou: ',k,'você errou: ',l)
print('sua nota é: ',j)'''