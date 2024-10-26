dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

print(dados["nome"])  # "Guilherme"
print(dados["idade"])  # 28
print(dados["telefone"])  # "3333-1234"

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

print(dados)  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}


#Para acessar dados no dicionário em python = dicionario[chave] 
#Ex do dicionário "dados" = print(dados["nome"])  # "Guilherme"

#Chaves devem ser únicas: Cada chave só pode aparecer uma vez em um dicionário. 
#Tipos de chaves: As chaves podem ser de diversos tipos imutáveis, como strings, números e tuplas.
#Tipos de valores: Os valores podem ser de qualquer tipo, incluindo outros dicionários, listas e até mesmo funções.
#Acessar dados em um dicionário Python é simples e intuitivo. Basta usar a chave entre colchetes para obter o valor correspondente. Ao trabalhar com dicionários aninhados, você pode usar múltiplas chaves para acessar valores mais profundos.