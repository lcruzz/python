class pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
    def saudacao(self):
        print("Bem vinde", self.nome, "\nSua idade é:", self.idade, "\nSeu e-mail é:", self.email)

humano = pessoa(nome = input("Digite seu nome: "), idade = int(input("Digite sua idade: ")), email = input("Digite seu email: "))
humano.saudacao()


