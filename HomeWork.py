#n = int(input())
#a = [] * n
# d = int(input())
# m = int(input())
# yc = int(input())
# c = yc // 100
# y = (yc - c) % 100
# otv = (d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)) % 7
# print(otv)
a = float(input("Первое число"))
b = input("Знак")
c = float(input("Второе число"))
def plusmine(a, c):
    d = a + c
    return d
def minusmine(a, c):
    d = a - c
    return d
def delitmine(a, c):
    d = a / c
    return d
def celDelm(a, c):
    d = a // c
    return d
def proizvm(a, c):
    d = a * c
    return d
if b == "+":
    d = plusmine(a, c)
elif b == "-":
    d = minusmine(a, c)
elif b == "*":
    d = proizvm(a, c)
elif b == "/":
    d = delitmine(a, c)
elif b == "//":
    d = celDelm(a, c)
else:
    print("Uncorrect")
if d % 1 == 0:
    print(int(d))
else:
    print(d)