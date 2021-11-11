x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
m = abs(x1 - x2)
n = abs(y1 - y2)
if m <= 1 and n <= 1:
    print('YES')
else:
    print('NO')
