# Peça ao usuário para digitar uma string e remova todos os espaços em branco.

msg = input("Digite uma string com espaços: ")

msg_sem_espacos = msg.replace(" ", "")

print(f"A string sem espaços é: {msg_sem_espacos}")