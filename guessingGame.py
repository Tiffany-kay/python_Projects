# guessing game (if-else condition only)
# user input
try:
    Win_num: int = 34
    num = int(input("You have to guess a number bruh: "))
except ValueError:
    print("Be serious😤😤😤😤")
    exit()
# if else statement
if num == Win_num:
    print("Damn you are good😎")
elif num < Win_num:
    print("Too low😪😪😪🥱... try harder bruh")
elif num > Win_num:
    print("sheeesh...Lower your ambitions.. Too high😛😛😛")
else:
    print("Be serious😤😤😤😤")
