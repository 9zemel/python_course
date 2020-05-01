#дз Написать программу, которая в словаре  хранит имена пользователей,
# потом с помощью функции выводит их имена и фамилии с
# положительными качествами, которые заданы в программе в начале списка.
# Качество пользователей определяется рандомно
import random

streaks = ['пушистый', 'веселый', 'обаятельный', 'находчивый', 'умный', 'смелый'] #версия программы
# для представителей женского пола TBD

users_info = [['Алена', 'Кирилл', 'Лёша'],['Полякова', 'Петров', 'Петренко']]
users = ['user1', 'user2', 'user3']

dict = {}

j = 0
for i in users:
    dict[i] = users_info[0][j], users_info[1][j]
    j+=1

def users_streaks():
    for user in users:
        streaks_of_the_day = random.sample(streaks, 3)
        print('{} {}'.format(dict[user][0],dict[user][1]),'самый', '{}, {}, {}'.format(streaks_of_the_day[0],streaks_of_the_day[1],streaks_of_the_day[2]))

users_streaks()