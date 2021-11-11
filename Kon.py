x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
m = abs(x1 - x2)
n = abs(y1 - y2)
if n == 1 and m == 2 or m == 1 and n == 2:
    print("YES")
else:
    print("NO")
