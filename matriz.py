matriz = []
numero = 1

for i in range(4):
    linha = []
    for j in range(5):
        linha.append(numero)
        numero += 1
    matriz.append(linha)

for linha in matriz:
    print(linha)