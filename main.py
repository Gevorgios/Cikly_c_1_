# oneNumber = int(input("Введите первое число: "))
# twoNumber = int(input("Введите второе число: "))
# for i in range(oneNumber, twoNumber +1):
#     if i % 7 == 0:
#         print("Число кратное", i)


# start = int(input("Введите начало диапазона: "))
# end = int(input("Введите конец диапазона: "))
#
# # Вывод всех чисел в диапазоне
# print("Все числа в диапазоне:")
# for num in range(start, end+1):
#     print(num, end=" ")
#
# # Вывод всех чисел в убывающем порядке
# print("\nВсе числа в убывающем порядке:")
# for num in range(end, start-1, -1):
#     print(num, end=" ")
#
# # Вывод всех чисел, кратных 7
# print("\nЧисла, кратные 7:")
# for num in range(start, end+1):
#     if num % 7 == 0:
#         print(num, end=" ")
#
# # Подсчет количества чисел, кратных 5
# count = 0
# for num in range(start, end+1):
#     if num % 5 == 0:
#         count += 1
# print("\nКоличество чисел, кратных 5: ", count)



# start = int(input("Введите начало диапазона: "))
# end = int(input("Введите конец диапазона: "))
# for num in range(start, end+1):
#     if num % 3 == 0 and num % 5 == 0:
#         print("Fizz Buzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)