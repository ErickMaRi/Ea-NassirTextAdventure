import csv
import matplotlib.pyplot as plt
import random
import numpy as np

"""
TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:

Añadir la funcionalidad para ir a comprar comida con efectos.

Documentar todos los métodos y clases.

Añadir más eventos en todos los lugares, implementar un sistema de eventos similar al de la economía pero en los distintos lugares:
    1-Asaltan a EaNassir.
    2-Ea nassir queda dormido en su casa y la economía avanza.
    3-Ea nassir recuerda algo que odia y su aburrimiento aumenta.
    4-Ea nassir tropieza con una persona importante, dañando su reputación.
    ...

Implementar la compra de cobre barato, y la venta del mismo a sobreprecio como una mecánica del juego,
    por lo que Ea requiere un skill nuevo, el appraising, hay bastante inspiración que tomar de Dwarf Fortress
    esto por supuesto que debe venir de la mano con las famosas tabletas de arcilla, talvez estas sirvan para 
    evitar perder tanta reputación por vender cobre de mala calidad. En el mercado aveces deberían intentar venderle
    a EaNassir cobre de mala calidad, para esto el appraising. 
        ¿Un modelo de lenguaje pequeño para sintetizar quejas?
        ¿Un modelo de markov para sintetizar quejas (más lijero)?

Verificar el guardado y cargado de partidas.

Implementar pruebas unitarias para todos los métodos.

Verificar el comportamiento del juego para un jugador que toma decisiones aleatorias para realizar un análisis
    estadístico del juego para un conjunto de parámetros dado, talvez sería bueno que el juego sea contenido
    en una clase más grande para la cual la inicialización se de con los parámetros actuales por defecto pero permita
    editarlos y correr la verificación.

TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:
"""

