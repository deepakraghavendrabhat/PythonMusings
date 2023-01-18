import pandas as pd

# df = pd.read_csv("data/Salary_Data.csv")
# print(df.shape)
# dict1 = df.to_dict()

people = {'name' : ['deepak','gundu','muddu'],'age' : [38,39,1]}
df = pd.DataFrame(people)
print(df)

if (1):
    print ('True')

# if (1)
#     print(True)
#
# if (1) print(True)

for i in range(3):
    print(i)

print('11 12 13 \n14')

a=11

b=12

c=13

d=14

print(a+b+c)

print(d)

a=11

b=12

c=13

d=14

print(a,b,c)

print(d)

a=11

b=12

c=13

d=14

print('{0} {1} {2}'.format(a,b,c) )

print(d)

a=11

b=12

c=13

d=14

print(f'{a}{b}{c}')

print(d)