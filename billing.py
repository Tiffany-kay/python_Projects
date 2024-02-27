# electric bill calculation
# user defined function
def electric_bill(name, id, units):
    if units <= 199:
        charges = units * 1.20
    elif units >= 200 and units < 400:
        charges = units * 1.50
    elif units >= 400 and units < 600:
        charges = units * 1.80
    elif units >= 600:
        charges = units * 2.00
    else:
        print("invalid unit")
    # surcharge calculation
    if charges < 100:
        charges = 100
    if units > 400:
        surcharge = charges * 0.15
        charges += surcharge
    total_bill = charges + surcharge

    print(f"Customer Name: {name}")
    print(f"Customer ID: {id}")
    print(f"Units Consumed: {units}")
    print(f"Electric Charges: {charges:.3f}")
    print(f"Total bill: {total_bill:.3f}")


name = input("Enter your name: ")
id = input("Enter your ID: ")
units = float(input("Enter your units: "))
electric_bill(name, id, units)  # function call
