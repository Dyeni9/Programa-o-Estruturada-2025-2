# Escreva um programa que tente modificar um elemento de uma tupla e capture a exceção

tupla = (1, 2, 3)

try:
    tupla[0] = 10
except TypeError as e:
    print("Erro:", e)
