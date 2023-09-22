import random
from random import randint
import time

n = 50000000
a=[]
b=[]
c=[]

for i in range(n):
    num = randint(1,999999)
    a.append(num)
    b.append(num)
    c.append(num)


def vstavka(y):
    for i in range(n):
        j = i-1
        k = y[i]
        while y[i] > k and j>=0:
            y[j+1] = y[j]
            j-=1
        y[j+1]= k 
    return y

start2 = time.time()
vstavka(b)
print('Сортировка вставками - ', time.time()-start2, 'секунд')

def quick(z):
    if len(z) <= 1:
       return z
    else:
       q = random.choice(z)
    l_z= [p for p in z if p < q]
    e_z = [q] * z.count(q)
    b_z = [p for p in z if p > q]
    return quick(l_z) + e_z + quick(b_z)

start3 = time.time()
quick(c)
print('Быстрая сортировка - ', time.time()-start3, 'секунд')

def puzirek(x):
    for i in range(n-1):
        for j in range(n-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]            
    return x

start1 = time.time()
puzirek(a)
print('Сортировка пузырьком - ', time.time()-start1, 'секунд')

#Не принтую отсортированные массивы, потому что сильно спамит консоль
