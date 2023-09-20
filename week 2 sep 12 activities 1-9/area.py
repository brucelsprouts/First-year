#Activity 5: Area Calculator
import math

w = input("Input the width of the rectangle:")
l = input("Input the length of the rectangle:")

intW = int(w)
intL = int(l)

area = intW * intL
area = str(area)

print("")
print("Rectangle area is "+area+".")


b = input("Input the base of the triangle:")
h = input("Input the height of the triangle:")

intB = int(b)
intH = int(h)

triArea = int((intB * intH)/2)
triArea = str(triArea)

print("")
print("Triangle area is "+triArea+".")


r = input("Input the radius of the circle:")

intR = int(r)

radArea = round(math.pi * intR**2, 2)
radArea = str(radArea)

print("Circle area is "+radArea+".")



