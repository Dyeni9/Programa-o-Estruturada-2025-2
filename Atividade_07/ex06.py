#  Escreva uma função conta_caracteres que receba uma string e retorne o número de caracteres. Teste com "Python".

def conta_caracteres(texto):
    """Recebe uma string e retorna seu comprimento."""
    return len(texto)

comprimento = conta_caracteres("Python")
print(f"A string 'Python' tem {comprimento} caracteres.")