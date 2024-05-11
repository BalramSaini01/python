
#to cacluate distance between 2 pint.
import math
def cacluate_distance(x1,y1,x2,y2):
    distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return distance


x1=float(input("enter the x-cordinate of first point :"))
y1=float(input("enter the y-cordinate of first point :"))
x2=float(input("enter the x-cordinate of second point :"))
y2=float(input("enter the y-cordinate of second point :"))

distances=cacluate_distance(x1,y1,x2,y2)
print(distances)