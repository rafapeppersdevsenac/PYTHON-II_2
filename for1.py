
""""
lista = [1, 2, 3, 4, 5]
contador = 0

for item in lista:
    contador = contador + 1 
    print("Item For = " ,  item , " ************************ O Próximo é o contador ! ")
    print("                 Contador : "  ,     contador ) ; 
        
sequencia = [1, 2, 3, 4, 5]    
for item in sequencia:
    print(item)
else:
    print('Todos os items foram exibidos com sucesso')
    """
        
    
notas = {
    'Potuguês': 7, 
    'Matemática': 9, 
    'Lógica': 7, 
    'Algoritmo': 7
}

for chave, valor in notas.items():
    print(f"{chave}: {valor}")