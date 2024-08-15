import numpy as np
import matplotlib.pyplot as plt

m = np.linspace(0, 10, 11)
print(f"Массив m должен выглядеть вот так: \n\n{m}")
c = 3 * 10 ** 8

E = m * c ** 2

fig = plt.figure()

ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(E,label='E=mc^2', color="red",lw=5)
ax.set_yscale("log")
ax.set_facecolor('darkred')
plt.xlim(0,10)
plt.title("E=mc^2")
plt.ylabel("Energy in Joules")
plt.xlabel("Mass in Grams")

plt.gcf()
# plt.figure(facecolor='black')
# plt.tight_layout()
plt.grid(which='both',axis='y')
plt.show()