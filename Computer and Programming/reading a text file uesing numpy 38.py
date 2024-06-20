#การอ่านไฟร์ text ของ numpy นี้จะใช้ methods ที่ชื่อว่า loadtext() ชื่งจะต่างจาก open()โดยที่ loadtext()นี้จะแปลงไฟร์เป็นfloatเลยโดยที่เอาค่าไปหาผลลัพได้เลย

import numpy as np
data = np.loadtxt("D:\Computer and Programming\DATA\c_array.txt")
print (data)
#[1.2000e+01 2.3000e+01 4.3000e+01 4.5400e+02 5.0000e+00 6.6000e+01
 #5.6000e+01 7.0000e+00 5.6400e+02 3.3400e+02 6.5000e+01 8.6700e+02
 #9.8700e+02 6.5600e+02 4.5400e+02 5.3400e+02 5.5400e+02 5.4656e+04
 #5.6000e+01 5.6000e+01 5.6000e+01 5.6000e+01 5.0000e+00 7.8000e+01
 #6.7000e+01 9.8000e+01 9.0000e+12]## คำตอบ


import numpy as np
c_array = np.loadtxt("D:\Computer and Programming\DATA\c_array.txt")
tatul = 9/5*c_array + 32
for i in tatul:
    print (i)

# 32.0
# 50.0
# 98.60000000000001
# 122.0
# 154.4
# 212.0
