# # # # # # # # # # # # # This is a sample Python script.
# # # # # # # # # # # #
# # # # # # # # # # # # # Press Shift+F10 to execute it or replace it with your code.
# # # # # # # # # # # # # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # # def print_hi(name):
# # # # # # # # # # # # #     # Use a breakpoint in the code line below to debug your script.
# # # # # # # # # # # # #     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # Press the green button in the gutter to run the script.
# # # # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # # # #     print_hi('PyCharm')
# # # # # # # # # # # #
# # # # # # # # # # # # # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# # # # # # # # # # # # in_string=input("Enter:")
# # # # # # # # # # # # # print(in_string)
# # # # # # # # # # # # in_list = in_string.split(',')
# # # # # # # # # # # # # print(in_list)
# # # # # # # # # # # # x = int(in_list[0])
# # # # # # # # # # # # # print(x)
# # # # # # # # # # # # y = int(in_list[1])
# # # # # # # # # # # # # print(y)
# # # # # # # # # # # #
# # # # # # # # # # # # print(f"x before swapping:{x}")
# # # # # # # # # # # # print(f"y before swapping:{y}")
# # # # # # # # # # # # x,y = y,x
# # # # # # # # # # # # print()
# # # # # # # # # # # # print(f"x after swapping:{x}")
# # # # # # # # # # # # print(f"y after swapping:{y}")
# # # # # # # # # # #
# # # # # # # # # # # number = int(input())
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # # the function definition starts here
# # # # # # # # # # # def factorial(n):
# # # # # # # # # # #     # write the funtion here that finds and RETURNS factorial of next
# # # # # # # # # # #     if n <= 0:
# # # # # # # # # # #         return -1
# # # # # # # # # # #     elif n == 0:
# # # # # # # # # # #         return 1
# # # # # # # # # # #     else:
# # # # # # # # # # #         a = 1
# # # # # # # # # # #         for i in range(1,n+1):
# # # # # # # # # # #             a = a * i
# # # # # # # # # # #         return a
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # # function definition ends here
# # # # # # # # # # #
# # # # # # # # # # # # do not alter the code typed below
# # # # # # # # # # # k = factorial(number)
# # # # # # # # # # # print(k)
# # # # # # # # # #
# # # # # # # # # # n = 23400
# # # # # # # # # #
# # # # # # # # # # r = 0
# # # # # # # # # # while n > 0:
# # # # # # # # # #     r = r * 10 + n%10
# # # # # # # # # #     n = n//10
# # # # # # # # # # print(r)
# # # # # # # # # #
# # # # # # # # #
# # # # # # # # # input = input()
# # # # # # # # # inp_list = input.split(',')
# # # # # # # # #
# # # # # # # # # m = int(inp_list[0])
# # # # # # # # # c = int(inp_list[1])
# # # # # # # # #
# # # # # # # # # chc = m // c
# # # # # # # # # w = chc
# # # # # # # # #
# # # # # # # # # while w//3 != 0:
# # # # # # # # #     chc = chc + w // 3
# # # # # # # # #     w = w % 3 + w // 3
# # # # # # # # #
# # # # # # # # # print(chc)
# # # # # # # # #
# # # # # # # #
# # # # # # # # # n = 3
# # # # # # # # # iter = 1
# # # # # # # # # disp = '*'
# # # # # # # # # print(disp)
# # # # # # # # # while iter <= n:
# # # # # # # # #     disp = disp + '_*'
# # # # # # # # #     iter+= 1
# # # # # # # # #     print(disp)
# # # # # # # #
# # # # # # # # # n = 5
# # # # # # # # # for i in range(1,n+1):
# # # # # # # # #     for j in range(n-i):
# # # # # # # # #         print(' ',end='')
# # # # # # # # #     for k in range(i-1):
# # # # # # # # #         print('*_',end='')
# # # # # # # # #     print('*')
# # # # # # # #
# # # # # # # # # print(list(range(10, 1, -1)))
# # # # # # # #
# # # # # # # # # n = 154
# # # # # # # # #
# # # # # # # # # str_of_num = list(str(n))
# # # # # # # # # output = True if sum([(int(i) ** 3) for i in str]) == n else False
# # # # # # # # # print(output)
# # # # # # # # # # pow_list = [(int(i) ** 3) for i in str]
# # # # # # # # # # sum_val = sum([(int(i) ** 3) for i in str])
# # # # # # # # #
# # # # # # # # # # print(sum_val)
# # # # # # # # # # for i in str:
# # # # # # # # # #     print(int(i) ** 3)
# # # # # # # #
# # # # # # # # # n=int(input())
# # # # # # # # # # print(type(n))
# # # # # # # # # str_of_num = list(str(n))
# # # # # # # # # # print(str_of_num)
# # # # # # # # # # print(type(str_of_num))
# # # # # # # # # output = True if sum([int(i) ** 3 for i in str_of_num]) == n else False
# # # # # # # # # print(output)
# # # # # # # #
# # # # # # # # # n = 5
# # # # # # # # # val = 0
# # # # # # # # # for i in range(0,n):
# # # # # # # # #     print(val)
# # # # # # # # #     val+= 1
# # # # # # # # #
# # # # # # # # # n = 5
# # # # # # # # # fib0, fib1 = 0, 1
# # # # # # # # # for i in range(n):
# # # # # # # # #     print(fib0)
# # # # # # # # #     fib0, fib1 = fib1, fib0+fib1
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # # L = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# # # # # # # #
# # # # # # # # # print(L[[1, 3, 5, 7]])
# # # # # # # #
# # # # # # # # # print(L[1, 3, 5, 7])
# # # # # # # #
# # # # # # # # print(L[1::2])
# # # # # # # #
# # # # # # # # print(L[1:-1:2])
# # # # # # # #
# # # # # # # # print(L[2:-1:2])
# # # # # # # #
# # # # # # # #
# # # # # # # import time
# # # # # # #
# # # # # # # start_time = time.perf_counter()
# # # # # # # print(f"The start time is: {start_time}")
# # # # # # # for i in range(10):
# # # # # # #     print(i)
# # # # # # #
# # # # # # # end_time = time.perf_counter()
# # # # # # # print(f"The end time is: {end_time}")
# # # # # # # execution_time = end_time - start_time
# # # # # # # print(f"The execution time is: {execution_time}")
# # # # # # #
# # # # # # # ave
# # # # # #
# # # # # # # import ast
# # # # # # # input_str = input()
# # # # # # input_list = [ [2,4,6,8,-10],  4]
# # # # # #
# # # # # # #Remember how we took input in the Alarm clock Question in previous Session?
# # # # # # #Lets see if you can finish taking input on your own
# # # # # #
# # # # # # data= input_list[0]
# # # # # # check=input_list[1]
# # # # # #
# # # # # # average = sum(data)/len(data)
# # # # # #
# # # # # # if average > check:
# # # # # #     print(False)
# # # # # # else:
# # # # # #     print(True)
# # # # # # #
# # # # #
# # # # # import ast
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # team_list = [23,45,34,76]
# # # # # applicant_list = [70,34,94]
# # # # #
# # # # #
# # # # # def check_above_avg(data, check):
# # # # #     avg = sum(data) / len(data)
# # # # #     if avg < check:
# # # # #         return 1
# # # # #     else:
# # # # #         return 0
# # # # #
# # # # #
# # # # # for applicant in applicant_list:
# # # # #     finalist = check_above_avg(team_list, applicant)
# # # # #     if finalist == 1:
# # # # #         team_list.append(applicant)
# # # # #
# # # # # print(team_list)
# # # #
# # # #
# # # # import ast
# # # # event_list = ast.literal_eval(input())
# # # # marriage_date = int(input())
# # # #
# # # # clash = 0
# # # #
# # # # for dates in event_list:
# # # #     if marriage_date >= dates[0] and marriage_date <= dates[1]:
# # # #         clash += 1
# # # #
# # # # [(clash+=1) for dates in event_list if marriage_date >= dates[0] and marriage_date <= dates[1]]
# # # # print(clash)
# # #
# # #
# # # in_str = input().split(',')
# # # m = int(in_str[0])
# # # n = int(in_str[1])
# # #
# # # for row in range(0,m):
# # #     for col in range(0,n):
# # #         if (row == 0 or row == m-1) or (col == 0 or col == n-1):
# # #             print(1,end=" ")
# # #         else:
# # #             print(0,end=" ")
# # #     print()
# #
# # L = [1, 2, 3, 4]
# # def cube_func(n):
# #     return n**3
# # print(list(map(cube_func, L)))
# #
# #
# # L = [13, 16, 2, 19, 22, 24, 10, 49, 28, 82, 18]
# # final = []
# #
# # for i in range(len(L)):
# #     if L[i]%9 == 1:
# #         final.append(L[i])
# #
# # print(final)
# #
# # l = [0, 8, 16, 10, 36, 44, 93]
# #
# # final = [int(x ** 0.5) for x in l if x ** 0.5 - int(x ** 0.5) == 0]
# #
# # print(final)
#
#
# import ast
# # input_str = input()
# # input_list = ast.literal_eval(input_str)
# lis=[1,2,3,4,5,6,7,8,9]
# # input_list = [1,2,3,4,5,6,7,8,9]
# k=3
#
# final = [i for i in lis]
# print(final)
#
# for i in range(0, len(lis), k):
#     print(lis[i: i + k])
#
t = (2,3,5,10,-1) #tuple
x = sorted(t) #list

y = tuple(x) #sorted tuple