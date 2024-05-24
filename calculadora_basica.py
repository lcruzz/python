num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
operacao = int(input('Digite 1 para adição \nDigite 2 para subtração \nDigite 3 para multiplicação \nDigite 4 para divisão \nInforme qual operação deseja realizar: '))

if operacao == 1:
    resultado = num1 + num2
    print('O resultado da soma é', resultado)

elif operacao == 2:
    resultado = num1 - num2
    print('O resultado da subtração é', resultado)

elif operacao == 3:
    resultado = num1 * num2
    print('O resultado da multiplicação é', resultado)

elif operacao == 4 and num2 == 0:
    print('É impossivel dividir por 0.')

elif operacao == 4 and num2 != 0:
    resultado = num1/num2
    print('O resultado da divisão é', resultado)

else:
    print('Operação invalida.')











