def romb(h,a):
    obwod = 4*a
    pole = a*h
    return obwod, pole

print(f"obwód i pole rombu wynosi kolejno {romb(10,5)}")

from math import pi
def kolo(r):
    obwod = 2* pi *r
    pole = pi*r**2
    return obwod, pole

print(f"obwód i pole kola wynosi kolejno {kolo(10)}")
