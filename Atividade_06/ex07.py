# Escreva um programa que some os valores de todas as chaves de um dicionário.

frutas_estoque = {"Maçã": 10, "Banana": 15, "Laranja": 8} 

soma_total = 0

for quantidade in frutas_estoque.values():
    soma_total += quantidade

print(f"A soma total das quantidades é: {soma_total}")