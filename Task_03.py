#  3. Напишите программу, в которой пользователь будет задавать 
#  две строки, программа - определять количество вхождений 
#  одной строки в другой.
#  in > gipopotampo > po   >> out 3
#  in > gipopotampo > ta   >> out 1

#  dir(str) в консоле покажет все методы к строкам


str_first = input()
str_second = input()

print(str_first.count(str_second))  # .count метод подсчета вхождений
                                    # строки в подстроку