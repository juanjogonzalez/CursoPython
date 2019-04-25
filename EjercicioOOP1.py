class Dog:

    #Atributo de la clase
    species = 'mammal'

    # Inicializador de la clase y los atributos
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Crear instancias de la clase
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 10)
toby = Dog("Dog", 12)

# Determinar cual es el perro mas viejo
def get_biggest_number(*args):
    return max(args)

print("El perro mas viejo tiene {} años".format(
    get_biggest_number(philo.age, mikey.age, toby.age)
))