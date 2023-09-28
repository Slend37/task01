s = str(input())

#1
x = s.split()
print(len(x))

#2
s2 = str(input('Write a word/letter: '))
s=s.replace(s2,'😎')
print(s)

#3
s=str(input())
for x in s:
    k=s.count(x)
    print(x,'-',k)

