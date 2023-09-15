import math

def gravitation(g,m1,m2,r):
    f=g*m1*m2 / math.pow(r,2)
    return f

m1 = 5.97600 * math.pow(10,24)
g = 6.6743 * math.pow(10,-11)
m2 = int(input("Введите массу Луны в тоннах: "))
m2=m2*1000
r = int(input("Введите расстояние от Луны до Земли: "))

print(gravitation(g,m1,m2,r))
