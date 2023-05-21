def romb(h,a):
    obwod = 4*a
    pole = a*h
    return obwod, pole

print(f"obwód i pole wynosi kolejno {romb(10,5)}")

def kolo(r):
    obwod = 2* pi *r
    pole = pi*r**2
    return obwod, pole

print(f"obwód i pole wynosi kolejno {kolo(10)}")
