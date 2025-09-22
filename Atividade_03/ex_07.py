# Crie uma tabuada de 1 a 10 com laços aninhados.

while True:
    entrada = input("Digite algo (ou 'sair' para encerrar): ")
    if entrada.lower() == "sair":
        print("Programa encerrado.")
        break
    print(f"Você digitou: {entrada}")
