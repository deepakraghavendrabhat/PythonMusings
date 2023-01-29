# # # # # # # # # # This is a sample Python script.
# # # # # # # # #
# # # # # # # # # # Press Shift+F10 to execute it or replace it with your code.
# # # # # # # # # # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # def print_hi(name):
# # # # # # # # #     # Use a breakpoint in the code line below to debug your script.
# # # # # # # # #     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # # Press the green button in the gutter to run the script.
# # # # # # # # # if __name__ == '__main__':
# # # # # # # # #     print_hi('PyCharm')
# # # # # # # # #
# # # # # # # # # # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# # # # # # # # # import numpy
# # # # # # # #
# # # # # # # # import math
# # # # # # # #
# # # # # # # #     # values (must be floats!)
# # # # # # # #
# # # # # # # # # google = open('dataset/google_stock_price.csv').readlines()
# # # # # # # # # print(google)
# # # # # # # # # print(type(google))
# # # # # # # # #
# # # # # # # # # google.pop(0)
# # # # # # # # # # gds = float(google)
# # # # # # # # #
# # # # # # # # # print(len(google))
# # # # # # # # # gstock = list(map(float,google))
# # # # # # # # # print(gstock)
# # # # # # # #
# # # # # # # # # # print((min((gstock))))
# # # # # # # # # print("min is: " + str(min(gstock)))
# # # # # # # # # # print((max((gstock))))
# # # # # # # # # print("max is: " + str(max(gstock)))
# # # # # # # # # # print((sum((gstock))))
# # # # # # # # # print("sum is: " + str(sum(gstock)))
# # # # # # # # # # print((sum((gstock))/len(gstock)))
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # n = len(gstock)
# # # # # # # # # gstock.sort()
# # # # # # # # #
# # # # # # # # # if n % 2 == 0:
# # # # # # # # #     median1 = gstock[n // 2]
# # # # # # # # #     median2 = gstock[n // 2 - 1]
# # # # # # # # #     median = (median1 + median2) / 2
# # # # # # # # # else:
# # # # # # # # #     median = gstock[n // 2]
# # # # # # # # # print("Median is: " + str(median))
# # # # # # # # #
# # # # # # # # # mean = sum(gstock) / len(gstock)   # mean
# # # # # # # # # print("Median is: " + str(mean))
# # # # # # # # # var  = sum(pow(x-mean,2) for x in gstock) / len(gstock)  # variance
# # # # # # # # # print("variance is: " + str(var))
# # # # # # # # # std  = math.sqrt(var)  # standard deviation
# # # # # # # # # print("std is: " + str(std))
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # g_d = dict()
# # # # # # # # # for i in gstock:
# # # # # # # # #     if i > 500:
# # # # # # # # #         g_d[i] = "Excellent"
# # # # # # # # #     elif i > 200 and i < 500:
# # # # # # # # #         g_d[i] = "Satisfactory"
# # # # # # # # #     elif i < 200:
# # # # # # # # #         g_d[i] = "Ok"
# # # # # # # # #
# # # # # # # # # print(g_d)
# # # # # # # # #
# # # # # # # # # print(chr(51))
# # # # # # # # #
# # # # # # # # # str = " Deepak "
# # # # # # # # # print(str.strip())
# # # # # # # #
# # # # # # # # # s = upGrad
# # # # # # # # #
# # # # # # # # # s = upgrad
# # # # # # # # #
# # # # # # # # # s = s[:2] + s[2].upper() + s[3:]
# # # # # # # # #
# # # # # # # # # print('G'.join(['up','rad']))
# # # # # # # # #
# # # # # # # # # s='aabupGradaab'.strip('aab')
# # # # # # # # # print(s)
# # # # # # # # # s='aabupGradaab'.strip('a').strip('b')
# # # # # # # # # # s='aabupGradaab'.strip('a').strip('b').strip('a')
# # # # # # # # # print(s)
# # # # # # # #
# # # # # # # # s = "Rebecca"
# # # # # # # # if s[::-1].lower() == s.lower():
# # # # # # # #     print(1)
# # # # # # # # else:
# # # # # # # #     print(0)
# # # # # # # #
# # # # # # # sentence="I love coding in python"
# # # # # # #
# # # # # # # output = []
# # # # # # # for i in sentence.split()[::-1]:
# # # # # # #     output.append(i)
# # # # # # # # print(" ".join(output))
# # # # # # # # print(" ".join(output))
# # # # # # #
# # # # # # # sen_list = sentence.split(' ')
# # # # # # # print(sen_list.reverse())
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # # s= "caloRie consuMed"
# # # # # # # cap1 = [word.title() for word in s.split(' ')]
# # # # # # # print('_'.join(cap1))
# # # # # #
# # # # # # # print(cap.replace(' ','_'))
# # # # # #
# # # # # # # s = "programming"
# # # # # # # v = 'aeiouAEIOU'
# # # # # # # c= ""
# # # # # # # o=""
# # # # # # # for i in s:
# # # # # # #     if i in v:
# # # # # # #         c = c + i
# # # # # # #     else:
# # # # # # #         o = o + i
# # # # # # # print(c+o)
# # # # # # #
# # # # # # # s1="programsbuzz"
# # # # # # # s2="programming"
# # # # # # #
# # # # # # # l1 = len(s1)
# # # # # # # l2 = len(s2)
# # # # # # # l3 = min(l1,l2)
# # # # # # #
# # # # # # # for i in range(l3):
# # # # # # #     if s1[i]!=s2[i]:
# # # # # # #         break
# # # # # # # print(i)
# # # # # # # if i == 0:
# # # # # # #     print(-1)
# # # # # # # else:
# # # # # # #     print(s1[:i])
# # # # # #
# # # # # #
# # # # # # # string1="upgradData"
# # # # # # # string2="upGradScience"
# # # # # # #
# # # # # # # #start writing your code to find largest common prefix here
# # # # # # # def comm():
# # # # # # #     low_s1 = string1.lower()
# # # # # # #     low_s2 = string2.lower()
# # # # # # #     l1 = len(string1)
# # # # # # #     l2 = len(string2)
# # # # # # #     l3 = min(l1,l2)
# # # # # # #
# # # # # # #     for i in range(l3):
# # # # # # #         if low_s1[i]!=low_s2[i]:
# # # # # # #             break
# # # # # # #
# # # # # # #     if i == 0:
# # # # # # #         print(-1)
# # # # # # #     else:
# # # # # # #         print(low_s1[:i])
# # # # # #
# # # # # #
# # # # # # # s1 = input()
# # # # # # # s2 = input()
# # # # # # #
# # # # # # # if sorted(s1) == sorted(s2):
# # # # # # #     print(1)
# # # # # # # else:
# # # # # # #     print(0)
# # # # # #
# # # # # # # s1 = "abcd"
# # # # # # # s2 = "cedab"
# # # # # # #
# # # # # # # elem = len(sorted(s2)) - len(sorted(s1))
# # # # # # # if len(sorted(s2)) > len(sorted(s1)):
# # # # # # #     elem = elem * -1
# # # # # # #     print(sorted(s2[elem]))
# # # # # # # else:
# # # # # # #     print(sorted(s1[elem]))
# # # # # # #
# # # # # # # print("Hello World"[::-1])
# # # # # # #
# # # # # # # S = "Python"
# # # # # # # S[1] = 'i'
# # # # # #
# # # # # # # s = 'I love Python'
# # # # # # # s = s.split(" ")
# # # # # # # s = s[-1::-1]
# # # # # # # s = " ".join(s)
# # # # # # #
# # # # # # # print(s)
# # # # # #
# # # # # # # value=input()
# # # # # # #
# # # # # # # # Hint
# # # # # # # # Step 1: Strip the spaces using strip()
# # # # # # # striped_val = value.strip()
# # # # # # # # Step 2: Separate the string at comma ','
# # # # # # # co_sv = striped_val.split(',')
# # # # # # # # Step 3: Join the number together using the join()
# # # # # # # joined_val = ''.join(co_sv)
# # # # # # # # Step 4: Convert the string to int
# # # # # # # print(int(joined_val))
# # # # # # # ['banana', 7]
# # # # # #
# # # # # # import ast
# # # # # # input_list = ast.literal_eval(input())
# # # # # #
# # # # # # msg = input_list[0]
# # # # # #
# # # # # #
# # # # # # key = int(input_list[1])
# # # # # # # print(key)
# # # # # # alphabet = 'abcdefghijklmnopqrstuvwxyz'
# # # # # # new_msg = ""
# # # # # # for char in msg:
# # # # # #     pos = alphabet.find(char.lower())
# # # # # #     newpos = (pos-key) % 26
# # # # # #     newchar = alphabet[newpos]
# # # # # #     if char.islower():
# # # # # #         pass
# # # # # #     else:
# # # # # #         newchar = newchar.upper()
# # # # # #     new_msg+= newchar
# # # # # # print(new_msg)
# # # # #
# # # # #
# # # # # # d=dict(a=1, b=2)
# # # # # #
# # # # # # # d={'a'=1, 'b'=2}
# # # # # # print(d)
# # # # # #
# # # # # # d={'a':64, 'b':65, 'c':66, 'd':67}
# # # # # # print(d['e'])
# # # # #
# # # # # d={'a':64, 'b':65, 'c':66, 'd':67}
# # # # # print(d.keys())
# # # #
# # # # #take input here
# # # # import ast
# # # # list_1 = ast.literal_eval(input())
# # # # #remove duplicates from the list
# # # # output = []
# # # #
# # # # for i in list_1:
# # # #     if i not in output:
# # # #         output.append(i)
# # # #
# # # # #print the list without duplicates
# # # # print(output)
# # #
# # # { 'Pen': ['Gel', 'Ink', 'ball'],'Mobile': ['Android', 'apple'] }
# # #
# # # #input has been taken for you
# # # import ast
# # # input_str = input()
# # # #input dictionary has been received in input_dict
# # # input_dict = ast.literal_eval(input_str)
# # # output = []
# # # for key in input_dict.keys():
# # #      for value in input_dict[key]:
# # #           output.append(key+'_'+value)
# # # print(output)
# # #
# # #
# # #
# #
# #
# # # #start writing your code here
# #
# # #input has been taken for you
# # s=input()
# #
# # output = dict()
# #
# # for i in s:
# #      if i not in output:
# #           output[i] = 1
# #      else:
# #           output[i]+= 1
# #
# # val = output.values()
# # n = len(output)
# #
# # def upgrad_String(val):
# #      for i in range(1,n+1):
# #           if i not in val:
# #                return False
# #      return True
# #
# # print(upgrad_String(val))
# # #start writing your code to check if s is upgrad string or no
# inp=input()
#
# stack = []
# for i in inp:
#      if len(stack) == 0:
#           stack.append(i)
#      else:
#           if i == ')' and stack[-1] == '(':
#                stack.pop()
#           elif i == '}' and stack[-1] == '{':
#                stack.pop()
#           elif i == ']' and stack[-1] == '[':
#                stack.pop()
#           else:
#                stack.append(i)
#
# if stack:
#      print('No')
# else:
#      print('Yes')
#
def func(x):
    return x % 10


L = [15, 20, 5, 29, 10]
print(sorted(L, key=func))

