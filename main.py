class Mammal:
    def __init__(self, name, age):
        self._name = name  
        self._age = age  

    def make_sound(self):
        return

    def move(self):
        return 

class Dog(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self._name}: Woof")

    def move(self):
        print(f"{self._name} is running")

class Cat(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self._name}: Meow")

    def move(self):
        print(f"{self._name} is jumping")

class Horse(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self._name}: Neigh")

    def move(self):
        print(f"{self._name} is galloping")

class Cow(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self._name}: Moo")

    def move(self):
        print(f"{self._name} is walking")

class Elephant(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self._name}: Trumpets")

    def move(self):
        print(f"{self._name} is lumbering")

class Wildcat(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self._name}: Growls")

    def move(self):
        print(f"{self._name} is prowling")

class Lion(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self._name}: Roar")

    def move(self):
        print(f"{self._name} is prowling")

# Testing
mammals = [
    Lion(name="Mouad", age=5),
    Dog(name="Max", age=5),
    Wildcat(name="Pitchup", age=3),
    Horse(name="Spirit", age=7),
    Cow(name="Tanoni", age=4),
    Elephant(name="Dabdob", age=10),
] 

for mammal in mammals:
    print(f"Name: {mammal._name}, Age: {mammal._age}")
    mammal.make_sound()
    mammal.move()