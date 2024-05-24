print("Calcule seu indice de massa corporal!")
peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura em metros: "))
imc = peso/altura**2

if imc < 18.5:
    print("Você está abaixo do peso ideal. Seu imc é", imc)

elif imc >= 18.5 and imc <= 24.9:
    print("Você está com o peso ideal. Seu imc é", imc)

elif imc >= 25 and imc <= 29.9:
    print("Você está com sobrepeso. Seu imc é", imc)

else:
    print("Você está obeso. Seu imc é", imc)
    