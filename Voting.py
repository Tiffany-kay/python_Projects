# code to check viability to vote
age = int(input("Enter your age: "))  # user input type int
nationality = input("Enter your nationality: ")  # user input
# if-else statement with the use of various operators to set conditions required to be met
if age >= 18 and nationality.lower() in ["kenya", "tanzania", "uganda"]:
    print(" You are eligible for voting")
else:
    print("You don't meet necessary requirements")
