import random

n = int(input("Insira um número inteiro maior que zero:"))

array = []

for i in range(n):
    num = random.uniform(0,100)
    array.append(num)

print("\nNúmeros gerados:")
for num in array:
    print(f"{num:.2f}")