# №1
last = 0
n = 0
s = 0
for i in open('k7b-2.txt').readline():
    if i == 'D':
        if last == 4:
            s += 4
        last = 1
    elif i == 'B' and last == 1:
        last = 2
    elif i == 'A' and last == 2:
        last = 3
    elif i == 'C' and last == 3:
        last = 4
    else:
        n = max(n, s + last)
        last = 0
        s = 0
print(max(n, s + last))

# №2
s = 0
string = open('k7c-6.txt').readline()
for i in range(len(string) - 3):
    s += int(len(set(string[i:i + 3])) == 3)
print(s)

# №3
n = 1
k = 0
string = open('k7-m3.txt').readline()
ind = len(string) + 1
for i in range(len(string)):
    if string[i] == 'C':
        k += 1
        ind = min(ind, i)
    elif 0 < k <= 4:
        print(f"{n} {k} {('c' * k).capitalize()}")
        n += 1
        k = 0
        ind = len(string) + 1
    else:
        k = 0
        ind = len(string) + 1
if 0 < k <= 4:
        print(f"{n} {k} {('c' * k).capitalize()}")
