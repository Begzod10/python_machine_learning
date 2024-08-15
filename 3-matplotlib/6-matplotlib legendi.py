import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 11, 10)
fig = plt.figure()

ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(x, x, label='x vs x', color="green", lw=1, marker='o')
ax.plot(x, x ** 2, label='x vs x2', color="red", ls='--', marker="+", ms=20)
# ax.legend(loc='upper left')
# ax.legend(loc=0)
ax.legend(loc=(0.5, 0.5))
plt.show()
