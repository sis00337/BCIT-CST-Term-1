"""
Author: Min Soo Hwang
Github ID: Delivery_KiKi
Description: Calculate how many cans of paint are needed to paint a room
             with a can of paint that can always cover 40 square metres.
"""


COVERAGE = 40
length = int(input("Enter the length of the room in metres : "))
width = int(input("Enter the width of the room in metres : "))
height = int(input("Enter the height of the room in metres : "))
coats = int(input("Enter the number of coats : "))
surface_area = (length * width) + (width * height * 2) + (length * height * 2)
coverage_needed = surface_area * coats
cans_of_paint_required = (coverage_needed / COVERAGE)
if cans_of_paint_required - int(cans_of_paint_required) != 0:
    cans_of_paint_required = int(cans_of_paint_required) + 1
    print("You need to buy", cans_of_paint_required, "cans of paint")
else:
    print("You need to buy", int(cans_of_paint_required), "cans of paint")
