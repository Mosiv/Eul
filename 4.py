#Четвертая задача
a = []
for i in range(100,1000):
    for n in range(100,1000):
        pal = str(i*n)
        if (pal == pal[::-1]) and (int(pal) > 900000):
            a.append(pal)
            print(a)
print(pal)
