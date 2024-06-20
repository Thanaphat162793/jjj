#ฟังก์ชั่นกับเมทตอดต่างกันอย่างไร
#methods นี้มันคือฟังก์ชั่นที่ต้องเกาะอยู่กับออฟเจ็กไม่สามารถอยู่ลอยๆได้
#โดยที่ functionสามารถอยู่ลอยๆได้
#อย่างเช่นfunction จะมี len(),sum()
#เเต่ถ้าเป็น methods คำสั่งsplit()จะต้องเกาะอยู่กับstr  ###คำสั่งsplit()มีหน้าที่แบ่ง str

list = open("D:\Computer and Programming\DATA\data.txt").read().splitlines()
for i in range(len(list)) :
    print(f'line {i+1} list {list[i]}')
    
#สิ่งที่ห้ามลืมคือเวลาเปิด file ออกมาอย่าลืมปิดเหตุผลว่าทำไมต้องปิดมันคือการเครียร์ค่าในเมมโมลี่
#คำสั่ง
    #with open("D:\Computer and Programming\DATA\data.txt").read().splitlines() as f: #ถ้าเป็น with loop ใช้ as f:ในการปิด
    
#    list = open("D:\Computer and Programming\DATA\data.txt").read().splitlines() #ถ้าเป็น for loop ใช้ close() ในการปิด
#    for i in range(len(list)) :
#		 print(f'line {i+1} list {list[i]}')
#    list.close() #ถ้าเป็น for loop ใช้ close() ในการปิด

#ถ้าเขียนโปรแกรมเล็กๆไม่จำเป็นต้องปิดก็ได้

