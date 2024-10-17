conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b) #{1, 4} "NÃO ESTÃO EM INTERSECTION"
print(resultado)


#Este código calcula a diferença simétrica entre dois conjuntos em Python. A diferença simétrica de dois conjuntos é um novo conjunto que contém TODOS os elementos que estão EM UM dos conjuntos, MAS NÃO em AMBOS. Em outras palavras, são os elementos que SÃO ÚNICOS a cada conjunto.
