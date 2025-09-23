#  Crie um programa que receba uma lista de números do usuário e retorne a média dos números pares na lista.

numeros = [1, 2, 3, 4, 5, 6]
pares = [n for n in numeros if n % 2 == 0]

if pares:
    media = sum(pares) / len(pares)
    print("Média dos pares:", media)
else:
    print("Não há números pares.")
