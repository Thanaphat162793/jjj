def Average(): #ฟังก์ชันหาค่าเฉลี่ย
    values = 0 #กำหนดตัวแปร values ให้เป็น 0
    more_data = 'yes' #กำหนดตัวแปร more_data ให้เป็น yes
    sum = 0
    while more_data[0] == 'y': # while loop คือ ทำโค้ดบล็อกเมื่อเข้าเงือนไขในที่นี้ ถ้า more_data = yes จะทำการเอา numbers+values นั้นคือ numbers+0 เมื่อบวกเส็จจะทำการ
        numbers = float(input('Enter values: '))                 #ถามว่า more datd /// yes or no /// ถ้าเป็น yes จะทำแบบเดิมอีกครั้ง แต่ถ้า no จะรีเทินค่าแล้าปริ้น
        values = values + numbers
        sum = sum+1  #ทำการบวก 1 ไปเรื่อยๆ ถ้าเงือนไขเป็นจริง
        more_data = input('more datd /// yes or no /// : ')
    return values/sum,sum  #นำค่าทั้งหมดมาหารด้วย sum เพื่อหาค่าเฉลี่ย
agv,sum = Average()
print(f'average is {agv} for loop {sum} ')