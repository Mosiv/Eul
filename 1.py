#Pyhton 3.7
#Задача решена списками
a = [i for i in range(3,1000,3)]
b = [i for i in range(5,1000,5)]
del b[2:500:3] #удаляем повторяющиеся цифры
print(sum(a+b))
