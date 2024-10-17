conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # False (A NAO ESTA MAIOR QUE B)
print(resultado)

resultado = conjunto_b.issuperset(conjunto_a)  # True (B ESTA MAIOR QUE A)
print(resultado)


#Este código verifica se um conjunto é um SUPERconjunto de outro. Um superconjunto é um conjunto que contém todos os elementos de outro conjunto, ou seja, o conjunto menor é um subconjunto do conjunto maior.
