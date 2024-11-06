import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.3, 12.3, 500)
y = np.log(x) + 0.7 * x**2

plt.figure(figsize=(8, 6))
plt.plot(x, y, linestyle='--', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік функції y = ln(x) + 0.7x^2')
plt.grid(True)

plt.savefig(r"C:\Users\artem\OneDrive\Рабочий стол\лаби\лаб16\lab16.1\myplot.jpg")
