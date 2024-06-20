#----- codeing แบบหาค่ามากที่สุด -----#
def max_of_three(a,b,c):
    max = a
    if max < b:
        max = b
        if max < c:
            max = c
            return max
def Input():
    a = float(input('Enter the vlue:'))
    b = float(input('Enter the vlue:'))
    c = float(input('Enter the vlue:'))
    return a,b,c

a,b,c  = Input()
value = max_of_three(a,b,c)                                  #----- ไม่สามารถรันโค้ดได้ต้องลบตัวไหนตัวหนึ่งออกก่อน ----#
print(value)


#----- Ezey the codeing ------#

def Input():
    a = float(input('Enter the vlue:'))
    b = float(input('Enter the vlue:'))
    c = float(input('Enter the vlue:'))
    return a,b,c

a,b,c  = Input()
h = max(a,b,c)
value = h
print(f'max fo three {value}')
