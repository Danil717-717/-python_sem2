#  2. Напишите программу, которая принимает на вход 
#  число N и выдает набор произведений чисел от 1 до N.
#  1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
#  4 -> [1, 2, 6, 24]
#  6 -> [1, 2, 6, 24, 120, 720]


#import math

num = int(input())
f = 1

#while num > 1:
#    f = f * num
#    num = num - 1
#print(f)    

################

for i in range(2, num + 1):
    f = f * i
print(f)

################

#f = math.factorial(num)
#print(f)

