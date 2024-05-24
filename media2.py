n1 = float(input("Digite a sua primeira nota: "))
n2 = float(input("Digite a sua segunda nota: "))
n3 = float(input("Digite a sua terceira nota: "))
media = (n1 + n2 + n3)/3

if media >= 6:
    print("Parabéns, você passou de ano! Sua média é", media)

else:
    print("Você está de recuperação. Até janeiro! Sua média é", media) 
    