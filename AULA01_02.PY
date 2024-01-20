    ##se a média foi  >= 7 aprovado
#se a média for 4 , 6 recuperação
# senão reprovado 

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a qauarta nota: '))

#notafull = [nota1, nota2, nota3, nota4]

#print (notafull)

if nota1 >10:
    
while (nota1 > 10 or nota2 > 10 or nota3 > 10 or nota4 > 10 ) : 
    print  ('Digite uma nota válida!! ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    nota04 = float(input('Digite a qauarta nota: '))

else:   

    media = (nota1 + nota2 + nota3 + nota4) / 4

    if media >= 7:
        print('Sua média final foi : {}' .format(media) , ' e você esta aprovado')
    elif media >= 4: 
        print('Sua média final foi : %1.f'  %media , ' e você esta de recuperação')
    else: 
        print('Sua média final foi : ' , media , ' e você esta reprovado')
    
    
    
    
    