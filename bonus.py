# code to compute employee bonus
salary = int(input("Enter your salary: "))
years = int(input("Enter your years of service: "))
# if else statement
if years > 10:
    bonus = 0.1 * salary
    netBonus = bonus + salary
elif years >= 6:
    bonus = 0.08 * salary
    netBonus = bonus + salary
    print("Your net Bonus=", netBonus)
elif years < 6:
    bonus = 0.05 * salary
    netBonus = bonus + salary
else:
    print("No bonus for you 😥")

print("Your bonus:", bonus)
print("Your net salary=", netBonus)




