nums = [1,2,3]
mylist = [n*n for n in nums]
print(mylist)

mylist2 = [n for n in range(1,100) if n%2 == 0]
print(mylist2)

char_p = ['a','b','c','d']
nums = [1,2,3,4]
mylist3 = [(letter,num) for letter in char_p for num in nums]
print(mylist3)

