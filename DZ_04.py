#  4. Напишите программу, которая принимает на вход 2 числа. 
#  Задайте список из N элементов, заполненных числами 
#  из промежутка [-N, N]. Найдите произведение 
#  элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

posit_1 = int(input("Position one: "))
posit_2 = int(input("Position two: "))
numb_element = int(input("Number of elements: "))
if posit_1 > numb_element * 2 or posit_2 > numb_element * 2:
    print("Введите другие позиции")
    exit(1)

list = []
   
for i in range(-numb_element, numb_element + 1):
    list.append(i)
print(list)

m = 1
for i in range(len(list)):
    if i == posit_1 - 1:
        m = list[i] * m 
 
n = 1
for i in range(len(list)):
    if i == posit_2 - 1:
        n = list[i] * n 

print(m * n)


#######################################################################

num = int(input("Enter the value of N: "))
n_1 = int(input("Position one: "))
n_2 = int(input("Position two: "))

nums_list = list(range(-num, num + 1))

print(nums_list)
len_list = len(nums_list)

if len_list >= n_1 > 0 and len_list >= n_2 > 0:
    print(nums_list[n_1 - 1] * nums_list[n_2 - 1])
else:
    print("There are no values for these indexes!")
