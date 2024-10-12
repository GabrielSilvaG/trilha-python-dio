matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (5, 6, "c"),
)

print(matriz[0][1])  # imprime: "a"
print(matriz[0][1:])  # imprime: "a", 2
print(matriz[0])  # imprime: (1, "a", 2)
print(matriz[1][-2:])  # imprime: 3, 4
print(matriz[-1])  # imprime: (5, 6, "c")
print(matriz[:])  # imprime: (1, "a", 2), ('b', 3, 4), (5, 6, 'c') "PASSA A LISTA COMPLETA"
print(matriz[1:])  # imprime: ('b', 3, 4), (5, 6, 'c') "TUDO DEPOIS DO ÍNDICE PASSADO"
print(matriz[:2])  # imprime: (1, 'a', 2), ('b', 3, 4) "TUDO MENOS O ÍNDICE PASSADO"
print(matriz[2][:2])  #imprime: 5, 6