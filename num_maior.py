num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

def verifica(num1, num2):
    if num1 > num2:
        print("O primeiro número é maior")
    if num1 < num2:
        print("O segundo número é maior")
    else:
        print("os dois são iguais")

verifica(num1, num2)