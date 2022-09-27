# 5. Реализуйте алгоритм перемешивания списка.
#  Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

num = int(input())
num_list = []

for i in range(1, num + 1):
    num_list.append(i - 1)
print(num_list)

n = []
for i in range(0, len(num_list)):
    var = 0
    if i % 2 == 0: 
        for i in range(1, len(num_list) - 1):
            i = var[i] 
            if i % 2 == 1: 
                m = num_list[i] + 1
                print(m, end = " ")



#####