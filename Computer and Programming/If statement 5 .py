def height_gard(height):
    if height >= 160:
        print ('ผ่านเกน')
        print (height/2)
    
    if height < 160:
        print('ไม่ผ่านเกน:')

height= int(input('Ente is height:'))
height_gard(height)
