a = []
i = 2
while len(a) < 10001:
    for j in a:
        if i % j == 0:
            break
    else:
        a.append(i)
    i += 1

print(a[-1])
