class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"hell, my name is {self.name} an i am {self.age} years")
person = Person("john", 34)
print(person.name)
print(person.age)
person.greet()