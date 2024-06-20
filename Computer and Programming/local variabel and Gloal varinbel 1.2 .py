import math

#การเขียนแบบ local variabel
def compute_circle_area (radius):
    circle_area = math.pi*radius**2
    return circle_area

r = float(input('Enter area:'))
area = compute_circle_area(r)
print(f'พื่นที่วงกลมที่ได้คือ {area:.2f}')


#การเขียนแบบ Global variabel
def compute_circle_area (): #ไม่ใส่ตัวแปล
    circle_area = math.pi*r**2 #ใส่ตัวแปล r แทน radius
    return circle_area

r = float(input('Enter area:'))
area = compute_circle_area() #ไม่ใส่ตัวแปล
print(f'พื่นที่วงกลมที่ได้คือ {area:.2f}')
