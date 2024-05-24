vida = 100

while vida > 0:
    print("Sua vida atual é", vida)
    situacao = int(input("Digite 1 para lacaio \nDigite 2 para chefão \nDigite 3 se vocêjá derrotou todos os inimigos \nInforme qual inimigo você quer batalhar ou se você já derrotou todos: "))   
    
    if situacao == 1:
        vida = vida-8
    
    elif situacao == 2:
        vida = vida-11
    
    elif situacao == 3:
        print("Parabéns, você derrotou todos os seus inimigos! Você ficou com", vida, "de vida.")
        break
else:
    print("Você perdeu. Você ficou com", vida, "de vida.")
