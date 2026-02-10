# program that takes total bill amount and number of people as input and calculates the amount each person has to pay also print the data type of the amount each person has to pay

total_bill = float(input("Enter the total bill amount: "))

num_people = int(input("Enter the number of people: "))

amount_per_person = total_bill / num_people

print("Each person has to pay: ", amount_per_person)
print("Data type of amount each person has to pay: ", type(amount_per_person))