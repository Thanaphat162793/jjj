import math

def line_triangle (x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def area_triangle (x1,y1,x2,y2,x3,y3):
    a = line_triangle (x1,y1,x2,y2)
    b = line_triangle (x2,y2,x3,y3)
    c = line_triangle (x3,y3,x1,y1)
    s = (a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

def Input ():
    x = float(input('Enter:'))
    y = float(input('Enter:'))
    return x,y

def read_triangle ():
    x1,y1 = Input ()
    x2,y2 = Input ()
    x3,y3 = Input ()
    return x1,y1,x2,y2,x3,y3

x1,y1,x2,y2,x3,y3 = read_triangle ()
area = area_triangle (x1,y1,x2,y2,x3,y3)
print(f'{area:.2f}')