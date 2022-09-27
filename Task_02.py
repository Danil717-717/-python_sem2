#  2. Создать список, длины n, значения формируются по формуле
#  3k + 1, где k принимает значения от 1 до n включительно.
#  in 3 >> out [4, 7, 10]
#  in 6 >> out [4, 7, 10, 16, 19]

num = int(input())
num_list = []

for i in range(1, num + 1):
    num_list.append(3 * i + 1)

print(num_list)