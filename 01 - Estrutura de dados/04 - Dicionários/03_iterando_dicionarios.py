contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

for chave, valor in contatos.items():
    print(chave, valor)


""" 
CONTATOS: É o nome da variável que armazena o dicionário.
" {} ": Define um dicionário em Python.
Cada par CHAVE: valor: Representa um contato. A CHAVE é o endereço de E-MAIL e o VALOR é outro dicionário com as informações do contato (NOME e TELEFONE).

====================================================================================
Primeiro loop for:
for chave in contatos:
    print(chave, contatos[chave])

*for chave in contatos*: Itera sobre as chaves do dicionário contatos. A cada iteração, a variável CHAVE(E-MAILS) recebe uma chave diferente.

*print(chave, contatos[chave])*: Imprime a chave (e-mail) e o valor correspondente (dicionário com nome e telefone).
====================================================================================

Segundo loop for:
for chave, valor in contatos.items():
    print(chave, valor)    

*contatos.items()*: Retorna uma lista de tuplas, onde cada tupla contém uma chave e seu valor correspondente.

*for chave, valor in contatos.items()*: Itera sobre essa lista de tuplas, desempacotando cada tupla em duas variáveis: chave e valor.

*print(chave, valor)*: Imprime a chave e o valor, com a mesma funcionalidade do primeiro loop.
====================================================================================

O QUE CADA LOOP FAZ?
Primeiro loop: Itera sobre as chaves e acessa os valores pelo MÉTODO de indexação [].
Segundo loop: Utiliza o MÉTODO items() para obter tanto as chaves quanto os valores diretamente em cada iteração, simplificando o código.

Resultado
Ambos os loops produzem a mesma saída, imprimindo cada contato em um formato     

Em resumo, este código demonstra como criar e iterar sobre um dicionário em Python. A estrutura de dados de dicionário é muito útil para armazenar informações relacionadas, como contatos, configurações, etc. Ao entender como acessar e manipular dicionários, você estará mais preparado para trabalhar com dados complexos em Python.

""" 