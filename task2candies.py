#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""




# 1 вариант: игра человека против "тупой машины")
# from random import *
# candies = 202
# while candies > 0:
#     first = int(input('Какое количество конфет берете? '))
#     if first > 28:
#         print('Можно брать не более 28 конфет за раз!')
#         first = int(input('Игрок 1: Какое количество конфет берете? '))
#     elif first > candies:
#         print('Вы не можете взять конфет больше, чем осталось!')
#         first = int(input('Игрок 1: Какое количество конфет берете? ')
#     candies -= first
#     print(f'Осталось {candies} конфет')
#     if candies >= 28:
#         second = randrange(1, 29)
#     elif candies < 28:
#         second = randrange(1, candies+1)
#     elif candies == 0:
#         print('Победил первый игрок - он забирает все конфеты!')
#         break
#     print(f'Второй игрок берет {second} конфет. Осталось {candies - second} конфет')
#     candies -= second
#     if candies == 0:
#         print('Победил второй игрок - он забирает все конфеты!')


#2 вариант: человек против человека
# candies = 202

# while candies > 0:
#     first = int(input('Игрок 1: Какое количество конфет берете? '))
#     if first > 28:
#         print('Можно брать не более 28 конфет за раз!')
#         first = int(input('Игрок 1: Какое количество конфет берете? '))
#     elif first > candies:
#         print('Вы не можете взять конфет больше, чем осталось!')
#         first = int(input('Игрок 1: Какое количество конфет берете? '))
#     candies -= first
#     print(f'Осталось {candies} конфет')
#     if candies == 0:
#         print('Победил первый игрок - он забирает все конфеты!')
#         break
#     second = int(input('Игрок 2: Какое количество конфет берете? '))
#     if second > 28:
#         print('Можно брать не более 28 конфет за раз!')
#         second = int(input('Игрок 2: Какое количество конфет берете? '))
#     elif second > candies:
#         print('Вы не можете взять конфет больше, чем осталось!')
#         second = int(input('Игрок 2: Какое количество конфет берете? '))
#     candies -= second
#     print(f'Осталось {candies} конфет')

#     if candies == 0:
#         print('Победил второй игрок - он забирает все конфеты!')


# 3 вариант: человек против умного бота -- в данном случае побеждает бот, если человек берет конфеты
#наугад случайным образом и не знает об алгоритме, как можно выиграть.
from random import *
candies = 202
while candies > 0:
    first = int(input('Игрок 1: Какое количество конфет берете? '))
    if first > 28:
        print('Можно брать не более 28 конфет за раз!')
        first = int(input('Игрок 1: Какое количество конфет берете? '))
    elif first > candies:
        print('Вы не можете взять конфет больше, чем осталось!')
        first = int(input('Игрок 1: Какое количество конфет берете? '))
    candies -= first
    print(f'Осталось {candies} конфет')
    if candies == 0:
        print('Победил Игрок 1 - он забирает все конфеты!')
        break
    if (candies % 29) != 0:
        second = candies % 29
    else:
        if candies >= 28:
            second = randrange(1, 28)
        else:
            second = randrange(1, candies + 1)
    candies -= second
    print(f'Игрок 2 берет {second} конфет. Осталось {candies} конфет')
    if candies == 0:
        print('Победил Игрок 2 - он забирает все конфеты!')



    

