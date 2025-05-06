import matplotlib.pyplot as plt
import numpy as np

num_b = 3000
num_n = 12
num_fi = 6

def simular_plinko(b, n, fi):
    posiciones_finales = []
    for _ in range(b):
        pasos = np.random.choice([0, 1], size=n)
        pos = sum(pasos)  
        fila = int(pos * fi / (n + 1))  
        posiciones_finales.append(fila)
    return posiciones_finales

def mostrar_resultado(posiciones, fi):
    plt.figure(figsize=(10, 5))
    plt.hist(posiciones, bins=range(fi + 1), edgecolor='black', align='left', color='green')
    plt.title(f"Caída de las {len(posiciones)} bolitas")
    plt.xlabel("Fila de destino")
    plt.ylabel("Distribución de las bolitas")
    plt.xticks(range(fi))
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


pos = simular_plinko(num_b, num_n, num_fi)
mostrar_resultado(pos, num_fi)
