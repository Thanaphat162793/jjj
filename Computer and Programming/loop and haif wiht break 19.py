# คำสั่ง break คือคำสั่งที่เมื่อใช้แล้วจะหลุดออกจากแค่ loop ไม่ได้หลุดออกจากฟังก์ชันเหมือน return
def chla(text,chal):
    result = "flase"  
    for c in text:
       if c == chal:
            result = "True"
            break  #เมื่อใช้คำสั่ง break จะหลุดออกจาก loop และจะมาต่อที่บรรทัดที่ 8 เลยคือ return
    return result #ทำการ นำค่าไปเก็บไว้ใน ฟังก์ชั่น


text = input('Enter a text: ')
chal = input('Enter a chal: ')
values = chla(text,chal)
print(f'the chla of {values}')