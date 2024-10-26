contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221", "idade": "25"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121", "idade": "32"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871", "idade": "20"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766", "idade": "27"},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(telefone)

idade = contatos["chappie@gmail.com"]['idade']
print(idade)

print(contatos["melaine@gmail.com"]["nome"])

#Paraca acessar dicionário aninhado é dicionário[valor][valor]...
#Exemplo: chave = contato, [valor], [valor]...
#Exemplo do exercício  contatos["melaine@gmail.com"]["telefone"] = 3333-7766

