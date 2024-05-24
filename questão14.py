#Dupla: Maria Lívia do Nascimento Sousa e Laura de Souza Cruz
#14. Crie um dicionário que armazene o nome e o telefone de 5 contatos. Escreva um programa que permita ao usuário buscar o telefone de um contato pelo nome.

contatos = {
    "hugo": "(85) 92851-5532",
    "pamela": "(85) 93524-4713",
    "isabelly": "(85) 93382-7517",
    "kelly": "(85) 92451-6171",
    "diogo": "(85) 92832-2411",
}

nome = input("Lista de contatos: \n- Hugo \n- Pamela \n- Isabelly \n- Kelly \n- Diogo \nQual contato você deseja saber? ").lower()

if nome in contatos:
    contatos = contatos[nome]
    print("O número de", nome, "é", contatos)
else:
    print("Contato não encontrado.")