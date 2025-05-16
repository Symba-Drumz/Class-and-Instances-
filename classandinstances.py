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