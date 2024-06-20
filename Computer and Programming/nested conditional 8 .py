#---- การเขียนหลายๆเงือนไข ----#
def diff_value(value,pow1):
    if value <= 0 :
        h = value**pow1
        if h == h:
            print(f'ค่ายกกำลังของ {value,pow1}คือ{h}')
    else:
        h =  value**pow1
        if h != h:
            print(f'ค่าที่ใส่มาไม่สามารถคำนวนได้')
        else:
            print(f'ค่ายกกำลังของ {value,pow1}คือ{h}')

              #main#
def Input():
    value = float(input('ใส่ค่าที่ต้องการเป็นเลขฐาน:'))
    pow1 = float(input('ใส่ค่าที่ต้องการยกกำลัง:'))
    return value,pow1

value,pow1 = Input()
diff_value(value,pow1)
