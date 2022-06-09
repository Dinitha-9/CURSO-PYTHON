#for numero in range (6):
    #print(numero)

# terceira casa e o para metro de 2 em 2
'''from distutils.log import info
from stat import FILE_ATTRIBUTE_SPARSE_FILE


for numero in range (1,20,2):
     print(numero)
     
     
flagcompra = True
info = ('compra efetuada')

for tentativas in range (3):
    if flagcompra:
        print (info)
        break
    else:
        print ("Erro na compra")
        
        
lista = [1,2,3,4,5]
for item in lista:
   input(item)
    
lista = [1,2,3,4,5]
for item in lista:
   print(item)'''
   
   
fruta1 = [ 'maçã', 'mamão', 'abacaxi','melão']
fruta2 = []
for fruta in fruta1:
    if 'm' in fruta:
        fruta2.append(fruta)
        print (fruta2)
       
#forma reduzida         
frutas3 = [fruta for fruta in fruta1 if "m" in fruta]
print(frutas3)

# 2 formas de aprececer o index
index = 0 
for fruta in fruta1:
    print(index,fruta)
    index +=1
for cont, fruta in enumerate(fruta1):
    print(cont, fruta)