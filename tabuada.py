num = int(input("Digite o número da tabuada que deseja: "))
print("Tabuada de", num)
for a in range(1,11):
    resultado = num * a
    print(num, "x", a, "=", resultado)