import math
MATERIAL_DENSITY = 2.70

def compute_circle_area (radins):
    circle_area = math.pi*radins**2
    return circle_area

def flat_washer_weight (outter_r , inter_r , thickness):
    rem_area =  compute_circle_area(outter_r)-compute_circle_area(inter_r)
    return rem_area*thickness*MATERIAL_DENSITY

outter_rad = float(input('ขอบด้านนอก:'))
inter_rad = float(input('ใส่ขอบด้านใน:'))
thickness = float(input('ความหนาของชิ้นงาน'))
quantity = int(input('จำนวนชิ้นงาน'))

unit_weight = flat_washer_weight(outter_rad,inter_rad,thickness)
totle_weight = unit_weight*quantity
print(f'น้ำหนักของชิ้นงานคือ {totle_weight:.2f}')
