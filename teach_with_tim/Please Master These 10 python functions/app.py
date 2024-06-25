# print("hello world", 'world', sep="-", end="") sep-> orasini symbol bn ajratishga; end -> keyingi print ni symbol bn ulashga bir qatorga
# print('age')
import pprint

# strings = ["my", "world", "apple", "pear"]


# lengths = map(len, strings) # harflani sanab beradi
# lengths = map(lambda x: x + "s", strings)  # harflani oxiriga s qoshib beradi
# print(list(lengths))
# def longer_than_4(string):
#     return len(string) > 4
#
#
# filtered = filter(lambda x: len(x) > 4, strings)
# print(list(filtered))

# numbers = {1, 2, 3, 4, 5, 23}
# print(sum(numbers, start=-10))
# people = [
#     {
#         "name": "name1", "age": 14
#     },
#     {
#         "name": "name3", "age": 12
#     },
#     {
#         "name": "name2", "age": 15
#     },
#     {
#         "name": "name4", "age": 16
#     }
# ]
# sorted_people = sorted(people, reverse=True, key=lambda person: person['name'])
# pprint.pprint(sorted_people)

# strings = ["my", "world", "apple", "pear"]
#
# for index, string in enumerate(strings):
#     print(f"{index + 1}. {string}")


# names = ['name1', 'name2', 'name3', 'name4']
# ages = [11, 22, 33, 12]
# gender = ["Female", "Male", "Female"]
# # for idx in range(min(len(names), len(ages))):
# #     name = names[idx]
# #     age = ages[idx]
# #     print(name, age, sep="-")
#
# combined = list(zip(names, ages, gender))
# for name, age, gen in combined:
#     print(name, age, gen)
# file = open("test.txt", "w")
# file.write("hello wordl\n my name is Begzod")
# file.close()
#
# with open('test.txt', "a") as file:
#     # text = file.read()
#     # print(text)
#     file.write("\nnew")
#     file.close()