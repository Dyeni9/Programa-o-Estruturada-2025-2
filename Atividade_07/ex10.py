# Escreva uma função calcula_fatorial que receba um número e retorne o seu fatorial. Teste com 5

def calcula_fatorial(n):
    """Calcula o fatorial de um número inteiro não negativo."""
    if n < 0:
        return "Fatorial não é definido para números negativos"
    if n == 0 or n == 1:
        return 1
    
    fatorial = 1
    for i in range(2, n + 1):
        fatorial *= i
    
    return fatorial

print(f"O fatorial de 5 é: {calcula_fatorial(5)}")