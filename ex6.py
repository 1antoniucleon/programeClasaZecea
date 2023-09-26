import math
def s(n):
    return math.sqrt(n)

rez = s(13+s(30*s(2+s(9+4*s(2)))))
print(rez)