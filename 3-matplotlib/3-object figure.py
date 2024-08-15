import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0, 10, 11)
b = a ** 4
x = np.arange(0, 10)
y = 2 * x

fig = plt.figure()
axes1 = fig.add_axes(([0.1, 0.1, 0.8, 0.8]))
axes1.plot(a, b)
axes1.set_xlim(0,8)
axes1.set_ylim(0,8000)
axes1.set_xlabel('A')
axes1.set_ylabel('B')
axes1.set_title("First")
axes2 = fig.add_axes([0.3, 0.3, 0.5, 0.5])
axes2.plot(a, b)
axes2.set_xlim(1,2)
axes2.set_ylim(0,50)
axes2.set_xlabel('A')
axes2.set_ylabel('B')
axes2.set_title("Zoom first one")
plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
#
# fig = plt.figure()
# fig.subplots_adjust(top=0.8)
# ax1 = fig.add_subplot(211)
#
# t = np.arange(0.0, 1.0, 0.01)
# s = np.sin(2 * np.pi * t)
# line, = ax1.plot(t, s, color='green', lw=2)
#
# np.random.seed(19680801)
#
# ax2 = fig.add_axes([0.15, 0.1, 0.7, 0.3])
# n, bins, patches = ax2.hist(np.random.randn(1000), 50,
#                             facecolor='yellow',
#                             edgecolor='yellow')
#
# fig.suptitle('matplotlib.figure.Figure.add_axes() \
# function Example\n\n', fontweight='bold')
#
# plt.show()
