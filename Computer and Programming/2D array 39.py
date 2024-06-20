#คือการเขียนแบบอ่านfileตารางหรือ CSV file
#การใช้ numpyอ่าน csv file
#ใช้คำสั่ง loadtxt("FILENAME",delimiter=",") แทนที่จะใช้ open("FILENAME").read().splitlines()
import numpy as np
table = np.loadtxt("D:\Computer and Programming\DATA\T_numpy.txt",delimiter=",")
print(table)

#คุณะสมบัติของ array
#ตัวแปล.ndim บอกมิติของ array
#ตัวแปล.shape บอกขนาดหรือบรรทัดกับตัวข้อมูลว่ามีกี่ช่อง
#ตัวแปล.size บอกจำนวนสมาชิกรวมกันทั้งหมด
table = np.loadtxt("D:\Computer and Programming\DATA\T_numpy.txt",delimiter=",")
a = table.ndim
b = table.shape
c = table.size
print(a) # 2 คำตอบ
print(b) # (3, 4) คำตอบ
print(c) # 12 คำตอบ



print("การเปลี่ยนจาก 1 มิติเป็น 2มิติ") #การเปลี่ยนจาก 1 มิติเป็น 2มิติ
T_1D1 = np.loadtxt("T_T.txt",delimiter=",")
print(T_1D1.ndim)

print("หลังเปลี่ยน")  #การเปลี่ยน
T_1D2 = np.loadtxt("T_T.txt",delimiter=",",ndmin = 2)
print(T_1D2.ndim)


#----------------- Example ------------#print คะแนนคนที่่ผู้ใช้พิมไป
import numpy as np 
FILENAME = np.loadtxt("D:\Computer and Programming\DATA\T_numpy.txt",delimiter=",",ndmin = 2)
print(f'Reading data from D:\Computer and Programming\DATA\T_numpy.txt')
nrow,crow = FILENAME.shape
print(f'Found scores fo {nrow} student(s) in {crow} subject(s)')
student = int(input('Enter student on.: '))
subject = int(input('Enter subject on.: '))
print(f'student #{student} scores on subject #{subject} is {FILENAME[student-1][subject-1]}')

print()
#----------------- Example2 ------------#หาคนที่คะแนนไม่ถึง 50
import numpy as np
FILENAME = np.loadtxt("D:\Computer and Programming\DATA\T_numpy.txt",delimiter=",",ndmin = 2)
print(f'Reading data from D:\Computer and Programming\DATA\T_numpy.txt')
nrow,crow = FILENAME.shape
print(f'Found scores fo {nrow} student(s) in {crow} subject(s)')
for s in range(nrow):
    for c in range(crow):
        table = FILENAME[s][c]
        if table < 50:
            print(f'student #{s+1} fails subject #{c+1} with score {table}')
    









