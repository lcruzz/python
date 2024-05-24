import math

class calculadora:
    def __init__(self):
        pass
    
    def soma(self, num1, num2):
        return num1 + num2
    
    def subtracao(self, num1, num2):
        return num1 - num2  
    
    def multiplicacao(self, num1, num2):
        return num1 * num2 
    
    def divisao(self, num1, num2):
        if (num2 != 0):
            return num1/num2
        else:
            return("impossivel dividir por 0")
    
    def raiz(self, num1):
        return math.sqrt(num1)
    
    def cacular(self):
        operacao = input("1. Adição \n2. Subtração \n3. Multiplicação \n4. Divisão \n5. Raiz quadrada \nInforme a operação: ")
        num1 = float(input("Informe o número: "))

        if operacao == "1":
            num2 = float(input("Informe o segundo número: "))
            resultado = self.soma(num1, num2)
        
        elif operacao == "2":
            num2 = float(input("Informe o segundo número: "))
            resultado = self.subtracao(num1, num2)
        
        elif operacao == "3":
            num2 = float(input("Informe o segundo número: "))
            resultado = self.multiplicacao(num1, num2)
        
        elif operacao == "4":
            num2 = float(input("Informe o segundo número: "))
            resultado = self.divisao(num1, num2)
        
        elif operacao == "5":
            resultado = self.raiz(num1)

        print("O resultado é", resultado)
            
resultadocalc = calculadora()
resultadocalc.cacular()