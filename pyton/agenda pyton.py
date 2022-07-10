import imp
from mailbox import NotEmptyError
from msilib.schema import Error
import sqlite3
#import os
#import sqlite3
#from sqlite3 import Error
# def conexaoBanco():
     #caminho=""
     #con=NotEmptyError
     #try
      #  con= sqlite3
       # except Error as ex:
        #    print(ex)
         #   return  con
#vcon= ConexaoBanco()         

agenda = []



def inserir_nome():
    return(input("Nome da pessoa que deseja adicionar: "))


def inserir_telefone():
    return(input("Insira seu numero de telefone: "))


def inserir_endereco():
    return(input("Insira o endereço: "))


def adicionar():
    global agenda
    nome = inserir_nome()
    telefone = inserir_telefone()
    endereco = inserir_endereco()
    agenda.append([nome, telefone, endereco])


def adicionar1():
    nome_arquivo = inserir_nome()
    arquivo = open(nome_arquivo, "w", encoding="utf-8")
    for e in agenda:
        arquivo.write("Nome: %s Telefone: %s Endereço: %s\n" % (e[0], e[1], e[2]))
    arquivo.close()

print("\n-------------------------------")
print("Bem-vindo a sua agenda!")
print("-------------------------------")

print("Escolha o tipo de operação")

operacoes = input('''
Para adicionar digite " adicionar "!
''')

if operacoes == 'adicionar':
    print("\nOpção ADICIONAR selecionada")
    adicionar1()
    inserir_telefone()
    inserir_endereco()

else:
    print('Você nao digitou um valor aceitavel!')
    print("Fim de operação!")

print("Fim de operação!")
python