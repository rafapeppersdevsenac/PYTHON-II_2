class Dados1:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
    

nome1 = input("Digite o seu nome: ")
cpf1 = input("Digite o seu cpf: ")
idade1 = int(input("Digite a sua idade: "))
    
dados = Dados1(nome1, cpf1, idade1)

print (dados.nome)
print (dados.cpf)
print (dados.idade)