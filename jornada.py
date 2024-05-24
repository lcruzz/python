vida = 22

while vida > 0:
    print("Sua vida atual é", vida)
    jornada = int(input("Digite 1 para deserto \nDigite 2 para floresta \nDigite 3 para montanha \nDigite 4 para oásis \nInforme por qual lugar você passou: "))   
    
    if jornada == 1:
        vida = vida-10
    
    elif jornada == 2:
        vida = vida-6
    
    elif jornada == 3:
        vida = vida-8
    
    elif jornada == 4:
       vida = vida+15

else:
    print("Fim da Jornada.")
