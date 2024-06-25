import pprint

import numpy as np

# a = np.array([1, 2, 3, 4, 5])
# print(type(a))
# a_mul = np.array([[1, 2, 3],
#                   [4, 5, 6],
#                   [7, 8, 9]])
#
# print(a_mul.shape)
# print(a_mul.ndim)
# print(a_mul.size)
# print(a_mul.dtype)

# d = {"num": 1}
# a = np.array([[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]], dtype="<U2")
# print(a.dtype)
# print(type(a[1][0]))


# a = np.full((2, 3, 4), 9)
# a = np.zeros((10, 5, 2))
# print(a)
# a = np.empty((5, 5, 5))
# print(a)

# x_values = np.arange(0, 1000, 5)
# print(x_values)
# x_values = np.linspace(0, 1000, 100)
# print(x_values)
#
# print(np.isnan(np.sqrt(-1)))
# print(np.isinf(np.array([10]) / 0))


# l1 = [1, 2, 3, 4, 5]
# l2 = [6, 7, 8, 9, 0]
# a1 = np.array(l1)
# a2 = np.array(l2)

# print(l1 * 5)
# print(a1 + 5)

# print(l1 + l2)
# print(a1 - a2)
# a1 = np.array([1, 2, 3])
# a2 = np.array([[1],
#                [2]])
# print(a1 + a2)

# a = np.array([1, 2, 3])
# a = np.append(a, [7, 8, 9])
# a = np.insert(a, 3, [4, 5, 6])
# print(np.delete(a, 1))
# print(np.delete(a, 3))
# print(np.delete(a, 4))

# a = np.array([[1, 2, 3],
#               [4, 5, 6]])
# print(np.delete(a, 1, 1))
# print(a)
# print(np.sqrt(a))

# a = np.array([[1, 2, 3, 4, 5],
#               [6, 7, 8, 9, 10],
#               [11, 12, 13, 14, 15],
#               [16, 17, 18, 19, 20]])
# print(a.shape)
# print(a.reshape((5, 4)))
# print(a.reshape((20,1)))
# print(a.reshape((2,10)))
# print(a.reshape((2,2,5)))
# a = a.reshape(10, 2)
# print(a)
# a.resize(10, 2)
# print(a)
# print(a.flatten())
# print(a.ravel())
# var1 = a.ravel()
# var1[2] = 100
# print(var1)
# print(a)
# var = [v for v in a.flat]
# print(var)

# a1 = np.array([[1, 2, 3, 4, 5],
#                [6, 7, 8, 9, 10]])
#
# a2 = np.array([[11, 12, 13, 14, 15],
#                [16, 17, 18, 19, 20]])
# a = np.concatenate((a1, a2),axis=1)
# print(a)
# print(a.transpose())

# a = np.stack((a1, a2))
# a = np.hstack((a1, a2))

# a = np.array([[1, 2, 3, 4, 5],
#               [6, 7, 8, 9, 10],
#               [11, 12, 13, 14, 15],
#               [16, 17, 18, 19, 20]])

# pprint.pprint(np.split(a, 4 , axis=0))
# print(a.min())
# print(a.max())
# print(a.mean())
# print(a.std())
# print(a.sum())
# print(np.median(a))

# number = np.random.randint(100)
# print(number)

# numbers = np.random.randint(90, 100, size=(2, 3, 4))
# numbers = np.random.binomial(10, p=0.5, size=(5, 10))
# numbers = np.random.normal(loc=170, scale=15, size=(5, 10))
# numbers = np.random.choice([19, 20, 39, 239], size=(5, 10))
# print(numbers)
# a = np.array([[1, 2, 3, 4, 5],
#               [6, 7, 8, 9, 10],
#               [11, 12, 13, 14, 15],
#               [16, 17, 18, 19, 20]])
#
# np.savetxt('myarray.csv', a, delimiter=",")
a = np.loadtxt('myarray.csv', delimiter=",")
print(a)
