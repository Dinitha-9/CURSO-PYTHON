
# tupla pois esta com parenteses nao pode ser modificada
flores = ('tulipa','rosa','margarida',)

#lista pois e couchetes
carros_lista = ['jaguar', 'toiota', 'uno','fordk']

#adiciona a lista
carros_lista.append ('fusca')

#Dicionario pois esta com chaves e tem chave valor 
alunos ={'nome': 'lucas',  'Idade': 28, 'nota': 10 }

#imprime valor especifico
print(alunos['nome'])

#altera valor
alunos['nome']='jose'

#altera dados e acrecenta
alunos.update({'nome':'jose', 'nota': 8})
alunos.update({'email': 'jose.fee@gmail.com'})

#deleta um valor
del alunos['Idade']

# retornos especificos
for x in alunos.values():
    print(x)
    
#print(alunos)