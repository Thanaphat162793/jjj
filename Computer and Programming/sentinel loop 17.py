#การเขียนแบบถ้าต้องการออกจากโปรแกรม ให้กด enter
def average():
    sum = 0
    conla = 0
    numbers = 0
    while numbers != "": #ถ้าต้องการออกจากโปรแกรม ให้กด enter
        numbers = (input('Enter values: '))
        numbers = float(numbers)
        sum = sum+numbers
        conla = conla+1
        numbers = (input('Enter values if quit a progarm // Enter //'))
    return sum/conla,conla
avg,conla = average()
print(f'average is {avg} by loop {conla}') 



##----- Example: finding maximum -----###

# หาค่าสูงสุดของจำนวนเลขที่ใส่มา
def find_maxvalues():
    numbers = float(input('Enter a values: '))
    max = 0
    while numbers >= 0 : #ถ้าใส่ เลขติดลบจะหลุดลูบทันที
        if numbers > max:
            max = numbers
        else:
            max = max
        numbers = float(input('Enter a values if quit a progarm: '))
        if numbers <= 0:
            print('error a progarm')
    return max
max = find_maxvalues()
print(f'max is values {max}')

