for i in range(1, 100):
    a = [i**2 for i in range(1, 101)]
    b = [i for i in range(1, 101)]
print((sum(b)**2)-sum(a))
