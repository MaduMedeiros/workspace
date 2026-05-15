nomes = ["Ana", "Bruno", "Carlos", "Diana"]

print("Possíveis duplas:\n")

for i in range(len(nomes)):
    for j in range(i + 1, len(nomes)):
        print(f"{nomes[i]} e {nomes[j]}")