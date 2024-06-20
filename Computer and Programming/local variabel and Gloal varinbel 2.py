def read_trapezoid () :
    print('กรุณาใส่ความกว้างความสูงของสี่เหลี่ยมคางหมูเพื่อหาค่า:')
    a = float(input('ความกว้าง:'))
    b = float(input('ความยาว:'))
    h = float(input('ความยาว:'))
    return a,b,h

def trapezoid_area (a,b,h):
    return (a+b)/2*h

    
a,b,h = read_trapezoid ()
area = trapezoid_area (a,b,h)

print(f'พื้นที่เท่ากับ:{area}')

