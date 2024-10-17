conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b)  #True "CONJUNTO A E B NÃO TEM ND IGUAL"
print(resultado)

resultado = conjunto_a.isdisjoint(conjunto_c)  #False "CONJUNTO A E C, TEM COISAS IGUAIS, NO CASO AQUI (1)"
print(resultado)


#Este código verifica se dois conjuntos são disjuntos. Conjuntos disjuntos(destinto) são aqueles QUE NÃO POSSUEM ELEMENTOS EM COMUM. Em outras palavras, a interseção entre eles é um CONJUNTO VAZIO, POIS NÃO EXISTE IGUAL NA COMPARAÇÃO DOS 2 CONJUNTOS.
