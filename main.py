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
       
class Horse(Mammal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def make_sound(self):
        print(f"{self._name} : Neigh")
    def move(self):
        print(f"{self._name} is galloping")

class Cow(Mammal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def make_sound(self):
        print(f"{self._name} : Moo")
    def move(self):
        print(f"{self._name} is walking")

class Sheep(Mammal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def make_sound(self):
        print(f"{self._name} : Baa")
    def move(self):
        print(f"{self._name} is trotting")

class Elephant(Mammal):
    def __init__(self, name, age, size):
        super().__init__(name, age)
        self.size = size
    def make_sound(self):
        print(f"{self._name} : Trumpets")
    def move(self):
        print(f"{self._name} is lumbering")

class Dolphin(Mammal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species
    def make_sound(self):
        print(f"{self._name} : Clicks")
    def move(self):
        print(f"{self._name} is swimming")

#Testing
mammals = [
    Dog(name="Max", age=5, breed="Golden Retriever"),
    Cat(name="Pitchup", age=3, color="Black"),
    Horse(name="Spirit", age=7, breed="Mustang"),
    Cow(name="Basso", age=4, breed="Holstein"),
    Sheep(name="Rio", age=2, breed="Merino"),
    Elephant(name="Dabdob", age=10, size="Large"),
    Dolphin(name="Rwiyssi", age=6, species="Bottlenose"),
] 
for mammal in mammals:
    mammal.make_sound()
    mammal.move()