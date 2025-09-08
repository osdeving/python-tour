guests = set()

while True:
    name = input("Digite o nome do convidado ou 'sair' para encerrar: ")

    if name.lower() == 'sair':
        break

    guests.add(name)

print(f'Convidados confirmados: {','.join(guests)}')
