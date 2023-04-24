data = [(-0.138, 0.0), (-0.128, -0.03799), (-0.116, -0.05057),
        (-0.101, -0.0609), (-0.08234, -0.06952), (-0.06341, -0.07583),
        (-0.04505, -0.07898), (-0.02496, -0.08099), (-0.004592, -0.08013),
        (0.01463, -0.07726), (0.03042, -0.07295), (0.04964, -0.06664),
        (0.06456, -0.05775), (0.07718, -0.04828), (0.08779, -0.0368),
        (0.09726, -0.02389), (0.102, -0.01184), (0.103, 0.003076),
        (0.103, 0.01771), (0.09984, 0.03263), (0.09267, 0.04583),
        (0.08234, 0.05788), (0.0703, 0.06964), (0.05681, 0.07969),
        (0.04017, 0.08772), (0.02238, 0.09289), (0.003735, 0.09719),
        (-0.0155, 0.09862), (-0.03586, 0.09776), (-0.05537, 0.09489),
        (-0.07374, 0.09001), (-0.09153, 0.08254), (-0.107, 0.07194),
        (-0.121, 0.06104), (-0.131, 0.04842), (-0.14, 0.03379),
        (-0.145, 0.01829), (-0.146, 0.003646), (-0.144, -0.01183),
        (-0.138, -0.02733), (-0.13, -0.0411), (-0.118, -0.05316),
        (-0.104, -0.06434), (-0.0881, -0.07354), (-0.07058, -0.07957),
        (-0.05221, -0.08385), (-0.03357, -0.08673)]
t = [0.067, 0.1, 0.133, 0.167, 0.2, 0.234, 0.267, 0.3, 0.334, 0.367, 0.4, 0.434, 0.467, 0.5, 0.534, 0.567, 0.601, 0.634, 0.667, 0.701, 0.734, 0.767, 0.801, 0.834, 0.868, 0.901, 0.934, 0.968, 1.001, 1.034, 1.068, 1.101, 1.134, 1.168, 1.201, 1.235, 1.268, 1.301, 1.335, 1.368, 1.401, 1.435, 1.468, 1.501, 1.535, 1.568, 1.602]



import matplotlib.pyplot as plt
import math
import numpy as np


def extract_coordinates(data):
    x = [point[0] for point in data]
    y = [point[1] for point in data]
    return x, y

def calculate_semi_axes(x, y):
    min_x, max_x = min(x), max(x)
    min_y, max_y = min(y), max(y)
    a = (max_x - min_x) / 2
    b = (max_y - min_y) / 2
    return a, b

def calculate_focal_distance(a, b):
    return math.sqrt(a**2 - b**2)

def calculate_areas(x, y, t, intervals):
    areas = []
    step = len(x) // intervals
    for i in range(0, len(x) - step, step):
        x1, y1, t1 = x[i], y[i], t[i]
        x2, y2, t2 = x[i + step], y[i + step], t[i + step]
        area = 0.5 * abs(x1 * y2 - x2 * y1) * (t2 - t1)
        areas.append(area)
    return areas

def plot_trajectory_and_ellipse(x, y, a, b, c):
    plt.scatter(x, y, label='Trayectoria del péndulo')

    center_x, center_y = (max(x) + min(x)) / 2, (max(y) + min(y)) / 2
    plt.plot([center_x, center_x + a], [center_y, center_y], 'r-', label='Semieje mayor (a)')
    plt.plot([center_x, center_x], [center_y, center_y + b], 'g-', label='Semieje menor (b)')
    plt.scatter([center_x + c, center_x - c], [center_y, center_y], color='red', label='Focos')

    # Dibujar elipse
    angle = np.linspace(0, 2 * np.pi, 100)
    elipse_x = center_x + a * np.cos(angle)
    elipse_y = center_y + b * np.sin(angle)
    plt.plot(elipse_x, elipse_y, 'b-', label='Elipse ajustada')

    plt.xlabel('Posición en x')
    plt.ylabel('Posición en y')
    plt.title('Comparación de la elipse ajustada y la trayectoria real')
    plt.legend(loc='upper right')
    plt.show()


x, y = extract_coordinates(data)
a, b = calculate_semi_axes(x, y)
c = calculate_focal_distance(a, b)


print(f'Semieje mayor (a): {a:.4f} m')
print(f'Semieje menor (b): {b:.4f} m')
print(f'punto focal (c): {c:.4f} m')
print(f'Excentricidad (c/a): {c / a:.4f}')

plot_trajectory_and_ellipse(x, y, a, b, c)
