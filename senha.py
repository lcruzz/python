senha = "senha123"
senha2 = input("Digite sua senha: ")

if senha == senha2:
    print("Senha correta.")

while senha != senha2:
        print("Senha incorreta. Digite novamente.")
        senha2 = input("Digite sua senha: ")
        if senha == senha2:
            print("Senha correta.")