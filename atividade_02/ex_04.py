# Peça ao usuário para digitar dois números e verifique se a soma deles énmaior que 10.

num1 = float(input("Digite um número: "))

num2 = float(input("Digite outro número: "))

soma = num1 + num2

if soma > 10:
    print("A soma dos números é maior que 10.")
else:
    print("A soma dos números NÃO é maior que 10.")
