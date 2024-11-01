i=0
va=0
vab=0
vam=0
while (i<3):
    i+=1
    va
    print('Bem vindo Senai Pizzas')
    gost=str(input('Gostaria de Fazer um Pedido ? '))
    if gost=='Sim':
        print('digite 1 para tamanho o P: 20R$')
        print('digite 2 para tamanho o M: 30R$')
        print('digite 3 para tamanho o G: 40R$')
        t=int(input('Qual o tamanho você gostaria ? '))
        if t==1:
            va+=20
        if t==2:
            va+=30
        if t==3:
            va+=40
        if t>3:
            ('Invalido')
        print('1:(Calabresa 5R$)')
        print('2:(Mussarela 5R$)')
        print('3:(Tomate 5R$)')
        print('4:(Cebola 5R$)')
        print('5:(Bacon 5R$)')
        sab=int(input('Qual o sabor você gostaria ? '))
        if sab>0 and sab<6:
            va+=5
        else:
            ('Invalido')
        h=str(input('Gostaria de adicionar um sabor ? '))
        if h=='Sim':
            nsa=0
            while (nsa<999):
                nsa+=1
                print('1:(Calabresa 5R$)')
                print('2:(Mussarela 5R$)')
                print('3:(Tomate 5R$)')
                print('4:(Cebola 5R$)')
                print('5:(Bacon 5R$)')
                print('6:Não quero adicionar mais')
                if nsa==1:
                    va+=5
                    nsa=nsa+1
                if nsa==2:
                    va+=5
                    nsa=nsa+1
                if nsa==3:
                    va+=5
                    nsa=nsa+1
                if nsa==4:
                    va+=5
                    nsa=nsa+1
                if nsa==5:
                    nsa=nsa+1
                    va+=5
                if nsa==6:
                    nsa=nsa+10000
                    va+=0
                    nsa+=6
                sab=int(input('Qual o sabor você gostaria de adicionar ? '))
                if nsa==6:
                    va=va+0
        ref=str(input('Gostaria de um Refrigerante ? '))
        if ref=='Sim':
            va+=8
        print('O Valor da compra de ',va,'Reais')
        goss=str(input('Gostaria de fazer outro pedido ? '))
        if goss=='Sim':
            i+=1
        if goss=='Não':
            i+=9999999999
            print('Obrigado a preferencia.')
