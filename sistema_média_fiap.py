cp1 = float(input("Insira em um número de 0 a 10 a nota do primeiro Checkpoint:"))
cp2 = float(input("Insira em um número de 0 a 10 a nota do segundo Checkpoint:")) 
cp3 = float(input("Insira em um número de 0 a 10 a nota do terceiro Checkpoint:"))
sprint1 = float(input("Insira em um número de 0 a 10 a nota da primeira Sprint:"))
sprint2 = float(input("Insira em um número de 0 a 10 a nota da segunda Sprint:"))
gs = float(input("Insira em um número de 0 á 10 a nota da Global Solution:"))

all_cp = [cp1, cp2, cp3]

#calculando a média das cps e sprints
def  calc_media1(all_cp, sprint1, sprint2):
   menor_cp = min(all_cp)
   result1 = (sum(all_cp) - menor_cp + sprint1 + sprint2) / 4
   return(result1)

#pra agilizar
media_cps = calc_media1(all_cp, sprint1, sprint2) 

#calculando média do semestre
def calc_media2(media_cps, gs):
   result2 = (media_cps * 0.4 + gs * 0.6)
   return(result2)
    
media_semestre = calc_media2(media_cps, gs)
print(f"Nota deste semestre sem a aplicação do peso: {media_semestre:.1f}")

#calculando o peso do semestre
def media_peso(media_semestre):
   result3 = (media_semestre * 0.4)
   return(result3)

media = media_peso(media_semestre)
print(f"Nota final deste semestre com a aplicação do peso: {media:.1f}")