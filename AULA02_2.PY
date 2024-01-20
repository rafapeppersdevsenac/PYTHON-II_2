saldo = 100

while saldo != 0:
    print('Você ficou com o saldo ', saldo)
    saque = int(input("VALOR SAQUE: "))
    
    if saque > saldo:
        print("Saque maior que o saldo disponível. Tente novamente.")
        continue  # Volta para o início do loop
        
    saldo = saldo - saque

    if saldo < 0:
        print("Você não tem saldo suficiente, mas ainda tem saldo a sacar.")
        resposta = input("Deseja sacar o valor restante? (s/n): ")
        if resposta.lower() == 's':
            saldo = 0  # Sacar o valor restante
        else:
            break  # Encerra o loop se o usuário não deseja sacar o valor restante

print("Operação concluída. Saldo final: ", saldo)


