#Четвертая задача
a = []
for i in range(100,1000):
    for n in range(100,1000):
        pal = str(i*n)
        if (pal == pal[::-1]):
            a.append(int(pal))
print(a)
print(max(a))
