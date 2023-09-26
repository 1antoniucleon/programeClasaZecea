import math
def s(n):
    return math.sqrt(n)

rez = 2*s(3+s(5-s(13+4*s(3))))
print(rez)