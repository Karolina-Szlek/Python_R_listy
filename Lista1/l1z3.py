
"""zadanie 3

hight = eval(input("Please enter height of the dimond:"))

for i in range(hight):
    print(" "*(hight-i), "*"*(i*2+1))
for j in range(hight-2, -1, -1):
    print(" "*(hight-j), "*"*(j*2+1))"""
    
    
    
    
#zadanie 3

hight = eval(input("Please enter height of the dimond:"))

for i in range(hight+1):
    print(" "*(hight-i), "*"*(i*2+1))
for j in range(hight-1, -1, -1): # od, co ile , do 
    print(" "*(hight-j), "*"*(j*2+1))