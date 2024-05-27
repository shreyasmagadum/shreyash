class Animal:

    def pp(self):
        print("i am super class")
    def speak(self):
        pass  # Abstract method

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()
dog.pp()
cat.pp()
print(dog.speak())
print(cat.speak())