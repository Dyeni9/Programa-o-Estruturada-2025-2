# Crie um programa que leia dois números e imprima a soma, subtração, multiplicação e divisão deles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2 if num2 != 0 else "Divisão por zero não é permitida"

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)