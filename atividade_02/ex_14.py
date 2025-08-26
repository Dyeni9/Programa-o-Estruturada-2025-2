#Solicite ao usuário que digite dois números. Verifique se um deles é zero e se a soma deles é maior que 10.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 == 0 or num2 == 0:
    print("Pelo menos um dos números é zero.")
else:
    print("Nenhum dos números é zero.")

soma = num1 + num2

if soma > 10:
    print("A soma dos números é maior que 10.")
else:
    print("A soma dos números NÃO é maior que 10.")
