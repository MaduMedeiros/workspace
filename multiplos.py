nA, nB = input("Digite dois números:").split()
nA = int(nA)
nB = int(nB)

def verifica(nA, nB):
    if nA % nB == 0:
        print("São múltiplos, eba!")
    else:
        print("Não são múltiplos!!")

verifica(nA, nB)