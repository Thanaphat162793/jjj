#list with built in functinos-example #---- list built in functinos เพิ่มเติม
def show_score_summary(score): #function printค่า
    for i in range(len(score)):
        print(f'student #{i+1} score {score[i]}')

def score(): #function เก็บค่า
    list = []
    while True:
        score =(input('Enter a score'))
        if score == "":
            break
        list.append(float(score))
    return list

score = score()
show_score_summary(score)

