a = float(input())
b = float(input())
c = input()
d = 0

if c == "/" or c == "+" or c == "*" or c == "-" and (c != "/" and b != "0"):
    if c == "+":
        d = a + b
    if c == "-":
        d = a - b
    if c == "*":
        d = a * b
    if c == "/":
        d = a / b
else:
    d = 888888
if d % 1 == 0:
    print(int(d))
else:
    print(d)