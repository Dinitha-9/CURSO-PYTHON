from urllib import response


valor = 100

while valor > 20:
    print(valor)
    valor -=5
 
    
lista =[1,2,3,4,5,6,7,8]
tamanho = len(lista)
x=0

while(x < tamanho):
    print (lista[x])
    x +=1
    
a =10
i = 5
while i<= a: print(a); a  -=1
    
a =10
i = 5
while i<= a:
    a -=1 
    if a== 7:
        print("chegou no 7")
        continue
    print(a)

a =10
i = 5
while i<= a:
    a -=1 
    if a== 7:
        print("chegou no 7")
        break
    print(a)
    
    i  = 10
    while i <=15:
        print(i)
        i += 1 
    else:
        print("chegamos no final!")
        
        pontos = 0
        questão = 1
        while questão <=3:
            resposta = input(f"Resposta da questão: {questão}")
            if questão == 1  and (resposta == "b" or resposta == "B"):
                pontos = pontos + 1
           
            if questão == 2  and (resposta == "a" or resposta == "A"):
                 
                 pontos = pontos + 1
            
            if questão == 3  and (resposta == "d" or resposta == "D"):
            
                 pontos = pontos + 1
            questão +=1
            print(f"aluno tem total de: {pontos} pontos" )