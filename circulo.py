import math
class circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return (math.pi * self.raio**2)
    
    def calcular_perimetro(self):
        return (2 * math.pi * self.raio)

Circunferencia = circulo(raio = float(input("Informe o valor do raio: ")))
print ("A área do círculo é", Circunferencia.calcular_area())
print ("O perímetro do círculo é", Circunferencia.calcular_perimetro())