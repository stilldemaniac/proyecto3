import matplotlib.pyplot as plt  # Para graficar la distribución final
import numpy as np               # Para generar elecciones aleatorias

# Parámetros de la simulación
num_b = 3000     # Número total de bolitas que caerán
num_n = 12       # Número de decisiones aleatorias por bolita (numero de obstáculos)
num_fi = 6       # Número de filas

# Función que simula la caída de las bolitas
def simular_plinko(b, n, fi):
    posiciones_finales = []  # Lista para guardar la fila final de cada bolita

    for _ in range(b):
        # Cada bolita toma 12 decisiones: 0 (izquierda) o 1 (derecha)
        pasos = np.random.choice([0, 1], size=n)

        # La posición base es la cantidad de veces que fue a la derecha 
        pos = sum(pasos)

        # Convertir esa posición a una de las 'fi' filas disponibles
        fila = int(pos * fi / (n + 1))

        # Agregar la fila final al registro
        posiciones_finales.append(fila)

    return posiciones_finales  # Devuelve la lista de filas donde cayó cada bolita

# Función que grafica la distribución final de bolitas por fila
def mostrar_resultado(posiciones, fi):
    plt.figure(figsize=(10, 5))  # Tamaño de la grafica

    # Histograma: cuenta cuántas bolitas cayeron en cada fila
    plt.hist(posiciones, bins=range(fi + 1), edgecolor='black', align='left', color='green')

    # Títulos y etiquetas
    plt.title(f"Caída de las {len(posiciones)} bolitas")
    plt.xlabel("Fila de destino")
    plt.ylabel("Distribución de las bolitas")

    # Etiquetas del eje X: una por fila
    plt.xticks(range(fi))

    # Marca la cuadricula
    plt.grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()  # Ajusta el marguen
    plt.show()          # Muestra la grafica

# Imprime la grafica
pos = simular_plinko(num_b, num_n, num_fi)
mostrar_resultado(pos, num_fi)