'''https://stepik.org/lesson/265083/step/14?unit=246031

Задача
	Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли ладья попасть с первой клетки на вторую одним ходом. 
	Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. 
	Программа должна вывести «YES», если из первой клетки ходом ладьи можно попасть во вторую, или «NO» в противном случае.
	Примечание. Шахматная ладья ходит по горизонтали или вертикали.
'''
	
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

if (a2 != a1 and b2 == b1) or (a2 == a1 and b2 != b1):
    print('YES')
else:
    print('NO')
    
    
'''https://stepik.org/lesson/265083/step/15?unit=246031

Задача
    Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, может ли король попасть с первой клетки на вторую одним ходом. 
    Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом короля можно попасть во вторую, или «NO» в противном случае.
    Примечание. Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку.
'''
	
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x2 == x1 or x2 == x1 - 1 or x2 == x1 + 1) and (y2 == y1 or y2 == y1 - 1 or y2 == y1 + 1):
    print('YES')
else:
    print('NO')
    
Или короче:

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (-1 <= x2 - x1 <= 1) and (-1 <= y2 - y1 <= 1):
    print('YES')
else:
    print('NO')