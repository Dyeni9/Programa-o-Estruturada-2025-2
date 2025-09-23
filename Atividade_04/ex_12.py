# Defina duas listas e crie uma nova lista com os elementos que estão presentes em ambas as listas, sem repetição.

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

interseccao = list(set(lista1) & set(lista2))
print(interseccao)