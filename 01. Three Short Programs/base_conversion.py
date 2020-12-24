"""
Author: Min Soo Hwang
Github ID: Delivery_KiKi
Description: Convert a base 10 number to a 4-digit number in another base (between 2 and 9).
"""


decimal = int(input("Enter the number in base 10 : "))
new_base = int(input("Which base is your destination base? (2 - 9) : "))
maximum = new_base ** 4 - 1
print(f"The maximum base 10 number is {maximum}.")
if decimal > maximum:
    print("Try again :(")

else:
    quotient_1 = decimal // new_base
    first_number = decimal % new_base
    if quotient_1 == 0:
        second_number = 0
        third_number = 0
        fourth_number = 0
    else:
        quotient_2 = quotient_1 // new_base
        second_number = quotient_1 % new_base
        if quotient_2 == 0:
            third_number = 0
            forth_number = 0
        else:
            quotient_3 = quotient_2 // new_base
            third_number = quotient_2 % new_base
            if quotient_3 == 0:
                forth_number = 0
            else:
                forth_number = quotient_3 % new_base

            print("The answer is",
                  str(forth_number)
                  + str(third_number)
                  + str(second_number)
                  + str(first_number)
                  + "("
                  + str(new_base)
                  + ")")
