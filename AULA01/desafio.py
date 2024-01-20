

#Com método full passando o numero e o operador e validando dentro do if o tipo de operação com returns do resultado

def calcfull(num1,num2, oper):
    
    if oper=='+': 
            result = num1+num2
            print('Parabéns por ter escolhido uma adição.')
            
    elif oper=='-':      
            result = num1-num2
            print('Parabéns por ter escolhido uma subtração.')
            
    elif oper=='*':      
            result = num1*num2
            print('Parabéns por ter escolhido uma multiplicação.')
            
    elif oper=='/':      
            result = num1/num2            
            print('Parabéns por ter escolhido uma divisão.')
                           
    return result

operador1 = input('Digite o tipo de operação: ')
numm1 = int(input('Insira o primeiro numero : ')  )
numm2 =  int(input('Insira o segundo numero : ')  )

calcfull1 = calcfull(numm1,numm2, operador1)

print ("Método Full ", calcfull1)


#leonardo.moliveira@sp.senac.br

#4 métodos sendo um pra cada operação ,  passando parametro dos numeros sem o operador ,  returns do resultado
def calcsoma(num1,num2):
    
    result = num1+num2
    
    return result


def calcsub(num1,num2):
    
    result = num1-num2
    
    return result


def calcnult(num1,num2):
    
    result = num1*num2
    
    return result

def calcdiv(num1,num2):
    
    result = num1/num2
    
    return result

#chamando o método da calculadora
final1= calcdiv(10,2)

print ("Métodos " , final1)


#cálculos básicos separados
num1 = int(input('Insira o primeiro numero : ')  )
num2 =  int(input('Insira o segundo numero : ')  )
resuladi = num1 + num2
resultsub = num1 - num2
resultmult = num1 * num2
resultdiv = num1 / num2


print ( "Foi realizado uma Adição format {} " .format (resuladi))

print ( "Foi realizada uma Subtração  " , resultsub)

print ( "Você escolheu Multiplicação  " , resultmult)

print ( "Você escolheu Divisão2  %.f"  %resultdiv)
    

#pedindo para o usuário escolher o tipo de operação
tipocalc = input('Digite o tipo de operação: ')
# validação com if e elif para o tipo de operação
if tipocalc=='+':
    resuladi = num1 + num2
    print ( "você escolheu Adição elif " , resuladi)
elif tipocalc=='-':
    resultsub = num1 - num2
    print ( "Você escolheu Subtração  elif" , resultsub)
elif tipocalc=='*':
    resultmult = num1 * num2
    print ( "Você eesoclheu Multiplicação  elif " , resultmult)
elif tipocalc=='/':
    resultdiv = num1 / num2
    print ( "Você escolheu Divisão  elif" , resultdiv)
else:
    print("Você não escolheu nenhuma das 4 opções disponiveis")    

# validação só com if para o tipo de operação
if tipocalc=='+':
    print ( "você escolheu Adição  if" , resuladi)

if tipocalc=='-':
    print ( "Você escolheu Subtração  if" , resultsub)

if tipocalc=='*':
    print ( "Você escolheu Multiplicação  if" , resultmult)

if tipocalc=='/':
    print ( "Você escolheu Divisão  if" , resultdiv)
    
    #--------------------------

"""    
if tipocalc=='+':
    print ( "você escolheu Adição  " , resuladi)

if tipocalc=='-':
    print ( "Você escolheu Subtração  " , resultsub)

if tipocalc=='*':
    print ( "Você escolheu Multiplicação  " , resultmult)

if tipocalc=='/':
    print ( "Você escolheu Divisão  " , resultdiv)

"""

"""

#Fibonacci
n = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1

if (n==1) or (n==2):
    print("1")
else:
    for count in range(2,n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo)
    
    

# numeros primos
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(number, 'não é primo')
            break
    else:
        print(number, 'é primo')
elif number == 0:
    print(number, 'é zero')
elif number == 1:
    print(number, 'é um')
else:
    print(number, 'é negativo')
    
    """