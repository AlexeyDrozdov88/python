# # По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N 
# # (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

# # Input:       5 -- 5! = 1 * 2 * 3 * 4 * 5 = 120
# # Output:    120

# n = int(input('n = '))
# fact_res = 1
# i = 1
# while i <= n:
#     fact_res *= i
#     i += 1
# print(fact_res)

# # 2
# fact_res_2 = 1
# while n > 0:
#     fact_res_2 *= n
#     n -= 1
# print(fact_res_2)


# ------------------------------------------------------------------
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# Input:    5
# Output:  6

# 1 2 3 4 5 6 7  8  9 - нумераци
# 0 1 1 2 3 5 8 13 21 

# a = int(input())
# n0 = 0
# n1 = 1
# n2 = 0
# i = 2
# while n2 < a:
#     n2 = n0 + n1
#     n0, n1 = n1, n2
#     i += 1
#     if n2 > a:
#         i = -1
# print(i)

# --------------------------------------------------------------------------------------
# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая 
# длинная оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам,
# а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует,
# сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который 
# среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, 
# помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В 
# следующих строках располагается N целых чисел. 
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые 
# числа и лежат в диапазоне от –50 до 50

# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2

# 3 -> 10 10 10
# -> 3

# 5 -> 10 10 -2 -5 10
# -> 2 

# n = int(input('n = '))
# count = 0
# count_max = 0
# for i in range(n):
#     x = int(input())
#     if x > 0:
#         count += 1
#         if count > count_max:
#             count_max = count
#     else:
#         count = 0
# print(count_max)

# -----------------------------------------------------------------------------------------------------

# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, 
# а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для
# тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать 
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
# Input:	5 -> 5 1 6 5 9
# Output:	1 9

n = int(input('n = '))
x = int(input())
max_w = x
min_w = x
for i in range(n - 1):
    x = int(input())
    if x > max_w:
        max_w = x
    if x < min_w:
        min_w = x

print(max_w, min_w)

