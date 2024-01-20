saldo = 100

while saldo != 0:
    print('Você ficou com o saldo ', saldo)
    saque = int(input("VALOR SAQUE: "))
    
    
    if (saque <= saldo):  
       print("Saque maior que o saldo disponível. Tente novamente.")
       saldo = saldo - saque
    else:
        print(" teste saque novamente")

