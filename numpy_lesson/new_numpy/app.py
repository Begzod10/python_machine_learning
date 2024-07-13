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
# print(np.linspace(0, 20, 19))
# print(np.eye(5))
# print(np.random.rand(5,2)) # (qator soni, element soni)
# print(np.random.randn(2, 3))
# print(np.random.randint(2, 3))
# print(np.random.randint(0, 101, 5))  # sonlarni random olish (boshlanish soni, max soni, listda newta son bolishi)
# print(np.random.randint(0, 101, (4, 5))) 0 dan 101 max son (4 qator list, 5 ta son har bir listda)

# print(np.random.seed(42)) # bir marta chiqqan random sonla boshqa ozgarmidi
# print(np.random.rand(4))

# arr = np.arange(0, 25)
# arr.reshape(5, 5) 5 ta list ichiga 5 ta sonni bolib beradi
# print(arr)

# ranarr = np.random.randint(0, 101, 10)
# print(ranarr)
# print(ranarr.max())
# print(ranarr.min())
# print(ranarr.argmax()) max numberni indexsini topib beradi listni ichidan
# print(ranarr.argmax()) min numberni indexsini topib beradi listni ichidan
# print(ranarr.dtype)
# print(arr.shape)
# print(arr.reshape(25, 1))
# print(arr.reshape(1, 25))


# numpy 2 lesson

# arr = np.arange(0, 11)
# arr[0:5] = 100
# slice_of_array = arr[
#                  0:5]  # listda 5 gacha bogan indexsini copy qimidi link ovotgan boladi , keyinchalik slice_of_arrayni ichidagi ozgarsa array da ham ozgaradi
# slice_of_array[:] = 99
# arr_copy = arr.copy() # bu kodda list copy bo'ladi
# arr_copy[:] = 200
# array_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
# print(array_2d.shape) # (qator soni, column soni)
# print(array_2d[0][1])  # index orqali son olish
# print(array_2d[0, 1])  # index orqali son olish 2-usul

# print(array_2d[:2, 1:]) 2 qator listni oladi, listni ichidagila sonla 2-index gacha olinadi
# boolean_arr = arr > 4  # 4dan kichik bogan sonlar = False kottasi = True
# print(arr[boolean_arr])
# print(arr > 4)


# numpy 3 - lesson


# arr = np.arange(0, 10)

# print(arr + 5) listdagi har bir songa 5 qoshiladi
# print(arr - 5) listdagi har bir sondan 5 ni ayiradi

# print(arr + arr)  # ikkala listdagi sonla bir biriga qoshiladi
# print(arr - arr)  # ikkala listdagi sonla bir biridan ayiriladi
# print(arr / arr)
# print(np.sqrt(arr))
# print(np.sin(arr))
# print(np.log(arr))
# print(arr.sum())
# print(arr.mean())
# print(arr.max())
# print(arr.std())

# arr2d = np.arange(0, 25).reshape(5, 5)
# print(arr2d.sum()) oddiy sum() db yozilganda listdagi hamma sonlar bir biriga qoshiladi
# print(arr2d.sum(axis=0)) har bir columndagi sonlari bir biriga qoshiladi
# print(arr2d.sum(axis=1)) #har bir qatordagi sonlari bir biriga qoshiladi


# numpy lesson practice

# print(np.zeros(10))
# print(np.ones(10))
# print(np.ones(10) * 5)
#
# print(np.arange(10, 51))
# print(np.arange(10, 51, 2))
# array = np.arange(0, 9)
# print(array.reshape(3, 3))
# print(np.eye(3))
# print(np.random.rand(1))
# print(np.random.randn(25))


# print(np.arange(1, 101).reshape(10, 10) / 100)
# print(np.linspace(0, 1, 20))

mat = np.arange(1, 26).reshape(5, 5)
# print(mat)
# print(mat[2:, 1:])
# print(mat[3,4])
# print(mat[:3, 1:2])
# print(mat[4])
# print(mat[3:5])
# print(mat.sum())
# print(mat.std())
# print(mat.sum(axis=0))
# np.random.seed(42)  # bir marta chiqqan random sonla boshqa ozgarmidi
# print(np.random.rand(4))
