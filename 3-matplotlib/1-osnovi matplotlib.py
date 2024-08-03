import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10)
y = x * 2
plt.plot(x, y)
plt.title('Test title')
plt.xlabel('X taraf')
plt.ylabel('Y taraf')
plt.xlim(0,6)
plt.ylim(0,15)
plt.savefig('my_first_plog.png')
plt.show()