class EconomiaHiperrealista:
    def __init__(self, cambio=None, inflacion=None):
        self.precio_cobre = 2
        self.inflacion = 0.01
        # Definir eventos económicos con sus números de probabilidad
        self.eventos_dict = {
            "guerra": {
                "probabilidad": 20,  # Ejemplo: 20% de probabilidad
                "cambio": 1.3,
                "inflacion": 0.05
            },
            "paz": {
                "probabilidad": 35,  # Ejemplo: 30% de probabilidad
                "cambio": 0.9,
                "inflacion": -0.02
            },
            "descubrimiento de nuevo yacimiento": {
                "probabilidad": 5,  # Ejemplo: 10% de probabilidad
                "cambio": 0.85,
                "inflacion": -0.1
            },
            "huelga": {
                "probabilidad": 20,  # Ejemplo: 20% de probabilidad
                "cambio": 1.1,
                "inflacion": 0.05
            },
            "festividades": {
                "probabilidad": 20,  # Ejemplo: 20% de probabilidad
                "cambio": 0.95,
                "inflacion": -0.01
            },
            "monotonía": {
                "probabilidad": 400,  # Ejemplo: 20% de probabilidad
                "cambio": 1,
                "inflacion": 0.01
            }
        }

        # Calcular la suma total de las probabilidades
        suma_total = sum(evento["probabilidad"] for evento in self.eventos_dict.values())

        # Normalizar las probabilidades para que sumen 1
        for evento in self.eventos_dict.values():
            evento["probabilidad"] /= suma_total

    def actualizar_precio(self):
        self.precio_cobre *= (1 + self.inflacion)
        # Selección de evento basado en probabilidades
        evento = self.seleccionar_evento()
        self.precio_cobre *= self.eventos_dict[evento]["cambio"]
        self.inflacion += self.eventos_dict[evento]["inflacion"]
        return round(self.precio_cobre, 2)
    
    def reiniciar_valores(self):
        self.precio_cobre = 2
        self.inflacion = 0.01

    def seleccionar_evento(self):
        # Generar un número aleatorio entre 0 y 1
        probabilidad_aleatoria = random.random()
        prob_acumulada = 0

        # Iterar a través de los eventos y seleccionar uno basado en las probabilidades
        for evento, info_evento in self.eventos_dict.items():
            probabilidad = info_evento["probabilidad"]
            prob_acumulada += probabilidad
            if probabilidad_aleatoria <= prob_acumulada:
                return evento
        # En caso de que no se seleccione ningún evento (probabilidad total < 1)
        return list(self.eventos_dict.keys())[-1]
    
    def diagnosis3D(self, precio_cobre_maximo_values = [4,8,16,32,64,128,256,512], iteraciones_máximas=5000, bins=100):
        """Función utilizada para validar el comportamiento de la economía en 3D.

        Esta función realiza simulaciones del comportamiento de la economía actualizando el precio del cobre y
        registrando la cantidad de iteraciones necesarias para que el precio del cobre supere valores máximos
        especificados en una lista. Estas simulaciones se repiten un número determinado de veces. Luego, se
        calcula un histograma en 3D que muestra la frecuencia de iteraciones para alcanzar los diferentes precios
        máximos.

        Args:
            precio_cobre_maximo_values (list, optional): Una lista de precios máximos a alcanzar en las simulaciones.
                Defaults to [4, 8, 16, 32, 64, 128, 256, 512].
            iteraciones_máximas (int, optional): La cantidad máxima de simulaciones a realizar.
                Defaults to 5000.
            bins (int, optional): La cantidad de intervalos (bins) en el histograma. Cuanto mayor sea el número de bins,
                mayor será la resolución del histograma. Defaults to 100.

        Returns:
            None
        """
        # Create a list to store the histogram data for each precio_cobre_máximo value
        hist_data = []

        # Loop over the precio_cobre_máximo values and generate the histogram data
        for precio_cobre_maximo in precio_cobre_maximo_values:
            lista_iterador = []
            iterador = 0
            while len(lista_iterador) < iteraciones_máximas:
                economia.actualizar_precio()
                iterador += 1
                if economia.precio_cobre > precio_cobre_maximo:
                    economia.reiniciar_valores()
                    lista_iterador.append(iterador)
                    iterador = 0

            # Calculate the histogram data (frequencies)
            hist, bins = np.histogram(lista_iterador, bins=bins)  # You can adjust the number of bins
            hist_data.append(hist)

        # Create the 3D histogram plot using Seaborn
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        for i in range(len(precio_cobre_maximo_values)):
            len_data = len(hist_data[i])
            ax.bar(range(len_data), height=hist_data[i], zs=precio_cobre_maximo_values[i], zdir='y', alpha=0.8)
        ax.set_xlabel('Iteraciones para alcanzar precio')
        ax.set_ylabel('Precio máximo del cobre')
        ax.set_zlabel('Frecuencia')
        plt.show()

class BienesTerminados:
    def __init__(self, tipo, calidad):
        self.tipo = tipo  # Puede ser 'joya', 'artículo', u otro tipo de bien terminado
        self.calidad = calidad  # Puede ser 'alta', 'media', 'baja', u otra calidad

    def __str__(self):
        return f"Tipo: {self.tipo}, Calidad: {self.calidad}"

