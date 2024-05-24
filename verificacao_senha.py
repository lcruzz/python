senha = input("Digite sua senha: ")
senha2 = input("Confirme sua senha: ")

if senha == senha2:
    print("Senha correta.")

while senha != senha2:
        print("Senha incorreta. Digite novamente.")
        senha = input("Digite sua senha: ")
        senha2 = input("Confirme sua senha: ")
        if senha == senha2:
            print("Senha correta.")