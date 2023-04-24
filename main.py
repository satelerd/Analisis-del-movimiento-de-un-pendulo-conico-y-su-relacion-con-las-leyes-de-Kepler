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

import matplotlib.pyplot as plt
import math


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


def calculate_areas(x, y):
  areas = []
  for i in range(len(x) - 1):
    x1, y1 = x[i], y[i]
    x2, y2 = x[i + 1], y[i + 1]
    area = 0.5 * abs(x1 * y2 - x2 * y1)
    areas.append(area)
  return areas


def verify_kepler_second_law(areas):
  avg_area = sum(areas) / len(areas)
  area_tolerance = 0.1 * avg_area
  return all(abs(area - avg_area) <= area_tolerance for area in areas)


def plot_trajectory_and_ellipse(x, y, a, b, c):
  plt.scatter(x, y, label='Trayectoria del péndulo')

  center_x, center_y = (max(x) + min(x)) / 2, (max(y) + min(y)) / 2
  plt.plot([center_x - a, center_x + a], [center_y, center_y],
           'r-',
           label='Eje mayor (2a)')
  plt.plot([center_x, center_x], [center_y - b, center_y + b],
           'g-',
           label='Eje menor (2b)')
  plt.scatter([center_x - c, center_x + c], [center_y, center_y],
              color='red',
              label='Focos')

  plt.xlabel('Posición en x')
  plt.ylabel('Posición en y')
  plt.title('Elipse de la trayectoria')
  plt.legend()
  plt.show()


x, y = extract_coordinates(data)
a, b = calculate_semi_axes(x, y)
c = calculate_focal_distance(a, b)
areas = calculate_areas(x, y)
kepler_second_law_holds = verify_kepler_second_law(areas)

print(f'Semieje mayor (a): {a:.4f}')
print(f'Semieje menor (b): {b:.4f}')
print(f'Distancia focal (c): {c:.4f}')
print(f'La segunda ley de Kepler se cumple: {kepler_second_law_holds}')

plot_trajectory_and_ellipse(x, y, a, b, c)
