saldo = 100

while (saldo!=0): 
    print('Você ficou com o saldo ' ,  saldo )
    saque = int(input("VALOR SAQUE: "))
    saldo = saldo -saque 
    
    if  saldo < 0:
        print("Você não tem saldo suficiente, tente novamente")
        break