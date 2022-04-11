def banknote_selector(valor):
    notas_100 = 0
    notas_50 = 0
    notas_20 = 0
    notas_10 = 0
    notas_5 = 0
    notas_2 = 0

    moedas_1 = 0
    moedas_050 = 0
    moedas_025 = 0
    moedas_010 = 0
    moedas_005 = 0

    soma = 0

    while True:
        soma += 100.0
        if soma > valor:
            soma -= 100.0
            break
        else:
            notas_100 += 1
        

        
    while True:
        soma += 50.0
        if soma > valor:
            soma -= 50.0
            break
        else:
            notas_50 += 1

        
    while True:
        soma += 20.0
        if soma > valor:
            soma -= 20.0
            break
        else:
            notas_20 += 1
            
        
    while True:
        soma += 10.0
        if soma > valor:
            soma -= 10.0
            break
        else:
            notas_10 += 1
            
        
    while True:
        soma += 5.0
        if soma > valor:
            soma -= 5.0
            break
        else:
            notas_5 += 1
            
        
    while True:
        soma += 2.0
        if soma > valor:
            soma -= 2.0
            break
        else:
            notas_2 += 1
            

    while True:
        soma += 1.0
        if soma > valor:
            soma -= 1.0
            break
        else:
            moedas_1 += 1
            
            
    while True:
        soma += 0.5
        if soma > valor:
            soma -= 0.5
            break
        else:
            moedas_050 += 1
            
            
    while True:
        soma += 0.25
        if soma > valor:
            soma -= 0.25
            break
        else:
            moedas_025 += 1
            
            
    while True:
        soma += 0.1
        if soma > valor:
            soma -= 0.1
            break
        else:
            moedas_010 += 1
            
            
    while True:
        soma += 0.05
        if soma > valor:
            soma -= 0.05
            break
        else:
            moedas_005 += 1
            
    if soma < valor:
        soma += 0.05
        moedas_005 += 1
        

    print('Used banknotes:')
    print('- 100:', notas_100)
    print('- 50:', notas_50)
    print('- 20:', notas_20)
    print('- 10:', notas_10)
    print('- 5:', notas_5)
    print('- 2:', notas_2)

    print('\nUsed coins:')
    print('- 1 BRL:', moedas_1)
    print('- 50 cents:', moedas_050)
    print('- 25 cents:', moedas_005)
    print('- 10 cents:', moedas_010)
    print('- 5 cents:', moedas_005)
