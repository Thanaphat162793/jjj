#numpy คือไลบาลี้อั่นหนึ่ง ที่เอาไว้ใข้กับภาษาอันเลกับเมตติกแล้วเหมาะกับการประมวลผลข้อมูลที่ใหญ่ๆแต่ numpyจะไม่เหมือนไลบรารี่อื่นๆอย่างเช่น math หรือซิตเซ็ม ที่ติดตั้งโปรมแกรมแล้วมาพร้อมเลย
#ที่ต้องทำคือต้องติดตั้งมันเพิ่มไม่สามารถ importมาใช้เฉยๆได้

#การสร้าง numpy

# import numpy
# a = numpy.array([1,2,3,4])

#การเขียนแบบสั่นๆหรือแบบมาตฐาน

# import numpy as np #ใส่ as np เพื่ิอที่จะเขียนย่อจาก numpyมาเป็นnp
# a = np.array([1,2,3,4])


#-----------------------  numpy vs list  -----------------------#
#ในการเขียน numpyเราจะใช้ array ซึ่งเป็นส่วนหนึ่งของการใช้ไลบราลี่ numpy
#หลักการทำงานเหมือนกันกับ list เลย
# >>> a = np.array([1,2,3,4])
# >>> a
# array([1,2,3,4])

# >>> a[2]
# 3

# >>> a[3] = 20
# >>> a 
# array([1,2,3,20])

# >>> for i in a:
#   	 print(i)
# 1
# 2
# 3
# 20

#--------------------- การเขียนแบบ nested ------------#

# import numpy as np
# >>> tabel = np.array([1,2,3] , [4,5,6])
# >>> tabel
# array([1,2,3],
#       [4,5,6]) #เห็นได้ว่า numpyมีการจัดเรียงให้


# >>> tabel[0]
# array([1,2,3])

# >>> tabel[0][1]
#2


#------------------ การใช้เครื่องหมาย +,-,*,/,** --------------#
# arrayสามารถใช้งานได้เลย
# import numpy as np
# >>> a1 = np.array([1,2,3])
# >>> a2 = np.array([4,5,6])
# >>> a1-1
# array([0,1,2])

# >>> a1+a2
# array([5,7,9])

#----------------------- เรื่ิองของ math functino ---------------#
#สามารถใช้ได้แค่บางตัวส่วนตัวไหนที่ใช้ไม่ได้ก็เพราะว่ามันมากับ numpyแล้ว วิธีใช้
# เปลี่ยนจาก math.sqrt()
# เป็น np.sqrt() แทน








    
    
    
    