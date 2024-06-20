#มันคือ list of list หรือ nested list ลักษณะข้อมูลจะเป็นตาราง
#เอาไว้ใช้กับ csv file ส่วน csv file คือข้อมูลค่าที่ขั้น , คอมม่า

l = [1,2,3]
l2 = [4,5,6]
l3 = [l,l2]      #การสร้าง nested list ด้วยตัวเอง
l3
#[[1, 2, 3], [4, 5, 6]] #คำตอบ


#การหาความยาวของ nested list
len(l3)
#2 #คำตอบ

#การเรียกใช้ข้อมูลใน nested list
l3[1][2]
#6 #คำตอบ

l = [1,2,3]
l2 = [4,5,6]
l3[0][0]
#1 #คำตอบ


#Example
    
def read_tabel():
    list = open("D:\Computer and Programming\DATA\data_nested.txt").read().splitlines()
    tabel = [x.split(",") for x in list if x != ""]
    for row in tabel:
        row[0] = int(row[0]) #เปลี่ยนข้อมูลเป็นint 
        row.append(gard_point(row[2])) #ทำการส่งค่าไปที่ gard_point เมื่อได้ค่ามาเพิ่มไปที่ rowส่วนrowคือ tabelนั่นเอง
    return tabel
    
def gard_point(gard): #start gard_pointจากคำสั่ง row.append(gard_point(row[2]))
    if gard == "A":
        return 4
    elif gard == "B+" :
        return 3.5
    elif gard == "B" :
        return 3
    elif gard == "C+" :
        return 2.5
    elif gard == "C" :
        return 2
    elif gard == "D+" :
        return 1.5
    elif gard == "D" :
        return 1
    elif gard == "F" :
        return 0    

tabel = read_tabel()
print  ("-----------------------------------------")
print  ("  Subject    Credits    Grade    point"   )
print  ("-----------------------------------------")
for row in tabel:
    print(f'{row[0]:8} {row[1]:>10} {row[2]:>18} {row[3]:>10}') #:<10ชิดซ้าย10 , :>ชิดขวา10
    
print  ("-----------------------------------------")











