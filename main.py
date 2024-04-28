import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider
from scipy.stats import multivariate_normal

# Parámetros de la simulación
diametro = 10  # Diámetro del cuarto circular
centro = [0, 0]  # Centro del cuarto

# Crear la grilla donde se calcularán los valores de la distribución
x = np.linspace(-diametro/2, diametro/2, 500)
y = np.linspace(-diametro/2, diametro/2, 500)
X, Y = np.meshgrid(x, y)
pos = np.empty(X.shape + (2,))
pos[:, :, 0] = X
pos[:, :, 1] = Y

# Corregiremos la función de distribución personalizada para que refleje una mayor cantidad de pedazos en el centro
# cuando la fuerza es menor y viceversa.

def updated_bivariate_distribution(centro, diametro, fuerza, X, Y):
    # La desviación estándar en el centro será inversa a la fuerza para que haya menos en el centro cuando la fuerza es mayor.
    std_dev_centro = diametro / (2 * fuerza) if fuerza > 0 else diametro
    
    # La distribución para los bordes tendrá una desviación estándar constante para evitar que los pedazos se alejen demasiado.
    std_dev_bordes = diametro / 2

    # Distribuciones para el centro y los bordes.
    rv_centro = multivariate_normal([centro[0], centro[1]], [[std_dev_centro, 0], [0, std_dev_centro]])
    rv_bordes = multivariate_normal([centro[0], centro[1]], [[std_dev_bordes, 0], [0, std_dev_bordes]])
    
    # Se pondera más la distribución del centro cuando la fuerza es menor.
    Z_centro = rv_centro.pdf(pos)
    Z_bordes = rv_bordes.pdf(pos)
    Z = Z_centro * (1 - fuerza/10) + Z_bordes * (fuerza/10)

    # Aplicar recorte circular para ajustar al cuarto
    Z[X**2 + Y**2 > (diametro/2)**2] = 0

    return Z

# Función para actualizar la gráfica
def update_distribution(val):
    ax.clear()
    fuerza = slider_fuerza.val

    Z = updated_bivariate_distribution(centro, diametro, fuerza, X, Y)

    # Graficar la superficie
    ax.plot_surface(X, Y, Z, cmap='viridis')

    # Configuración de la visualización
    ax.set_xlim([-diametro/2, diametro/2])
    ax.set_ylim([-diametro/2, diametro/2])
    ax.set_zlim([0, np.max(Z)])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Porcentaje de fragmentos')
    plt.title("Distribución de los pedazos de la copa en el cuarto")

# Crear la figura y los ejes para la visualización 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Espacio para el slider de la fuerza
ax_fuerza = plt.axes([0.2, 0.01, 0.65, 0.03], facecolor='lightgoldenrodyellow')

# Crear el slider
slider_fuerza = Slider(ax_fuerza, 'Fuerza', 0.1, 10.0, valinit=1.0)

# Conectar el evento de cambio de slider con la función de actualización
slider_fuerza.on_changed(update_distribution)

# Inicializar la gráfica con la distribución actualizada
update_distribution(1.0)

plt.show()

