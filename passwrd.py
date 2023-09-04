import string
from random import random, choice
import time
import os
time.sleep(1)
os.system(' figlet passwrd')
time.sleep(1)

print("""
####################################################
                   NOVO PROJETO

           CRIADOR: WILLIAN DE OLIVEIRA
####################################################""")
time.sleep(3)

print("GERANDO SENHA: ")
time.sleep(3)
valores = string.ascii_letters

valores += string.digits

valores += string.punctuation

tamanho = 10
senha = ""

print(string.digits)
print(string.punctuation)

for i in range(tamanho):
      senha += choice(valores)

print(senha)
