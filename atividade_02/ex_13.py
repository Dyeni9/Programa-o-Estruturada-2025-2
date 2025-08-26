#Leia três números e imprima se todos são diferentes.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 != num2 and num1 != num3 and num2 != num3:
    print("Todos os números são diferentes.")
else:
    print("Alguns números são iguais.")
