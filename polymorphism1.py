class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Polymorphic function to make different animals speak
def make_animal_speak(animal):
    return animal.speak()

# Creating objects of different animal classes
dog = Dog()
cat = Cat()

# Making animals speak using polymorphism
print(make_animal_speak(dog))  # Output: Woof!
print(make_animal_speak(cat))  # Output: Meow!
