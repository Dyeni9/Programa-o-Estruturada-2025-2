#  Crie uma função string_mais_longa que receba uma lista de strings e retorne a string mais longa. Teste com ["Python", "Java" , "C","JavaScript"] .

def string_mais_longa(lista_strings):
    """Retorna a string com o maior comprimento da lista."""
    mais_longa = ""
    for texto in lista_strings:
        if len(texto) > len(mais_longa):
            mais_longa = texto
    return mais_longa

lista_de_strings = ["Python", "Java", "C", "JavaScript"]
resultado = string_mais_longa(lista_de_strings)
print(f"A string mais longa é: {resultado}")