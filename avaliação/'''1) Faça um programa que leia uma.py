#1) Faça um programa que leia uma
#quantidade indeterminada de números positivos e conte quantos deles estão nos
#seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados
#-9deverá terminar quando for lido um número negativo.

'''z=0
v=0
c=0
s=0
n=0


while(n<4):
    k=float(input('informe um valor positivo menor que 100: '))
    if(k>0):
        l=k
    if (k<0):
        n=4
        print('o seu numero é negativo')
if l<0:
    print('o valor é negativo')
    if (l>=0)and(l<=26):
        z+=1
        print('seu numero esta no intervalo de 0 a 25')
    if (l>=25)and(l<=51):
        v+=1
        print('o seu numero está no intervalo de 26 a 50')
    if (l>=50)and(l<=76):
        c+=1
        print('o seu numero esta no intervalo de 51 a 75')
    if (l>=75)and(l<=101):
        s+=1
        print('o seu numero esta no intervalo de 76 a 100')
print (z,'foram a quantidade de numeros no intervalo de 0 a 25')
print (v,'foram a quantidade de numeros no intervalo de 26 a 50')
print (c,'foram a quantidade de numeros no intervalo de 51 a 75')
print (s,'foram a quantidade de numeros no intervalo de 76 a 100')'''

#2)Em uma eleição presidencial existem quatro candidatos. Os votos são informados por
#meio de código. Os códigos utilizados são:
#1 , 2, 3, 4 - Votos para os candidatos associados (você deve montar uma tabela 
#ex: 1 - José/ 2- João /3 - Maria/ 4 - Meu nego) 5 - Voto Nulo 6 - Voto em Branco

#Faça um programa que calcule e mostre:
#- O total de votos para cada candidato;
#- O total de votos nulos;
#- O total de votos em branco;

#A percentagem de votos nulos sobre o total de votos;
#A porcentagem de votos em branco sobre o total de votos. 
#Para finalizar o algoritmo, o valor digitado deve ser igual a 0.

k=0
jos=0
joã=0
mar=0
men=0
vn=0
vb=0
coletor_de_dados=0

while(k<4):
    l=int(input('infome o seu candidatode acordo com as cegintes informação:  1 - José/ 2- João /3 - Maria/ 4 - Meu nego 5) - Voto Nulo 6 - Voto em Branco:   '))
    if(l<7):
        print('FIM')
    if(l==1):
        jos+=1
    if(l==2):
        joã+=1
    if(l==3):
        mar+=1
    if(l==4):
        men+=1
    if(l==5):
        vn+=1
    if(l==6):
        vb+=1
    if(l>0):
        k+=1
    if(l>6):
        print('numero invalido,tente novamente')

print ('josé = ',jos,)
print('João = ',joã)
print('maria = ',mar)
print('meu nego = ',men)
print('votos nulos = ',vn)
print('votos brancos',vb)
print('total de votos',k)






#3) Faça um algoritmo que receba a sigla da cidade de origem de 
# um grupo de pessoas, ao final informe
# quantas foram digitalizadas das cidades do Rio de Janeiro
#, Belo Horizonte e Santa Catarina (separadamente). O algoritmo encerra 
# quando digitado a palavra “fim”.

outro=0
n=0
ro=0
rj=0
sc=0
while(n<4):
    print('1=Acre (AC)  2=Alagoas (AL)  3=Amapá (AP)  4=Amazonas (AM)  5=Bahia (BA)  6=Ceará (CE)  7=Distrito Federal (DF)  8=Espírito Santo (ES)  9=Goiás (GO)  10=Maranhão (MA)  11=Mato Grosso (MT)  12=Mato Grosso do Sul (MS)  13=Minas Gerais (MG)  14=Pará (PA)  15=Paraíba (PB)  16=Paraná (PR)  17=Pernambuco (PE)  18=Piauí (PI)  19=Rio de Janeiro (RJ)  20=Rio Grande do Norte (RN)  21=Rio Grande do Sul (RS)  22=Rondônia (RO)  23=Roraima (RR)  24=Santa Catarina (SC)  25=São Paulo (SP)  26=Sergipe (SE)  ')
    k=int(input('infome a sigla do seu estado'))
    if (k==24):
        sc+=1
    if (k==19):
        rj+=1
    if (k==22):
        ro+=1
    if (k>0)and(k<19)and(k>19)and(k==23)and(k>14):
        outro=+1
print('pessoas do rj',rj,'pessoas de ro',ro,'pessoas de sc',sc)

