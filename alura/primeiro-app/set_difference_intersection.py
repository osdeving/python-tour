text1 = 'O sol brilha forte no céu azul'
text2 = 'O céu azul anuncia um dia de sol intenso'

s1 = set(text1.lower().split())
s2 = set(text2.lower().split())
s3 = s1.intersection(s2)

#s4 = [w for w in text1.lower().split() if w in text2.lower().split()]


print(f'Palavras em comum: {s3}')
print(f'Palavras diferentes no texto 1: {s1.difference(s2)}')
print(f'Palavras diferentes no texto 2: {s2.difference(s1)}')
#print(f'Palavras em comum: {s4}')

