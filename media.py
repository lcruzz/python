n1 = float(input("Digite a sua primeira nota: "))
n2 = float(input("Digite a sua segunda nota: "))
n3 = float(input("Digite a sua terceira nota: "))
media = (n1 + n2 + n3)/3

if media >= 8:
    print("Parabéns, você passou de ano e está entre os melhores alunos da turma! Sua média foi", media)

elif media >=6 and media < 8:
    print("Parabéns, você passou! Mas poderia ter se esforçado um pouquinho mais pra estar entre os melhores da turma. Sua média foi", media)

else:
    print("Você está de recuperação. Até janeiro! Sua média foi", media) 
    