# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# X = 12
#
# if (X > 10 & X < 15):
#     print('YES')
# else:
#     print('No')
#
# a = 10
# b = 16
# c = 20
#
# if (c < a and c < b):
#     print("a")
# elif (a < b):
#     print("b")
# else:
#     print("c")

# input_str = "Alpha"
# #
# vowels = ['a','e','i','o','u']
# if(input_str[0].lower() in vowels):
#     print("YES")
# else:
#     print("NO")

# if (10 < 0) and (0 < -10):
#     print("A")
# elif (10 > 0) or False:
#     print("B")
# else:
#     print("C")


# shoppinng_total = 550
#
# if shoppinng_total >= 100:
#     print("You won a discount voucher of flat 1000 on next purchase")
# elif shoppinng_total >= 250:
#     print("You won a discount voucher of flat 500 on next purchase")
# elif shoppinng_total >= 500:
#     print("You won a discount voucher of flat 100 on next purchase")
# else:
#     print("OOPS!! no discount for you!!!")

# world_cups = {2019: ['England', 'New Zealand'], 2015: ["Australia", "New Zealand"], 2011: ["India", "Sri Lanka"],2007: ["Australia", "Sri Lanka"], 2003: ["Australia", "India"]}
#
# print(len(world_cups))
# print(list(world_cups.keys()))
#
# print(list(world_cups.values()))
#
#
# year = int(input("Enter year to check New Zealand made it to Finals in 20th century : "))
#
# if year in world_cups:
#     if "New Zealand" in world_cups[year]:
#         print("New Zealand made it to Finals")
#     else:
#         print("New Zealand could not make it to Finals")
#
# else:
#     print("World cup wasn't played in", year)

# students_data = {1:['Sam', 24] , 2:['Rob',25], 3:['Jack', 26], 4:['Cornor',24], 5:['Trump',27]}
#
# for key,value in students_data.items():
#     print(value[1])

# L1 = [10, 20, 30, 24, 18]
# L2 = [8, 14, 15, 20, 10]
# L3 = [0, 1, 2, 3, 4]
#
# for i in L3:
#     L3[i] = L1[i] - L2[i]
#     print((L3[i]))

# print(range(1, 10))
#
# print((list(range(1,10))))
#
# for i in range(1, 10):
#     print(i, end = ',')
#

# input_list = ['VARMA', 'raj', 'Gupta', 'SaNdeeP']
#
# new_name = [name.capitalize() for name in input_list]
# print(new_name)

# print(list(range(-100, -1, 2)))

# l = []
# for i in range(-100, 0):
#     if(i % 2 == 0):
#         l.append(i)
# print(l)
#
# print(sorted(set(range(-2, -101, -2))))
#
# print(list(range(0, -101, 2)))
#
# d = {0: 'Fish', 1: 'Bird', 2: 'Mammal'}
# for i in d:
#     print(i)

print(list(range(9,100,9)))

for i in range(1,10):
    print(19*i)