import math;
r = float(input("Input the radius of the circle : "))
print("Input the radius of the circle :",r,"The area of the circle with radius ",r,"is:",(math.pi*r*r))
#print("Input the radius of the circle : %.1f"%r,"The area of the circle with radius  %.1f"%r,"is: %.16f "%(math.pi*r*r))  



n = str(input())
ext = n.split(".")
if ext[1]=="py":
    print("Input the Filename:",n,"The extension of the file is:'python'")
else:
    print("Input the Filename:",n,"The extension of the file is:'%s'"%ext[1])

   
'''
dict1 = {"py":"Python",
        "c":"C",
        "java":"java",
        "html":"html"
        }
file=str(input())
ext1 = file.split(".")
print("Input the Filename:",file,"The extension of the file is:",(dict.get(ext1[1])))
'''
