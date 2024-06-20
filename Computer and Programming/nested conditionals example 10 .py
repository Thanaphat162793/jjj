def divfivem(a): 
    rem = a % 5
    if rem == 0:
        print(f'{a}is divsisble by 5')
        print(f'the remainder is {rem}')
    elif rem == 1:
        print(f'{a}is not divsisble by 5')
        print('the remainder is 1')
    elif rem == 2:
        print(f'{a}is not divsisble by 5')
        print('the remainder is 2')                   #------- การหาค่าที่หารลงตัวด้วยเลข5 ----#
    elif rem == 3:
        print(f'{a}is not divsisble by 5')
        print('the remainder is 3')
    elif rem == 4:
        print(f'{a}is not divsisble by 5')
        print('the remainder is 4')   
def Input():
    a = float(input('Enter value:'))
    return a

# ----- main ----- #
a = Input()
values = divfivem(a)



#----- codeing Ezyez ----#
def divfivem2(b):
    rem2 = b % 5
    if rem2 == 0 :
        print(f'is divsisble by 5 ')
        print(f'the remainder is {rem2}')
    else:
        print(f'{b}is not divsisble by 5')
        print(f'the remainder is {rem2}')
#----- codeInput ----#
def Input2():
    b = float(input('Enter value:'))
    return b
#------ main -----#
b = Input2()
values = divfivem2(b)



#------ codeing BMI and weight status ----#
def bmi_weight_status(weight,height):
    bmi = weight/(height*height)
    if bmi < 18.5:
        wstatus = "underweight"
    elif bmi < 25:
        wstatus = "normal"
    elif bmi < 30:
        wstatus = "overweight"
    elif bmi > 30:
        wstatus = "obese"                                        #------------ คิดค่าดรัชณีมวลกาย (BMI)
    return bmi,wstatus
#------ codeInput ------#
def Input3():
    weight = float(input('Enter is the height:'))
    height = float(input('Enter is the weight:'))
    return height,weight

#-------- main ------#
weight,height = Input3()
bmi,wstatus = bmi_weight_status(weight,height)
print(f'the values of bmi{bmi:.2f} and the values of status {wstatus}')