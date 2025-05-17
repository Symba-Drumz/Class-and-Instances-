class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says Woof!"
my_dog = Dog("Rusty")
print(my_dog.bark())     

class Pipe:
    def __init__(self, length, diameter, material):
        self.length = length
        self.diameter = diameter
        self.material = material

    def flow_water(self):
        print("water is flowing through the pipe.")

my_pipe = Pipe(10, 5, "PVC")
my_pipe.flow_water()  # Output: water is flowing through the pipe   

class Human:
    species = "Homo sapiens" # This is a CLASS ATTRIBUTE as it set outside the scope of any methods
    def __init__(self, name):
        self.name = name
alfa = Human("Alfa")
print(alfa.species) # Output: Homo sapiens    
print(alfa.name)    # Output: Alfa
#print(Human.name) # will out put an error because name is not a class attribute
alfa.nationality = "Kenyan" # this will be an instance attribute
print(alfa.nationality) # Output: Kenyan
alfa.species = "Python Programmer" # this will be a class attribute. Changing species using dot notation
print(alfa.species) # Output: Python Programmer
alfa.name = "Alfa Zach Mmosi"
print(alfa.name) # Output: Alfa Zach Mmosi
print(alfa.nationality) # Output: Kenyan
print(getattr(alfa, "name")) # Output: Alfa Zach Mmosi
alfa.nationality = "Kenyan"
print(setattr(alfa, "nationality", "Kenyan")) # Output: None
my_attr = "is_a_friend"
print(getattr(alfa, my_attr, False)) # Output: False

setattr(alfa, my_attr, True)
print(getattr(alfa, my_attr, False)) # Output: True
print(hasattr(alfa, my_attr)) # Output: True

class Human:
    species = "Homo sapiens" # This is a CLASS ATTRIBUTE as it set outside the scope of any methods
    def __init__(self, age):
        self.age = age

    def get_age(self):
        print("Retrieving age.")
        return self._age  
    def set_age(self, age):
        if (type(age) in (int, float)) and (0 <= age <= 120):
            print(f"Setting age to {age}.")  
            self._age = age

        else:
            print("Age must be between 0 and 120.")    

    age = property(get_age, set_age)    

my_Human = Human(20)
print(my_Human.age) # Output: 20
my_Human.age = 30
print(my_Human.age) # Output: 30
my_Human.age = False
print(my_Human.age) # Output: Age must be between 0 and 120.
