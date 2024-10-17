conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b)  # True (A ESTA DENTRO DO CONJUNTO B)
print(resultado)

resultado = conjunto_b.issubset(conjunto_a)  # False (B NÃO ESTA DENTRO DO CONJUNTO A)
print(resultado)


#Este código verifica se um conjunto é SUBconjunto de outro. Um subconjunto é um conjunto onde todos os elementos também estão presentes em outro conjunto maior.
