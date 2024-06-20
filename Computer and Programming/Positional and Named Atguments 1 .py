#positional Atguments
def totle_area():
    a = float(input())
    b = float(input())
    h = float(input())
    return a,b,h,


def area1(a,b,h):
    return a+b+h

a,b,h  = totle_area()
area = area1(a,b,h)
print(f'{a}+{b}+{h}={area:.2f}')



#Nemed Atguments
def totle_area():
    a = float(input())
    b = float(input())
    h = float(input())
    return a,b,h,


def area1(h,a,b):
    return (a+b)*h
    

a,b,h  = totle_area()
area = area1(a = a,b = b,h = h)
print(f'{a}+{b}+{h}={area:.2f}')
