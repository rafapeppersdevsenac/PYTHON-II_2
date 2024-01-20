numero_secreto = 82
total_de_tentativas = 3 


for rodada in range (1, total_de_tentativas + 1 ):
    print("Tentativa {:02d} de {:02d}".format(rodada, total_de_tentativas))
    tentativa = int(input("Tente acertar o número de 1 a 100: ")    )
    print("Você digitou : ", tentativa)
    tentativa_int = int(tentativa)
    if (tentativa_int < 1 or tentativa_int > 100):
        print("Somente números de 1 a 100")
        continue
    if tentativa_int == numero_secreto:
        print("Você acertou , o número secreto é : " ,  numero_secreto)  
        break
    else:
        print('Você errou , tente novamente. Você tem mais : ' , total_de_tentativas - rodada, 'tentativas')
        
         
    """
    
    """