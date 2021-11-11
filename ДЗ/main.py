with open("input.bmp", "rb") as a:
    b = a.read()
    c = bytearray(b)
    for i in range(54, len(b)):
        c[i] = 255 - b[i]
    with open("res.bmp", "wb") as result:
        result.write(c)