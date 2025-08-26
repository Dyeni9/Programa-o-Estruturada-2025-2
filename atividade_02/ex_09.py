#Solicite ao usuário que digite uma letra. Se a letra for uma vogal, imprima "Vogal", caso contrário, imprima "Consoante".

# Solicita que o usuário digite uma letra
letra = input("Digite uma letra: ").lower()  # .lower() transforma em minúscula

# Verifica se é vogal
if letra in "aeiou":
    print("Vogal")
else:
    print("Consoante")