# Implementación de la clase Ea-Nasir con las mejoras para "Descanso y Hambre"
class EaNasir:
    def __init__(self):
        self.inventario = {'cobre': 10, 'bienes_terminados': [], 'dinero': 100, 'reputacion': 0, 'aburrimiento': 0, 'hambre': 0}
        self.finanzas = {'ingresos': 0, 'gastos': 0}
        self.transacciones = []

    def comprar_cobre(self, cantidad, precio_cobre):
        costo = cantidad * precio_cobre
        if costo > self.inventario['dinero']:
            print("No tienes suficiente dinero.")
            return
        self.inventario['cobre'] += cantidad
        self.inventario['dinero'] -= costo
        self.finanzas['gastos'] += costo
        self.avanzar_tiempo()
        print(f"Has comprado {cantidad} unidades de cobre por {costo} unidades de dinero.")

    def vender_cobre(self, cantidad, precio_cobre):
        if cantidad > self.inventario['cobre']:
            print("No tienes suficiente cobre para vender esa cantidad.")
            return
        ingreso = cantidad * precio_cobre
        self.inventario['cobre'] -= cantidad
        self.inventario['dinero'] += ingreso
        self.finanzas['ingresos'] += ingreso
        self.avanzar_tiempo()
        print(f"Has vendido {cantidad} unidades de cobre por {ingreso} unidades de dinero.")

    def vender_bienes(self, cantidad):
        if cantidad > len(self.inventario['bienes_terminados']):
            print("No tienes suficientes bienes terminados.")
            return
        for _ in range(cantidad):
            self.inventario['bienes_terminados'].pop()
        ingreso = cantidad * 5
        self.inventario['dinero'] += ingreso
        self.finanzas['ingresos'] += ingreso
        self.inventario['reputacion'] += 1
        self.avanzar_tiempo()
        print(f"Has vendido {cantidad} bienes terminados por {ingreso} unidades de dinero.")

    def avanzar_tiempo(self):
        self.inventario['aburrimiento'] += random.randint(0, 3)  # Random increase in boredom
        self.inventario['hambre'] += random.randint(1, 2)  # Random increase in hunger

        if self.inventario['hambre'] >= 20:
            print("Ea Nassir come de mala gana de forma apurada en un terrible local")
            self.inventario['hambre'] -= 5
            print("Esto cuesta una cantidad indecente de dinero y ni siquiera llena demasiado")
            self.inventario['dinero'] -= 10
            self.comer()
        if self.inventario['aburrimiento'] >= 20:
            print("Ea Nassir se aburre, una mente aburrida peligra")
            print("Impulsado por una picazón de manos Ea Nassir \nle juega una broma a la persona incorrecta")
            self.inventario['aburrimiento'] = random.randint(0,3)
            self.inventario['reputacion'] -= 5

    def comer(self):
        comida_disponible = self.inventario.get('food_inventory', {}).items()
        if comida_disponible:
            food_choice = random.choice(list(comida_disponible))
            food, effect = food_choice
            self.inventario['hambre'] = max(0, self.inventario['hambre'] - effect)
            print(f"Has comido {food} y reducido tu hambre en {effect} unidades.")
        else:
            print("No tienes comida en tu inventario.")

    def descansar(self):
        print("Estás aburrido. ¿Dónde te gustaría descansar?")
        opcion_descanso = input("(casa/restaurante/leer/paseo): ")
        if opcion_descanso == 'casa':
            self.inventario['aburrimiento'] = max(0, self.inventario['aburrimiento'] - 5)
        elif opcion_descanso == 'restaurante':
            self.inventario['aburrimiento'] = max(0, self.inventario['aburrimiento'] - 10)
        elif opcion_descanso == 'leer':
            self.inventario['aburrimiento'] = max(0, self.inventario['aburrimiento'] - 7)
        elif opcion_descanso == 'paseo':
            self.inventario['aburrimiento'] = max(0, self.inventario['aburrimiento'] - 8)
        else:
            print("Opción no válida.")




