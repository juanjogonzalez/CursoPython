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
        return "{} says {}".format(
            self.name, sound
        )


philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)

print("{} is {} and {} is {}.".format(
    philo.name, philo.age, mikey.name, mikey.age
))

if philo.species == "mammal":
    print("{0} is a {1}!".format(philo.name, philo.species))

print(mikey.description())
print(mikey.speak("Guau Guau"))