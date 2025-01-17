#list vs string คือความแตกต่างของทั้งสองนี้คือ
# list สามารถเปลี่ยนแปลงข้อมูลได้
#ส่วน string หรือ str ไม่สามารถเปลี่ยนแปลงข้อมูลได้

#ข้อระวังถ้าต้องการอ้างอิงถึงข้อมูลข้างใน list แต่ดันไปใช้เป็น list2 = list ถ้าเขียนแบบนี้จะใช้ข้อมูลข้างในอันเดียวกันเปลี่ยอันหนึ่งอีกอันก็จะเปลี่ยนด้วย
#ให้ใช้คำสั่งนี่คัดลอกข้อมูลข้างใน

>>> num = [1,2,3]
>>> num2 = list(num)
>>> num2[0] = 10 
>>> num
[1, 2, 3]
>>> num2
[10, 2, 3]
>>>

#และสามารถใช้ in โอบาเลเตอร์ได้
#โดยคำสั่้งนี้จะใช้เช็คว่ามีค่าด้ายหน้า in มั้ยเช่น
>>> list = [1,2,3,4,5]
>>> 5 in list
True
>>> 10 in list
False
>>>


#Example-การใช้ in

text = input('Enter a text: ')
count = 0
for c in text:
    if c in "AEIOUaeiou":
        count = count + 1
print(f'The vowels of {count}')