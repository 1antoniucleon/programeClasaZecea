import math
def s(n):
    return math.sqrt(n)

rez = s(26+6*s(13-4*s(8+2*s(6-2*s(5))))) + s(26-6*s(13+4*s(8-2*s(6+2*s(5)))))
print(rez)