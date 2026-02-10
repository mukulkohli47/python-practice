# take input in celsius and convert it to fahrenheit and kelvin and print all three values with their data types

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print("Temperature in Celsius: ", celsius, "\nData type of Celsius: ", type(celsius))
print("Temperature in Fahrenheit: ", fahrenheit, "\nData type of Fahrenheit: ", type(fahrenheit))
print("Temperature in Kelvin: ", kelvin, "\nData type of Kelvin: ", type(kelvin))