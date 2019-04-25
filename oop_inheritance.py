class Dog:

    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return "{} is {} years old".format(
            self.name, self.age
        )

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)



class Terrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

jim = Bulldog("Jim", 6)
print(jim.description())

print(jim.run("slowly"))

# Jim es un perro?
print(isinstance(jim, Dog))

# Julie es un perro?
julie = Dog("Julie", 100)
print(isinstance(julie, Dog))

# johnny walker es un Bulldog?
johnnywalker = Terrier("Johnny Walker", 4)
print(isinstance(johnnywalker, Bulldog))