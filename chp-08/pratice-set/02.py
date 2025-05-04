#  Write a python program using function to convert Celsius to Fahrenheit.

def C_to_F(param):
    return (param * 9/5) + 32


arg = int(input("Convert °C to °F : "))
print(f"{arg}°C is {C_to_F(arg)}°F")
