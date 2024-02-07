print("Het_Kothari_60004230270")
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement the 'speak' method.")


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


dog_instance = Dog("Buddy")
cat_instance = Cat("Whiskers")

print(dog_instance.speak())
print(cat_instance.speak())
