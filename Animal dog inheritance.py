# ---- Parent (Base) class
class Animal:
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species

    def speak(self) -> str:      # To be overridden
        return f'{self.name} makes a sound'

    def describe(self):
        print(f'{self.name} is a {self.species}')


# ---- Child classes - Inherit from Animal ----
class Dog(Animal):               # Dog IS-A Animal
    def __init__(self, name, breed):
        super().__init__(name, 'Canis lupus familiaris')  # Call parent
        self.breed = breed       # New attribute

    def speak(self) -> str:      # OVERRIDE parent method
        return f'{self.name} says: Woof!'

    def fetch(self):             # NEW method - only for Dog
        print(f'{self.name} fetches the ball!')


class Cat(Animal):
    def speak(self) -> str:
        return f'{self.name} says: Meow!'


# ---- Using the hierarchy ----
dog = Dog('Rex', 'German Shepherd')
cat = Cat('Whiskers', 'Felis catus')

dog.describe()           # Inherited from Animal!
print(dog.speak())       # Dog's override: Woof!
print(cat.speak())       # Cat's override: Meow!
dog.fetch()               # Dog-only method