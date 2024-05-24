idade = int(input("Digite sua idade: "))
patrimonio = float(input("Informe o seu patrimônio: "))

if idade >= 18 and idade <= 30:
    fator_idade = 3
elif idade >= 31 and idade <= 50:
    fator_idade = 6
elif idade >= 51 and idade <= 60:
    fator_idade = 9
else:
    fator_idade = 12
print("O fator idade é ", fator_idade)

if patrimonio <= 50000:
    fator_de_risco = fator_idade + 2
elif patrimonio > 50000 and patrimonio <= 200000:
    fator_de_risco = fator_idade + 1
elif patrimonio > 200000 and patrimonio <= 1000000:
    fator_de_risco = fator_idade - 1
else:
    fator_de_risco = fator_idade - 2

print("O fator de risco é ", fator_de_risco)

juros_anuais = 1.8 + (fator_de_risco)*0.2
print("Os juros anuais serão de ", juros_anuais)

valor_do_emprestimo = float(input("Informe o valor do empréstimo: "))
numero_de_parcelas = int(input("Informe o número de parcelas: "))

mensalidade = (valor_do_emprestimo*(1 + juros_anuais))/numero_de_parcelas
print("a mensalidade será de: ", mensalidade)
