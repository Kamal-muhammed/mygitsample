
# word = input("what is your word:")
# word = word.lower()
# new = ""
# vowels ="aeiou"
# for i in word:
#     if i in vowels:
#         # print(i)
#         new = new + i
#         print(new)
#         # print(len(new))

# user = input('What is your word:')
# new = ""
# for i in user:
#     if i in "aeiou":
#         new = new + i
# print(new)
# print(len(new))

#number = int(input('Enter your number range:'))
#for i in range(1,number):
        # if i % 3 == 0:
        #         print('Fizz')
        # elif i % 5 == 0 and i % 3 != 0:
        #         print('Buzz')
        # elif i % 3 ==0 and i % 5 == 0:
        #         print('Fizz Buzz')
        # if i % 3 == 0 and i % 5!= 0:
        #         print('Fizz')
        # if i % 5 == 0 and i % 3 != 0:
        #         print('Buzz')
        # if i % 3 == 0 and i % 5 == 0:
        #         print('Fizz Buzz')
        # if i % 3 != 0 and i % 5 != 0:
        #         print(i)
print('kamal')
import numpy as np 
import matplotlib.pyplot as plt
import datetime
kamal = [[1,7,3,9],[8,5,4,3,6],[0,9,7,2]]
listo = np.array(kamal)
print(type(listo))
print(listo[:])

year = [1950,1970,1990,2010]
pop = [2000,5000,9000,15000]
names = [0,4,7,9]
plt.plot(year,pop,names)
plt.show()

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)

p1.myfunc()
list1 = ['kamal','moha','clahi']
myit = iter(list1)
# print(next(myit))
# print(next(myit))
# print(next(myit))
#print(next(myit))
yobs = [1996,2000,1992,1985,2001,2009,2006,2003]
for year in yobs:
        age = 2019 - year
        print('This person is ' + str(age) + ' years old' )
