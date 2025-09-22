# Leia números em uma lista até encontrar um negativo ( break ).

numeros = []

while True:
    n = int(input("Digite um número (negativo para parar): "))
    if n < 0:
        print("Número negativo detectado. Encerrando.")
        break
    numeros.append(n)

print("Números digitados:", numeros)
