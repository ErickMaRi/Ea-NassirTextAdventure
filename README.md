# Ea-NassirTextAdventure
# Proyecto de Juego de Economía Hiperrealista

## Descripción
Este proyecto simula una economía hiperrealista con un enfoque en la compra y venta de cobre. El personaje principal, Ea-Nasir, debe navegar a través de eventos económicos para hacer crecer su riqueza y reputación. 

## Índice
- [Descripción](#descripción)
- [Instalación](#instalación)
- [Cómo jugar](#cómo-jugar)
- [Características](#características)
- [Librerías utilizadas](#librerías-utilizadas)
- [TODOs](#todos)

## Instalación
Para instalar el juego, clona este repositorio y ejecuta el archivo principal en Python.

```bash
git clone <https://github.com/ErickMaRi/Ea-NassirTextAdventure>
cd <Ea-NassirTextAdventure>
python ea.py
```

## Cómo jugar
Después de iniciar el juego, se te presentarán varias opciones:
- Ir al mercado para comprar o vender cobre.
- Ir al taller para producir bienes.
- Descansar en la residencia de Ea-Nasir.

## Características
- Simulación de eventos económicos como guerras, paz, huelgas, etc.
- Opciones para comprar y vender cobre y bienes terminados.
- Registro de transacciones y estado financiero.
- Sistema de hambre y aburrimiento para Ea-Nasir.
- Guardado y carga de partidas.

## Librerías utilizadas
- `csv` para el sistema de guardado y carga de partidas.
- `matplotlib` para gráficos y visualizaciones.
- `random` y `numpy` para la generación de números aleatorios y cálculos.

## TODOs
Añadir la funcionalidad para ir a comprar comida con efectos.

Documentar todos los métodos y clases.

- Añadir más eventos en todos los lugares, implementar un sistema de eventos similar al de la economía pero en los distintos lugares:
    1. Asaltan a EaNassir.
    2. Ea nassir queda dormido en su casa y la economía avanza.
    3. Ea nassir recuerda algo que odia y su aburrimiento aumenta.
    4. Ea nassir tropieza con una persona importante, dañando su reputación.
    ...

- Implementar la compra de cobre barato, y la venta del mismo a sobreprecio como una mecánica del juego,
    por lo que Ea requiere un skill nuevo, el appraising, hay bastante inspiración que tomar de Dwarf Fortress
    esto por supuesto que debe venir de la mano con las famosas tabletas de arcilla, talvez estas sirvan para 
    evitar perder tanta reputación por vender cobre de mala calidad. En el mercado aveces deberían intentar venderle
    a EaNassir cobre de mala calidad, para esto el appraising. 
        ¿Un modelo de lenguaje pequeño para sintetizar quejas?
        ¿Un modelo de markov para sintetizar quejas (más lijero)?

- Verificar el guardado y cargado de partidas.

- Implementar pruebas unitarias para todos los métodos.

- Verificar el comportamiento del juego para un jugador que toma decisiones aleatorias para realizar un análisis
    estadístico del juego para un conjunto de parámetros dado, talvez sería bueno que el juego sea contenido
    en una clase más grande para la cual la inicialización se de con los parámetros actuales por defecto pero permita
    editarlos y correr la verificación.
