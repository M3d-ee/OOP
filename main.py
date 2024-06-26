class Mammal:
    def __init__(self, name, age):
        self._name = name  
        self._age = age  
    def make_sound(self):
       return
    def move(self):
       return 
    
class Dog(Mammal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self._breed = breed
    def make_sound(self):
        print(f"{self._name} : Woof ")
    def move(self):
        print(f"{self._name} is running")

class Cat(Mammal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self._color = color
    def make_sound(self):
        print(f"{self._name} : Meow")
    def move(self):
        print(f"{self._name} is jumping")

#Testing
mammals = [
    Dog(name="Max", age=5, breed="Golden Retriever"),
    Cat(name="Pitchup", age=3, color="Black"),
] 
for mammal in mammals:
    mammal.make_sound()
    mammal.move()