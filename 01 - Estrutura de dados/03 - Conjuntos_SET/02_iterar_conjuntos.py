carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros): 
    print(f"{indice}: {carro}")



#"for carro in carros:" Inicia um laço for que irá percorrer cada elemento do conjunto carros. A cada iteração, o valor do elemento atual é atribuído à variável carro.

#A função enumerate() é uma ferramenta poderosa em Python que permite ITERAR sobre uma sequência (como uma lista, tupla ou conjunto) e, ao mesmo tempo, OBTER o ÍNDICE(COMEÇA NO 0) de cada elemento. Isso é particularmente útil quando você precisa tanto do valor do elemento quanto da sua posição na sequência.