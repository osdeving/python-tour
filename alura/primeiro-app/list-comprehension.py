# Sintaxe básica
#
# [expressão for item in iterável if condição]
# 
# expressão: 
#
# como cada item da lista vai ser.
# pode ser o item em si, ou uma transformação dele
# ex: item.upper() ou item * 2
#
# for item in iterável:
#
#  define o laço de repetição
# item é a variável temporária que assume cada valor
# 
# if condição: 
#
# é opcional, atua como um filtro. a expressão
# só será incluída na nova lista se esta condição for true 


# Múltiplos de 3
# range(start, stop, step)
# start = 3 (inclusive), stop = 31 (exclusivo), step = 3
# n é a  expressão, nesse caso
multiplos_de_3 = [n for n in range(3, 31, 3)]
print(multiplos_de_3)


print()

colors = ['BLACK', 'WHITE']
sizes = ['S', 'M', 'L']

tshirts = [ (color, size) for color in colors for size in sizes]

print(f'Cores: {colors}')
print(f'Tamanhos: {sizes}')
print()
print(f'Combinações de camisetas (cor, tamanho): {tshirts}')



quadrados_pares = [n ** 2 for n in range(1, 11) if n % 2 == 0]
print(quadrados_pares)
