# Escreva uma função ordena_lista que receba uma lista de números e retorne a lista ordenada. Teste com [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5] .

def ordena_lista(lista):
    """Recebe uma lista e retorna uma nova lista ordenada."""
    return sorted(lista)

lista_original = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
lista_ordenada = ordena_lista(lista_original)

print(f"Lista original: {lista_original}")
print(f"Lista ordenada: {lista_ordenada}")