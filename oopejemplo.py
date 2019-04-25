from datetime import date
import datetime

class Persona:

    personas = []

    def __init__(self, personas):
        self.personas = personas

    def calcular_edad(self, fecha_nac):
        today = date.today()
        return today.year - fecha_nac.year - ((today.month, today.day) < (fecha_nac.month, fecha_nac.day))


class Cliente(Persona):

    edad = 0

    def __init__(self, nombre, fecha_nacimiento):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = self.calcular_edad(fecha_nacimiento)

    def descripcion(self):
        return "La persona {} tiene {} años".format(
            self.nombre, self.edad
        )

lista_clientes = [
    Cliente("Juanjo", datetime.date(1978, 4, 17)),
    Cliente("Cony", datetime.date(2005, 5, 21))
]

lista_personas = Persona(lista_clientes)
for p in lista_personas.personas:
    print(p.descripcion())

