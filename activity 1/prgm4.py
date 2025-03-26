import math
a = float(input("Enter the length of first side: "))
b = float(input("Enter the length of second side: "))
c = float(input("Enter the length of third side: "))
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(f"The area of the triangle is: {area:.2f}")
