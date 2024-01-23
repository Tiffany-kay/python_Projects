import sys  # used to import the sys module

year = input("Enter your birth year: ")  # user input
print(type(year))
size_year = sys.getsizeof(year)  # function to determine size of user input
age = 2024 - float(year)
print("your age=", age)
print(type(age))
height = input("Enter your height in meters:")  # user input
print(type(height))
size = sys.getsizeof(height)  # function to determine size of user input
print(" size of height", size, "bytes....." " Size of year", size_year, "bytes")
