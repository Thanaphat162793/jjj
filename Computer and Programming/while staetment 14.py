# --- ตัวอย่างการ while loop ค่าฟาเลนไฮกับเชลเชียล ------#
def fah_to_cel(start,stop,step):
    print(f"    {'Fahrrenheit'}             {'Celcius'}")
    print(f"    {'______________'}          {'__________'}")

    fah = start
    while fah < stop:   #while loop คือคำสั่งที่ทำ loop ในเงือนไข ถ้าไม่ตรงเงือนไขที่สร้างจะหลุด while loop ทันที      #### 2 infiniet loop คือการเขียน code blox ที่ตรงเงือนไขจนไม่สามารถหลุด
        cel = (5/9)*(fah-32)                                                                            ###### เงือนไขนั้นมาได้ทำให้เกิดการ loop จนไม่มีที่สิ้นสุด เช่น (10,20,-10)
        fah = fah + step
        print (f" {fah:.2f}                      {cel:.2f}")

    print(f"  {'_________________'}         {'_______________'}")
#---- main ----#
def Input():
    start = float(input("Enter the start"))
    stop = float(input("Enter the stop"))
    step = float(input("Enter the step"))
    return start,stop,step

start,stop,step = Input()
fah_to_cel(start,stop,step)
