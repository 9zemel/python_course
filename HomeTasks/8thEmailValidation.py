# Сделать программу, которая собирает данные пользователей -
# в нем можно ввести логин пользователя и почту,
# и если с помощью проверки регулярными
# выражениями валидны, тогда они записываются в файл.
# В другом случае, пользователю говорится,
# что у него ошибка в введеных данных и нужно заново ввести данные.
import re


def get_user_login():
    while True:
        login = input('Please enter the login: ')
        if re.match(r'^[a-zA-Z0-9][^а-яА-Яё\s]{5,21}$', login):
            return 'match'
            break
        elif re.match(r'[а-яА-Яё]', login):
            print('Use only lat literals and symbols without spaces: ')
        else:
            print('Login must contains sequence of literals length from 6 to 20 ')

print(get_user_login())
