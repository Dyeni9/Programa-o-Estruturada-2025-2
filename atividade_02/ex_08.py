#Leia um número e imprima "Positivo" se ele for maior que zero "Negativo" se for menor que zero e "Zero" se for igual a zero

num = float(input("Digite um número: "))

if num > 0:
    print("Positivo")
elif num < 0:
    print("Negativo")
else:
    print("Zero")