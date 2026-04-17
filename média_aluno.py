n1 = float(input("Digite uma nota de 0 a 10:"))
n2 = float(input("Digite uma nota de 0 a 10:"))
n3 = float(input("Digite uma nota de 0 a 10:"))
n4 = float(input("Digite uma nota de 0 a 10:"))


def soma_nota(n1, n2, n3, n4):
    resultado = n1 + n2 + n3 + n4
    return resultado

total = soma_nota(n1, n2, n3, n4)

#elif 5 <= media_final < 7: eu poderia usar assim mas prefiro não
def media(total):
    media_final = total / 4
    if media_final >= 7:
        print("Aprovado")
    elif media_final >= 5 and media_final < 7:
        print("Recuperação")
    else:
        print("Reprovado")

media(total)

    

    
