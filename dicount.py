# program to calculate discount
amount = float(input("Enter the amount:"))  # user input
# if else statement
if amount > 1000:
    discount = 0.05 * amount
    print("The discount is:", discount)
else:
    print("No discount:")