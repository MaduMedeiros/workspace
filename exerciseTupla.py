lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 
         'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
input_num = int(input("Digite um número entre 0 e 20: "))
if 0 <= input_num <= 20:
    print(f"O número {input_num} por extenso é {lista[input_num]}")
else:
    print("Número fora do intervalo permitido.")


