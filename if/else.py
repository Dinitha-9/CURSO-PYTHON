from ast import If


idade = 10
idades2 = 15
if( idade  > idades2):
    print(' pode votar')
    
else:
        print(" não apto a votar")
        
cores =  {"amarelo", "azul","rosa"}
if "amarelo" in cores:
    print( 'possui')
else:
    print("não possui")
    
cor_cliente= input("Digite uma cor: ")
#.lower=indifere se o usuario digitar maiusculo ou minusculo
if cor_cliente.lower in cores:
        print("Esta")
else:
    print("Não esta")
    
    
    
    
    