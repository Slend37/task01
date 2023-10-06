import random
from random import randint
s=''
for i in range(1000):
    s=s+str(chr(randint(0,9)))
print(s)