import random

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

    def domestication_status(self):
        return

    def fight(self, other):
        print(f"{self.get_name()} is fighting {other.get_name()}")
        result = random.choice([self, other])
        print(f"The winner is {result.get_name()}")
        return result

class Dog(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.get_name()} (dog): Woof")

    def move(self):
        print(f"{self.get_name()} is running")

    def attack(self):
        print(f"{self.get_name()} attacks")

    def action(self):
        self.attack()

    def domestication_status(self):
        return "domesticated"

class Wildcat(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.get_name()} (wildcat): Growl")

    def move(self):
        print(f"{self.get_name()} is stalking")

    def attack(self):
        print(f"{self.get_name()}'s attack: pounces")

    def action(self):
        self.attack()

    def domestication_status(self):
        return "not domesticated"

class Horse(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.get_name()} (horse): Neigh")

    def move(self):
        print(f"{self.get_name()} is galloping")

    def defend(self):
        print(f"{self.get_name()}'s defense: kicks")

    def action(self):
        self.defend()

    def domestication_status(self):
        return "domesticated"

class Cow(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.get_name()} (cow): Moooo")

    def move(self):
        print(f"{self.get_name()} is walking")

    def defend(self):
        print(f"{self.get_name()}'s defense: uses its horns")

    def action(self):
        self.defend()

    def domestication_status(self):
        return "domesticated"

class Elephant(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.get_name()} (elephant): Trumpets")

    def move(self):
        print(f"{self.get_name()} is lumbering")

    def defend(self):
        print(f"{self.get_name()}'s defense: uses its trunk")

    def action(self):
        self.defend()

    def domestication_status(self):
        return "not domesticated"

class Lion(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.get_name()} (lion): Roar")

    def move(self):
        print(f"{self.get_name()} is prowling")

    def attack(self):
        print(f"{self.get_name()}'s attack: pounce")

    def action(self):
        self.attack()

    def domestication_status(self):
        return "not domesticated"

class Dolphin(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.get_name()} (dolphin): Click-click")

    def move(self):
        print(f"{self.get_name()} is swimming")

    def defend(self):
        print(f"{self.get_name()}'s defense : by using its speed")

    def action(self):
        self.defend()

    def domestication_status(self):
        return "domesticated"

class Bat(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.get_name()} (bat): Screech")

    def move(self):
        print(f"{self.get_name()} is flying")

    def attack(self):
        print(f"{self.get_name()} attacks using its sharp teeth")

    def action(self):
        self.attack()

    def domestication_status(self):
        return "not domesticated"

class Kangaroo(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.get_name()} (kangaroo): Chortle")

    def move(self):
        print(f"{self.get_name()} is hopping")

    def defend(self):
        print(f"{self.get_name()}'s defense : uses its powerful legs")

    def action(self):
        self.defend()

    def domestication_status(self):
        return "not domesticated"

class Monkey(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.get_name()} (monkey): Chatter")

    def move(self):
        print(f"{self.get_name()} is climbing")

    def attack(self):
        print(f"{self.get_name()} attacks by throwing objects")

    def action(self):
        self.attack()

    def domestication_status(self):
        return "not domesticated"

class Whale(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.get_name()} (whale): Sings")

    def move(self):
        print(f"{self.get_name()} is swimming")

    def defend(self):
        print(f"{self.get_name()}'s defense : uses its massive tail")

    def action(self):
        self.defend()

    def domestication_status(self):
        return "not domesticated"

class Bear(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.get_name()} (bear): Growl")

    def move(self):
        print(f"{self.get_name()} is lumbering")

    def attack(self):
        print(f"{self.get_name()} attacks with its powerful claws")

    def action(self):
        self.attack()

    def domestication_status(self):
        return "not domesticated"

#testing
mammals = [
    Dog(name="Max", age=5),
    Wildcat(name="Pitchup", age=3),
    Horse(name="Spirit", age=7),
    Cow(name="Tanoni", age=4),
    Elephant(name="Dabdob", age=10),
    Lion(name="Mouad", age=5),
    Dolphin(name="Rwiyssi", age=6),
    Bat(name="Shuho", age=2),
    Kangaroo(name="Adam", age=3),
    Monkey(name="Tanoni", age=4),
    Whale(name="Ghwis", age=15),
    Bear(name="Daoudi", age=8)
]

for mammal in mammals:
    mammal.make_sound()
    mammal.move()
    mammal.action()
    print(f"{mammal.get_name()} is {mammal.domestication_status()}.")

#user's interaction
def choose_and_fight(mammals):
    for idx, mammal in enumerate(mammals):
        print(f"{idx}: {mammal.get_name()}")

    first_choice = int(input("Choose the number of the first mammal to fight: "))
    second_choice = int(input("Choose the number of the second mammal to fight: "))

    if 0 <= first_choice < len(mammals) and 0 <= second_choice < len(mammals):
        first_mammal = mammals[first_choice]
        second_mammal = mammals[second_choice]
        first_mammal.fight(second_mammal)
    else:
        print("Invalid choices. Please choose valid mammal numbers.")

choose_and_fight(mammals)
