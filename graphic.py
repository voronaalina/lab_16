import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 8, 51)
y = np.cos(x) + 6*x

plt.plot(x, y, 'y--', label = 'y=cos(x) + 6x')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.title('Графік функції y=cos(x)+6x')
plt.legend()

plt.savefig('z.tiff', format='tiff', dpi=400)
plt.show()
