#คือการอ่าน file txt
# function ที่ต้องใช้คือ open() แล้วก็เม็ดตอดคือ read()
# รวมกันเป็น open(filemane).read()
# ส่วนข้อมูลที่ได้มาจะเป็น string เสมอหรือ str

f = open("data.txt").read()
print(f)
#ผลลัพที่ได้อยู่ใน datd.txt


#หรืออีกฟังก์ชั่นหนึ่งคือ spltllines()การใช้คือเอามาเกาะกับ read()
#จะกลายเป็น open(filemane).read().splitlines() functinoนี้คือการจัดเรียงfileให้อยู่ในการจัดเก็บข้อมูลแบบlist

s = open("D:\Computer and Programming\DATA\data.txt").read().splitlines()
print(s)
#ผลลัพที่ได้ ['Hello word', 'Good morning']

#ข้อระวังคือการระบุที่อยู่ของfileถ้าfileไม่ข้อมูลที่จะใช้ไม่ได้อยู่ในโฟร์เดอร์เดียวกันห้ามใส่แค่ชื่อfileเด็ดขาด
#ถ้าอยู่โฟร์เดอร์เดียวกัน f = open("data.txt").read()
#แต่ถ้าไม่อยู่โฟร์เดอร์เดียวกัน f = open("D:\local variabel and Gloal varinbel I-III.PY\DATA\data.txt").read() #เอาที่อยู่ของข้อมูลมาใส่

#----- การแปลงข้อมูลใน file จาก str ไปเป็น flost
list = open("D:\Computer and Programming\DATA\codeing_data.txt").read().splitlines()
scores = [] #ทำการสร้าง listเปล่าๆมา
for i in list :
    scores.append(float(i)) #แปลงเป็นfloatแล้วaddข้อมูลไปไว้ในlistเปล่าที่สร้างไว้ด้วยappend()
print(scores)