import requests
import math

def gravitation(g,m1,m2,r):
    f=g*m1*m2 / math.pow(r,2)
    return f

m1 = 5.97600 * math.pow(10,24)
g = 6.6743 * math.pow(10,-11)

names = [["Mercury", "0.055", "77","202"],
    ["Venus", "0.815", "38", "261"],
    ["Mars", "0.107", "54","401"],
    ["Jupiter","318", "628","928"],
    ["Saturn", "95.2", "1200","1600"],
    ["Uranus", "14.6", "2700","2900"],
    ["Neptune","17.2","4300","4700"]]
for i in range(len(names)):
    m2 = 5.97*10**24 * float(names[i][1])
    r= (int(names[i][2])+int(names[i][3]))/2
    print(names[i][0],'-',gravitation(g,m1,m2,r))