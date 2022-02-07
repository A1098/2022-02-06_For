from asyncore import loop
from re import A


for x in range (0, 151, 1) :
    if x <= 150:
        print(x)
for y in range (5, 1005, 5):
    if y <=1000:
        print(y)
for z in range (1, 101, 1):
    if z % 5 == 0:
        print("Coding")
    elif z % 10 == 0:
        print("Coding Dojo")
    else:
        print(z)

b = 0
for a in range (0, 500001,1):
    if a % 2 == 0:
        continue
    else:
        b += A
print (b)

for c in range (2018, 0, -4):
    print(c)

lowNum = 2
highNum = 10
mult=3
for d in range (lowNum, highNum, 1):
    if d % 3 == 0:
        print(d)
