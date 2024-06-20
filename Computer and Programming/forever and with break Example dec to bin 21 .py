# คือการเขียนแบบแปลงเลขฐาน 10 เป็นเลขฐาน 2 หรือแปลงจำนวนจริงเป็นเลขฐาน 2
def dec_to_bin(n):
    binary = ''
    while True: #สร้าง forever loop มา
        binary = str(n % 2) + binary #n%2,n//2 คือสูตรการหาเลขฐาน 2
        n = n //2
        if n == 0:
            break
    return binary
while True: #สร้าง forever loop มาเพื่อใช้คำสั่งเรื่่อยๆ
    n = int(input('enter a value: '))
    if n < 0:
        break
    print(dec_to_bin(n))
print('Good bye')
   