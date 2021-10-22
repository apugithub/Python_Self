class animal():
    name = "Dog"  # name is an attribute here
    age = 11

    def change_animal (self, abc):
        self.name=abc


a = animal()


# print(a.age)
# print(a.change_animal("Cat"))


# ####################################### Init method in Python  (Which can be accessed in runtime)
class human():
    def __init__(self, name, age):
        self.name = name
        self.age = age


a1 = human("San", 12)
a2 = human("John", 17)
print(a1.name, a2.age)



