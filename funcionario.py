class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
    
    def calcular_bonus(self):
        return self.salario * 0.10
    
    def dados(self):
        bonus = self.calcular_bonus()
        print(self.nome,"seu bônus é de:", bonus)

class Gerente(Funcionario):
    def __init__(self, nome, cargo, salario):
        super().__init__(nome, cargo, salario)
    
    def calcular_bonus(self):
        return self.salario * 0.15
    
    def dados(self):
        super().dados()

class Vendedor(Funcionario):
    def __init__(self, nome, cargo, salario):
        super().__init__(nome, cargo, salario)
    
    def calcular_bonus(self):
        return (self.salario * 0.05) + 500
    
    def dados(self):
        super().dados()

funcionario1 = Funcionario("Cla", "Feirante", 2000)
gerente1 = Gerente("Livia", "Gerente", 10000)
vendedor1 = Vendedor("Hugo", "Vendedor", 1600)

funcionario1.dados()
gerente1.dados()
vendedor1.dados()
