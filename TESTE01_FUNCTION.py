# Função para obter uma nota válida no intervalo de 0 a 10
def obter_nota(numero_nota):
    while True:
        try:
            nota = float(input(f"Digite a nota {numero_nota} (de 0 a 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Por favor, digite uma nota válida (de 0 a 10).")
        except ValueError:
            print("Por favor, digite um valor numérico válido.")

# Solicitação de notas ao usuário
nota1 = obter_nota(1)
nota2 = obter_nota(2)
nota3 = obter_nota(3)
nota4 = obter_nota(4)

media = (nota1  + nota2  +  nota3  +  nota4   ) / 4 

if media >=7:
    print('Você esta aprovado e a sua média foi: ' ,  media)

elif media >4:
    print('Você esta em recuperação e a sua média foi: ' ,  media)

else:
    print('Você esta reprovado e a sua média foi: ' ,  media)   

# Calcula a média das notas
media = (nota1 + nota2 + nota3 + nota4) / 4

# Exibe a média
print(f"A média das notas é: {media}")

#$ git config --global user.name"rafapeppersdevsenac"
