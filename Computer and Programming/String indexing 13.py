#-------- String indexing คือการปริ้นค่า string ออกมาทีละตัวตามลำดับ 0,1,2,3 อย่างเช่น

valabels = "Thanaphat"
valabels [3]
# ค่าที่ได้คือ a เพราะ a เป็นตัวที่ 3 นับจาก 0

# ตัวอย่าง 
valabels = "Thanaphat"
valabels [-3]
# ค่าที่ได้คือ h เพราะ h เป็นตัวที่ 3 นับจาก -1

# สรุป ถ้าคำสั่งเป็นเลขจำนวนเต็มเช่น 0,1,2,3 จะนับจากตัวอักษรด้านหน้าสุดไปหลัง แต่ถ้าเป็นเลขติดลบ เช่น -1,-2,-3 จะนับจากด้านหลังสุดไปหน้า

# String loop 
def String_loop(text):   #รับค่า text 
    for c in text:  # ถ้าเขียนแบบนี c จะเป็นคาเเล็คเตอร์ในแต่ละอินทาเลชั่น หรือ c จะเป็น ตัวอักษรในแต่ละ text นั้นเอง
        print(f'/{c}/')  #ปริ้นค่า c ใน text คือค่าที่รับมาจาก input
text = input('Enter the text:')
String_loop(text)


# String loop v2
def String_loop2(text):   #รับค่า text 
    for c in (range(len(text))):   #แต่ถ้าเขียนแบบนี้ c จะเป็น index แทนคือ 0,1,2,3
        print(f'/{text[c]}/')  #ปริ้นค่า c ใน text คือค่าที่รับมาจาก input
text = input('Enter the text:')
String_loop2(text)


# String loop นับ text ที่เราต้องการ

def string_loop_V3(text,char): #รับค่าจาก input
    values = 0 #สร้างตัวแปร
    for i in text: # ถ้าเขียนแบบนี i จะเป็นคาเเล็คเตอร์ในแต่ละอินทาเลชั่น หรือ i จะเป็น ตัวอักษรในแต่ละ text นั้นเอง
        if i == char: # ถ้า i มีค่าเท่ากับอักษรที่กำหนดมาให้บวกตามจำนวนอักษรที่มี
            values = values + 1
    return values
        
#----- main ----#
def Input():
    text = input('Enter the text:')
    char = input('Enter the char:')
    return text,char

text,char = Input()
values = string_loop_V3(text,char)
print(f'values = {values}')