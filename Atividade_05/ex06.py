# Escreva um programa que conte quantas vezes uma letra aparece em uma string.

msg = input("Digite uma string: ")
letra = input("Digite a letra a ser contada: ")
contador = 0

for c in msg:
    if c == letra:
        contador += 1
        
print(f"A letra '{letra}' aparece {contador} vezes na string.")