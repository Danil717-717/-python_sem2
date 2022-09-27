#  3. Задайте список из n чисел, заполненный 
#  по формуле (1 + 1/n) ** n и выведите на экран их сумму.
#  Для n = 6: [2, 2, 2, 2, 2, 3] -> 13


num = int(input())
num_list = []

for i in range(1, num + 1):
    num_list.append(round((1 + 1 / i) ** i))   
print(num_list)
sum = 0
for i in num_list:
    sum += i
print(sum)    


