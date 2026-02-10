# take a number as input and convert to string and print both original & converted value with their data types

a = input("Enter a value: ")

convertedValue = float(a)

print("Original value: ", a, "\nData type of original value: ", type(a))
print("Converted value: ", convertedValue, "\nData type of converted value: ", type(convertedValue))