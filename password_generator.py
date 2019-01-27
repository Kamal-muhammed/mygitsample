# import random,string
# length = int(input('Enter range:'))
# all = ""
# def func():
#     letters  = ''.join(random.choice(string.ascii_letters) for x in range(length - 2))
#     nums =  random.randint(0,12)
#     nums1 =  random.randint(0,9)
#     weird = ''.join(random.choice('@$^&*!~_=-()-+/#%') for x in range(5))
#     all = letters + str(nums) + weird + str(nums1)
#     return all
# print(func())
# #print(random.choice('@$^&*!~_=-')
# print('kamal')
# #print(random.choice('@$^&*!~_=-') for m in range(5))



N = int(input('Enter number:'))
if N % 2 == 1:
    print('Weird')
elif N % 2 == 0 and  range(2,5):
    print('Not Weird')
elif N % 2 == 0 and  range(6,20):
    print('Not Weird')
elif N % 2 == 0 and N > 20:
    print('Not Weird')
