FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return FAHRENHEIT_TO_CELSIUS_FACTOR * fahrenheit -32

def convert_to_fahrenheit(celsius):
    return CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32
while True:
    temp = input("Enter the temperature to convert: ")
    try:
        temp_int = int(temp)
        break
    except ValueError:
        print("That is not a valid integer.")
while True:
    type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if(type.lower() == "c" or type.lower() == "f"):
        break
    else:
        print("That is not a valid unit of temperature.")
if type.lower() == "c":
    print(f"{temp}°C is {convert_to_fahrenheit(temp_int)}°F")
else:
    print(f"{temp}°F is {convert_to_celsius(temp_int)}°C ")