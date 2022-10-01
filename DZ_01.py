#  1. Напишите программу, которая принимает на вход 
#  вещественное число и показывает сумму его цифр.
#  in -> out               12345 % 10 >> 5
#  6782 -> 23              12345 // 10 >> 1234
#  0.67 -> 13              int(198.45 * 10 ** 4)  >> 1984500 / 4-это 
#  198.45 -> 27            кольчество цифр в числе - 2, а - 2 
#                          делаем потому что . элемент плюс запас

num = float(input())
num_len = len(str(num))
num_natur = int(num * 10 ** num_len)
sum = 0
while num_natur > 0:
    digit = num_natur % 10 
    sum = sum + digit
    num_natur = num_natur // 10
print(sum)    

###########################################################

num = float(input())
sum_digits = 0

power = len(str(num)) - 2
num *= 10 ** power

while num:
    sum_digits += num % 10
    num //= 10

print(int(sum_digits))

