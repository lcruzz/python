#Dupla: Maria Lívia do Nascimento Sousa e Laura de Souza Cruz
#12. Escreva um programa em Python que gere uma lista com 6 números inteiros aleatórios, entre 1 e 60, e exiba estes números para o usuário.
#12.1. Modifique o programa para exibir os números da lista em ordem crescente.
#12.2. Modifique o programa ainda mais para exibir, além dos números da lista, o maior e o menor valor.
#12.3. Inclua no programa um código que remova quaisquer números duplicados da lista.
#12.4. Agora, verifique se a lista ainda contém 6 números. Caso contrário, gere mais números aleatórios para completá-la, repetindo as funcionalidades implementadas anteriormente.

import random

class Numeros:
    def __init__(self):
        self.numeros_sorteados = []
    
    def gerar_numeros(self):
        self.numeros_sorteados = random.sample(range(1, 61), 6)
        self.numeros_sorteados.sort()
    
    def resultado(self):
        return self.numeros_sorteados
    
numeral = Numeros()
numeral.gerar_numeros()
numeros_sorteados = numeral.resultado()
maior = max(numeros_sorteados)
menor = min(numeros_sorteados)

print("Os números sorteados foram:", numeros_sorteados)
print("O maior número é", maior)
print("O menor número é", menor)