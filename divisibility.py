# divisibility
num = int(input("Enter a Number: "))  # user input
# modulus operator
five = num % 5 == 0
seven = num % 7 == 0
eleven = num % 11 == 0
even = num % 2 == 0
# if else statement
if five or seven or eleven or even:
    if five:
        print("The number is divisible by 5")
    if seven:
        print("The number is divisible by 7")
    if eleven:
        print("The number is divisible by 11")
    if even:
        print("The number is divisible by 2")
else:
    print("Not divisible by 5, 7 or 11")
