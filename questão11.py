#Dupla: Maria Lívia do Nascimento Sousa e Laura de Souza Cruz
#11. Crie uma tupla que contenha 10 números inteiros. 
#11.1. Imprima o quinto número da tupla utilizando o índice.
#11.2. O que acontece se eu executar o comando print(tupla[-1])?
#11.3. Use a fatiação para imprimir os números de 3 a 7.
#11.4. Altere o 4o elemento de sua tupla para o valor 578.
#11.5. Calcule a média de todos os elementos de sua tupla.

tupla_int = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("o quinto número é: ", tupla_int[4])
print(tupla_int[-1])
print("números de 3 a 7: ", tupla_int[2:7])
media = sum(tupla_int)/len(tupla_int)
print("A média da tupla dos números inteiros é: ", media)

tupla2 = (1, 2, 3, 4, 578, 6, 7, 8, 9, 10)
print("o quinto número é: ", tupla2[4])
print(tupla2[-1])
print("números de 3 a 7: ", tupla2[2:7])
media = sum(tupla2)/len(tupla2)
print("A média da segunda tupla é: ", media)
