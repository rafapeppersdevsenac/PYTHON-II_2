#com while para finalizar o programa quando a pessoa escrever sair 
operacao = input('Digite o que você quer fazer ou sair para sair do programa: ')

while operacao != "sair": 
  numero1 = input("Digite o primeiro numero: ")
  numero2 = input("Digite o segundo numero: ")

  if operacao == "soma":
    resultado = int(numero1) + int(numero2)  
  if operacao == "sub":
    resultado = int(numero1) - int(numero2)
  if operacao == "mult":
    resultado = int(numero1) * int(numero2)
  if operacao == "div":
    resultado = int(numero1) / int(numero2)
  else:
    resultado = "operador não suportado, use soma, sub, mult ou div."

  print("O resultado da operação é: " + str(resultado))
  print("---------------------------------------")