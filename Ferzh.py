x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
m = abs(x1 - x2)
n = abs(y1 - y2)
if x1 == x2 or y1 == y2 or m == n:
    print("YES")
else:
    print("NO")
