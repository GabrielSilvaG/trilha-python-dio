conjunto_a = {1, 2, 3, 5}
conjunto_b = {2, 3, 4, 7}

resultado = conjunto_a.difference(conjunto_b) #{1, 5} "A" EM "B"
print(resultado)

resultado = conjunto_b.difference(conjunto_a) #{4, 7} "B" EM "A"
print(resultado)


#Este código demonstra a operação de DIFERENÇA entre dois conjuntos em Python. A diferença entre dois conjuntos é um novo conjunto que CONTÉM os elementos que estão presentes em UM conjunto, MAS NÃO no OUTRO.
