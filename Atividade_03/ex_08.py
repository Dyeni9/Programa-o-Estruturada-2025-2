#Crie uma lista com 5 números e imprima o dobro de cada um.

while True:
    entrada = input("Digite algo (ou 'sair' para encerrar): ")
    if entrada.lower() == "sair":
        print("Programa encerrado.")
        break
    print(f"Você digitou: {entrada}")
