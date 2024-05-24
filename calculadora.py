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
    
    def cacular(self):
        operacao = input("1. Adição \n2. Subtração \n3. Multiplicação \n4. Divisão \nInforme a operação: ")
        num1 = float(input("Informe o primeiro número: "))
        num2 = float(input("Informe o segundo número: "))

        if operacao == "1":
            resultado = self.soma(num1, num2)
        
        elif operacao == "2":
            resultado = self.subtracao(num1, num2)
        
        elif operacao == "3":
            resultado = self.multiplicacao(num1, num2)
        
        elif operacao == "4":
            resultado = self.divisao(num1, num2)
        
        print("O resultado é", resultado)
            
resultadocalc = calculadora()
resultadocalc.cacular()