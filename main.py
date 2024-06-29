class Mammal:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def make_sound(self):
        return

    def move(self):
        return
    
    def action(self):
        return

class Dog(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.get_name()}: Woof")

    def move(self):
        print(f"{self.get_name()} is runing")

    def attack(self):
        print(f"{self.get_name()} attacks")

    def action(self):
        self.attack()

  
class Wildcat(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.get_name()}: Growl")

    def move(self):
        print(f"{self.get_name()} is stalking")

    def attack(self):
        print(f"{self.get_name()}'s attack: pounces")

    def action(self):
        self.attack()


class Horse(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.get_name()}: Neigh")

    def move(self):
        print(f"{self.get_name()} is galloping")

    def defend(self):
        print(f"{self.get_name()}'s defense: kicks")

    def action(self):
        self.defend()    

class Cow(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.get_name()}: Moooo")

    def move(self):
        print(f"{self.get_name()} is walking")

    def defend(self):
        print(f"{self.get_name()}'s defense: uses its horns")

    def action(self):
        self.defend()    

class Elephant(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.get_name()}: Trumpets")

    def move(self):
        print(f"{self.get_name()} is lumbering")

    def defend(self):
        print(f"{self.get_name()}'s defense: uses its trunk")

    def action(self):
        self.defend()    

class Lion(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.get_name()}: Roar")

    def move(self):
        print(f"{self.get_name()} is prowling")

    def attack(self):
        print(f"{self.get_name()}'s attack: pounce")

    def action(self):
        self.attack()    

#testing
mammals = [
    Dog(name="Max", age=5),
    Wildcat(name="Pitchup", age=3),
    Horse(name="Spirit", age=7),
    Cow(name="Tanoni", age=4),
    Elephant(name="Dabdob", age=10),
    Lion(name="Mouad", age=5),
] 

for mammal in mammals:
    mammal.make_sound()
    mammal.move()   
    mammal.action()
