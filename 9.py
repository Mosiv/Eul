for i in range(1,500):
    for n in range(1,500):
        for m in range(1,500):
            if i+n+m == 1000:
                if (i**2)+(n**2)==(m**2):
                    print(i*n*m)
