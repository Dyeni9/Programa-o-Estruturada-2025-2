#Leia entradas até o usuário digitar "sair"

while True:
    entrada = input("Digite algo (ou 'sair' para encerrar): ")
    if entrada.lower() == "sair":
        print("Programa encerrado.")
        break
    print(f"Você digitou: {entrada}")
