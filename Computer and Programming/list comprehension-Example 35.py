scores1 = open("D:\Computer and Programming\DATA\codeing_data.txt").read().splitlines()
scores2 = []
scores2 = [float(x) for x in scores1] #การเขียนแบบ comprehension
scores2.sort(reverse=True) #Methodsเรียงจากมากไปน้อย
for i in range(len(scores2)):
    print(f'Rank #{i+1} the scores of :{scores2[i]}')
    
print()    
#การเขียนแบบ conditional การเขียนแบบนี้เพื่ออะไรการเขียนเเบบนี้เป็นการกรองสิ่งที่เราไม่ต้องการออกไปเพื่อให้โปรแกรมเออร์เลอร์น้อยลง
  #การเขียนแบบ conditional
    
scores1 = open("D:\Computer and Programming\DATA\codeing_data.txt").read().splitlines()
scores2 = []
scores2 = [float(x) for x in scores1 if x == ""] #การเขียนแบบ conditional เงือนไขคือไม่ต้องการ ""
scores2.sort(reverse=True) #Methodsเรียงจากมากไปน้อย
for i in range(len(scores2)):
    print(f'Rank #{i+1} the scores of :{scores2[i]}')
    
    

    
    
