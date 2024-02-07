while True:
    try:
        m1 = int(input("Enter your maths marks: "))
        if m1 < 0 or m1 > 100:
            print("Marks should be between 0 and 100.")
            continue
        break
    except ValueError:
        print("Please enter valid marks.")
while True:
    try:
        m2 = int(input("Enter your English marks: "))
        if m2 < 0 or m2 > 100:
            print("Marks should be between 0 and 100.")
            continue
        break
    except ValueError:
        print("Please enter valid marks.")
while True:
    try:
        m3 = int(input("Enter your Kiswahili marks: "))
        if m3 < 0 or m3 > 100:
            print("Marks should be between 0 and 100.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter valid marks.")
average = (m1 + m2 + m3) / 3

if 70 <= average < 100:
    print("You have A")
elif 60 <= average < 70:
    print("You have B")
elif 50 <= average < 60:
    print("You have C")
elif 40 <= average < 50:
    print("You have D")
else:
    print("FAILURE... Do better")
