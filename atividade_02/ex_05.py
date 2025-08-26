#Leia três números e imprima se o primeiro é menor que o segundo e maior que o terceiro.

num1 = float(input("Digite o primeiro número: "))

num2 = float(input("Digite o segundo número: "))

num3 = float(input("Digite o terceiro número: "))

if num1 < num2 and num1 > num3:
    print("O primeiro número é menor que o segundo E maior que o terceiro.")
else:
    print("A condição não foi satisfeita.")