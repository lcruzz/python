#Dupla: Maria Lívia do Nascimento Sousa e Laura de Souza Cruz
#13. Escreva um programa que solicite ao usuário que insira o nome de cinco países e suas respectivas capitais. Armazene essas informações em um dicionário e, em seguida, imprima o dicionário.

pais_capital = {}

for i in range(5):
    pais = input("Digite o nome do país: ")
    capital = input("Digite o nome da capital do país: ")
    pais_capital[pais]=capital

print("\nOs países e suas capitais são:\n", pais_capital)