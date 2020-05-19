a = 2520
while True:
    for i in range(1, 20):
        if (a % i) > 0:
            break
    else:
        print(a)
        break
    a = a + 2520
