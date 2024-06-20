

# ------- การทำงานของ range function ------#

               #ค่าเริ่มต้นคือ 5   ค่าที่จะถึง 10   เพิ่มทีละ2   ----==ลูบที่ได้คือ 3 ครั้ง เพราะฟังก์ชันนี้นับจาก 0,1,2,...... เเละจะไม่นับเลข stop คือ 10
for i in range(      5       ,    10   ,     2   ):
    print(10+10)

# --- ตัวอย่างการ loop ค่าฟาเลนไฮกับเชลเชียล ------#
def fah_to_cel(start,stop,step):
    print(f"    {'Fahrrenheit'}             {'Celcius'}")
    print(f"    {'______________'}          {'__________'}")

    for fah in range(start,stop,step):
        cel = (5/9)*(fah-32)
        print (f" {fah:.2f}                      {cel:.2f}")

    print(f"  {'_________________'}         {'_______________'}")
#---- main ----#
def Input():
    start = int(input("Enter the start"))
    stop = int(input("Enter the stop"))
    step = int(input("Enter the step"))
    return start,stop,step

start,stop,step = Input()
fah_to_cel(start,stop,step)




# ----- Example factorial -----#

def factorial(n):
    result = 1
    for i in range(n,1,-1):
        result = result*i
    return result

def Input():
    n = int(input('Enter the fcatorial:'))
    return n
#------ main ----#
n = Input()
values = factorial(n)
print(f'{values}')




#------ Example: Average of Numbers -----#

import sys
def average(n):
    sum = 0
    for i in range(n):
        number = float(input(f'Enter numbers #{i+1} '))  ######------- การทำลูบ input
        sum = number+sum/n
    return sum

n = int(input("How many average: "))
if n <= 0 :
    print('good bay see you agan ')
    sys.exit()


#------ main ----#
agv = average(n)
print(agv)