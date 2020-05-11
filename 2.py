#Фибоначи
a, b = 0, 1
fibo = []

while b < 4000000:
    a_sum = a + b
    a = b
    b = a_sum
    if a_sum % 2 == 0:
        fibo.append(a_sum)
print(sum(fibo))
