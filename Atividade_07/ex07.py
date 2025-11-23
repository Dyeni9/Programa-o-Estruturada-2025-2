#  Crie uma função eh_primo que receba um número e retorne True se ele é primo e False caso contrário. Teste com 11.

def eh_primo(numero):
    """Verifica se um número é primo."""
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False 
    return True

print(f"O número 11 é primo? {eh_primo(11)}")
print(f"O número 4 é primo? {eh_primo(4)}")