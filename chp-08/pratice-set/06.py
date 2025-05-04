# Write a python function which converts inches to cms.

from simple_chalk import green, red

# def in_to_cm(inch):
#     if inch == 0:
#         return
#     return inch * 2.54

# conversion = in_to_cm(6)
# print(conversion)

# let's make it more better

def in_to_cm(inch):
    if inch == 0:
        print(red("Cant multiply with '0'"))
    else:
        print(inch, "inches =", green(inch * 2.54) , "centimeters")

in_to_cm(float(input("convert inches to centimeters: ")))