import numpy as np

my_list = [1, 2, 3]

my_array = np.array(my_list)
# print(type(my_array))
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_arr = np.array(my_matrix)
# print(np.arange(0, 10))
# print(np.arange(0, 100, 2))
# print(np.zeros(5))  # (listdagi element soni) son=0
# print(np.zeros((2, 5)))  # (2- qator, 5- listdagi element soni) son=0
# print(np.ones((4, 4))) # np.zeros ga oxshab ishlidi faqat 0 ni orniga 1 keladi


# print(np.linspace(0, 11, 10))  # (listdagi son nechidan boshlanishi, listdagi sonlar max soni, boshlanishidan tugashigaca bogan sonlani newtasini olishi)

# print(np.eye(5))
# print(np.random.rand(5,2)) # (qator soni, element soni)
# print(np.random.randn(2, 3))
# print(np.random.randint(2, 3))
# print(np.random.randint(0, 101, 5))  # sonlarni random olish (boshlanish soni, max soni, listda newta son bolishi)
# print(np.random.randint(0, 101, (4, 5)))

# print(np.random.seed(42)) # bir marta chiqqan random sonla boshqa ozgarmidi
# print(np.random.rand(4))

arr = np.arange(0, 25)
arr.reshape(5, 5)
print(arr)
