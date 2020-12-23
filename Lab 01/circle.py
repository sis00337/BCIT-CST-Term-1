"""
Author: Min Soo Hwang
Github ID: Delivery_KiKi
Description: Calculate the area and circumference of a circle depending on the radius that the user entered,
             and print the message that describes how the area and circumference change when the radius is doubled.
"""


PI = 3.14159
radius = float(input("Enter a radius value : "))
circumference = 2 * PI * radius
print("Circumference : ", circumference)
area = PI * radius * radius
print("Area : ", area)

double_radius = radius * 2
circumference_double = 2 * PI * double_radius
print("Circumference with doubled radius : ", circumference_double)
area_double = PI * double_radius * double_radius
print("Area with doubled radius : ", area_double)

circumference_increased = circumference_double / circumference
area_increased = area_double / area
print("When you double the radius,")
print("the circumference will increase by", circumference_increased, "times, ")
print("and the area will increase by", area_increased, "times.")
