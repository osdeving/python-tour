# apaga se existir
with open('notes.txt', 'w', encoding='utf-8') as file:
    file.write('These are my notes.\n')
    file.write('I am learning Python file handling.\n')
    file.write('This is the third line of my notes.\n')

# adiciona ao que já existe
with open('notes.txt', 'a', encoding='utf-8') as file:
    file.write('This is an additional line.\n')

# lê o conteúdo do arquivo
with open('notes.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

# lê o arquivo linha por linha
with open('notes.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.rstrip())