def guardar_partida():
    with open('partida.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for key, value in ea_nasir.inventario.items():
            writer.writerow([key, value])
    print("Partida guardada.")

def cargar_partida():
    with open('partida.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            key, value = row
            ea_nasir.inventario[key] = eval(value)
    print("Partida cargada.")

def taller_de_artesanos(self):
    print("Bienvenido al Taller de Artesanos.")
    # ASCII art to represent the workshop
    print("-------Taller-------")
    print("|                 |")
    print("|  🛠️       🛠️   |")
    print("|                 |")
    print("-------------------")

    accion = input("¿Deseas producir bienes, mejorar tus habilidades o revisar inventario? (producir/mejorar/revisar/salir): ")
    if accion == 'producir':
        if self.inventario['cobre'] == 0:
            print("No tienes suficiente cobre para producir bienes. Considera comprar más cobre primero.")
            return

        cantidad = int(input("¿Cuántos bienes deseas producir? "))
        if cantidad > self.inventario['cobre']:
            print("No tienes suficiente cobre para producir esa cantidad de bienes.")
            return

        for _ in range(cantidad):
            calidad = "alta" if self.inventario['reputacion'] > 5 else "media"
            nuevo_bien = BienesTerminados("joya", calidad)
            self.inventario['bienes_terminados'].append(nuevo_bien)
        self.inventario['cobre'] -= cantidad
        self.finanzas['gastos'] += cantidad  # Assume 1 unit of money is spent per item
        print(f"Has producido {cantidad} nuevos bienes de calidad {calidad}. Tu reputación podría aumentar si vendes estos bienes.")

    elif accion == 'mejorar':
        costo_mejora = 10
        if costo_mejora > self.inventario['dinero']:
            print("No tienes suficiente dinero para mejorar tus habilidades.")
            return
        self.inventario['dinero'] -= costo_mejora
        self.finanzas['gastos'] += costo_mejora
        self.inventario['reputacion'] += 2
        print(f"Has mejorado tus habilidades. Tu reputación ha aumentado a {self.inventario['reputacion']}.")

    elif accion == 'revisar':
        print(f"Inventario actual: {self.inventario}")

    else:
        print("Opción no válida. Regresando al menú principal.")

# Método para Residencia de Ea-Nasir en la clase EaNasir
def residencia_de_ea_nasir(self):
    print("Bienvenido a tu Residencia, Ea-Nasir.")
    # Dibujo en consola para representar la residencia
    print("-------Casa-------")
    print("| 🛏️        🪑   |")
    print("|        🌼      |")
    print("------------------")
    
    print(f"Ingresos: {self.finanzas['ingresos']}, Gastos: {self.finanzas['gastos']}")
    accion = input("¿Deseas revisar tus finanzas o descansar un poco? (finanzas/descansar/comer/salir): ")
    if accion == 'finanzas':
        print(f"Estado actual de finanzas: Ingresos: {self.finanzas['ingresos']}, Gastos: {self.finanzas['gastos']}")
    elif accion == 'descansar':
        ea_nasir.descansar()
        print("Has descansado y tu energía ha aumentado.")
    elif accion == 'comer':
        print("Decides ir por una comida")
        ea_nasir.comer()

    

# En la función iniciar_juego
def iniciar_juego():
    while True:
        print("\n¿A dónde te gustaría ir?")
        destino = input("(mercado/taller/residencia/salir): ")
        if destino == 'mercado':
            precio_cobre = economia.actualizar_precio()
            print(f"Bienvenido al Mercado de Ur. El precio del cobre hoy es {precio_cobre}.")
            accion = input("¿Qué te gustaría hacer? (comprar/vender/salir): ")
            if accion == 'comprar':
                cantidad = int(input("¿Cuánto cobre quieres comprar? "))
                ea_nasir.comprar_cobre(cantidad, precio_cobre)  # Agregamos precio_cobre como argumento
            elif accion == 'vender':
                cantidad = int(input("¿Cuántos bienes terminados quieres vender? "))
                ea_nasir.vender_bienes(cantidad)
        elif destino == 'taller':
            taller_de_artesanos(ea_nasir)
        elif destino == 'residencia':
            residencia_de_ea_nasir(ea_nasir)
        elif destino == 'salir':
            print("Gracias por jugar. Hasta luego.")
            break


def menu_principal():
    print("Bienvenido al mundo de Ea-Nasir")
    opcion = input("1. Nueva Partida\n2. Cargar Partida\n3. Salir\nElige una opción: ")
    if opcion == '1':
        iniciar_juego()
    elif opcion == '2':
        cargar_partida()
        iniciar_juego()
    elif opcion == '3':
        print("Gracias por jugar. Hasta luego.")

#EaNasir viene al mundo
ea_nasir = EaNasir()
# Crear una instancia de la clase EconomiaHiperrealista
economia = EconomiaHiperrealista()

#Iniciamos el juego
menu_principal()

#economia.diagnosis3D()