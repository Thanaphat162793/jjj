#----- Loop and Haif wiht return ----#
# คือการเอา return มาใช้ให้หลุดฟังก์ชัน
# เหรือเรียกง่ายๆว่า return เมื่อไหร่หลุดฟังก์ชันทันที
def find(text, chas, index=0): #ฟังก์ชันหา len ของ text
    text_is_index = len(text) #กำหนดให้ text_is_index = len ของ text สมมุท text = Thanaphat  len ของ textคือ 8  นับจาก 0,1,2,3....
    while index < text_is_index: #ถ้า index ยังน้อยกว่า len ของ text ก็ทำการบวก index ไปเรื่อยๆ 
        if text[index] == chas:  # แต่ถ้า index ของ text = chas จะreturn ค่าของ index ทันที
            return index       # แต่ถ้า index ของ text = chas จะreturn ค่าของ index ทันที
        index = index + 1  #ถ้า index ยังน้อยกว่า len ของ text ก็ทำการบวก index ไปเรื่อยๆ 
    return -1   #แต่ถ้า index เยอะกว่า text = Thanaphat  len ของ textคือ 8  นับจาก 0,1,2,3.... ถ้า index เยอะกว่า8 จะreturn-1
text = input('Enter a text: ')
chas = input('Enter a chas: ')
index = 0
find = find(text,chas,index=0)
print(f'the index of {text} is {find}')