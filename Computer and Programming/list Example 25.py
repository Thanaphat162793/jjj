#การหาค่าเฉลี่ยของคะแนนแล้วหาค่าที่ตำกว่าค่าเฉลี่ย
def rade_scores(): #ฟังก์ชั่่นเก็บค่าหรือ list
    scores = []
    while True:
        s1 = (input('Enter a value'))
        if s1 == "" :
            break
        scores.append(int(s1))
    return scores

def average_scores(scores): #ฟังก์ชั่นหาค่าเฉลี่ย
    sum = 0
    for s in scores:
        sum = s + sum
    return sum / len(scores) #หารด้วยพื้นที่่ของ list

def print_below(average,scores): #หาค่าที่ตำสุด
    for s in scores:
        if average > s:
            avg = s
    return avg
#----- main ---#
scores = rade_scores()
average = average_scores(scores)
below = print_below(average,scores)
print(f'the average of {average} and below {below}')