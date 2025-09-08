fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

r = fruits.count('apple')
print(r)

r = fruits.count('tangerina')
print(r)

r = fruits.index('banana')
print(r)

r = fruits.index('banana', 4)
print(r)


fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

r = fruits.pop()
print(fruits)

from collections import deque

queue = deque(['Eric', 'John', 'Michael'])
queue.append('Terry')
queue.append('Graham')
r = queue.popleft()
print(r)
r = queue.popleft()
print(r)
print(queue)

squares = list(map(lambda x: x**2, range(10)))
squares2 = [x**2 for x in range(10)]

print(squares)
print(squares2)

combs = [(x,y) for x in [1,2,4] for y in [2,4,3] ]


[print(x, end=' ') for x in range(1,10) if x % 2 == 0]


print()

v = [[1,2,3], [4,5,6], [7,8,9]]
[print(n) for e in v for n in e]


def print_chess_board(m=8, n=8):
    [print("".join("⬛" if (i + j) % 2 == 0 else "⬜" for j in range(n))) for i in range(m)]

print_chess_board()

v = [[1,2,3], [4,5,6], [7,8,9]]
[print(n) for e in v for n in e]
