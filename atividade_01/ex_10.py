#Escreva um programa que calcule o resto da divisão de um número por outro.
num1 = int(input("Digite o dividendo: "))
num2 = int(input("Digite o divisor: "))

if num2 != 0:
    resto = num1 % num2
    print(f"O resto da divisão de {num1} por {num2} é: {resto}")
else:
    print("Erro: divisão por zero não é permitida.")