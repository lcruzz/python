pokemon = int(input("Digite 1 para tipo água \nDigite 2 para tipo voador \nDigite 3 para tipo terrestre \nQual tipo de pokemon você vai infrentar?: "))

if pokemon == 1 or pokemon == 2:
    print("Escolha o Pikachu para enfrentar seu oponente!")

elif pokemon == 3:
    print("Para enfrentar um pokémon de tipo terrestre recoemendo os pokémon de tipos que são sua fraquesa: \nGreninja - Tipo água \nChespin - Tipo planta \nTalonflame - Tipo voador")

else:
    print("Pokémon invalido.")
    