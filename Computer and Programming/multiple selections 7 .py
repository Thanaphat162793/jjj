
#การเขียนแบบหลายทางเลือก

def Find_someone_with_money(money): #หาคนที่มีเงิน
    if money > 100000 :
        moneyTHB1 = 33*money
        print(f'โคตรรวยเลยคุณมีเงิน{moneyTHB1:.2f}บาท:')
        if money >= 1000000 :
            moneyTHB = 33*money
            print(f'โคตาละรวยเลยคุณมีเงิน{moneyTHB:.2f}')
    
    else:
        money_THB = 33*money
        print(f'คุณก็ไม่ได้แย่นะคุณมีเงิน{money_THB:.2f}')

money = float(input('ใส่จำนวนเงิน:'))
Find_someone_with_money(money)




