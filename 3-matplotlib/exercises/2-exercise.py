import numpy as np
import matplotlib.pyplot as plt

labels = ['1 Mo', '3 Mo', '6 Mo', '1 Yr', '2 Yr', '3 Yr', '5 Yr', '7 Yr', '10 Yr', '20 Yr', '30 Yr']

july16_2007 = [4.75, 4.98, 5.08, 5.01, 4.89, 4.89, 4.95, 4.99, 5.05, 5.21, 5.14]
july16_2020 = [0.12, 0.11, 0.13, 0.14, 0.16, 0.17, 0.28, 0.46, 0.62, 1.09, 1.31]
fig = plt.figure()

# ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
#
# ax.plot(labels, july16_2020, color="blue", label='july 16 2020')
# ax.plot(labels, july16_2007, color="red", label='july 16 2007')

# fig, axes = plt.subplots(nrows=2, ncols=1)
# axes[0].plot(labels, july16_2007)
# axes[0].set_title("July 16th, 2007")
# axes[1].plot(labels, july16_2020)
# axes[1].set_title("July 16th, 2020")
# # fig.suptitle('Figure level Title')
# plt.legend()


fig, ax1 = plt.subplots()
ax1.plot(labels, july16_2007, lw=2, color="blue")
ax1.set_ylabel(r"2007", fontsize=18, color="blue")
ax1.set_title("July 16th")
for label in ax1.get_yticklabels():
    label.set_color("blue")
ax2 = ax1.twinx()
ax2.plot(labels, july16_2020, lw=2, color="red")
ax2.set_ylabel(r"2020", fontsize=18, color="red")
for label in ax1.get_yticklabels():
    label.set_color("red")
plt.tight_layout()
plt.show()
