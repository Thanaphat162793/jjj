# 1 .# nested loop มันคือ loop ช้อน loop นั้นเองหรือลูบในลูบ
k = 5
n = 1
while n <= k:
    for i in range(n):
        print("$",end='')
    print()  #ทำการขึ้นบรรทัดใหม่
    n = n + 1
    
    
# 2 .#ข้อนี้จะมี6บรรทัดเพราะ print รอบแรกจะมี 1บรรทัด รอบที่2จะมี2บรรทัด รอบที่3จะมี3บรรทัด ซึ่งโค้ดดังกล่าว ไม่มี end = '' จะทำให้โค้ดพิม 1 $ต่อ1บรรทัด
    #แต่ถ้ามี $ทุกตัวจะรวมอยู่บรรทัดเดียวกัน
k = 3
n = 1
while n <= k:
    for i in range(n):
        print('$')
    n = n+1
        
#3.#ถ้าต้องการแบบข้อที่่ 2 ซ้อนกัน 4 อันละ
    ### ทำแบบนี้
# หรือมันคือลูบซ้อนลูบซ้อนลูบนั้นเอง
m = 4
for o in range(m):
    k = 5
    n = 1
    while n <= k:
        for i in range(n):
            print("$",end='')
        print()  #ทำการขึ้นบรรทัดใหม่
        n = n + 1
        
