# сколько тебе будет лет в таком то году?
# Программа,  которая спрашивает сколько тебе лет, потом ты вбиваешь год. Программа отвечает сколько тебе лет.
from datetime import datetime

currentYear = datetime.now().year

age = input('Сколько тебе лет? ')
while (age.isnumeric() == False) or (0 <= int(age) > 100):
    print('Ввод некорректен ')
    age = input('Сколько тебе лет? ')

age = int(age)

year = int(input('Введи год, чтобы узнать, сколько тебе будет лет в этом году: '))
while year <= currentYear:
    year = int(input('Пожалуйста, введи год в будущем, чтобы узнать, сколько тебе будет лет в этом году: '))

yearDiff = year - currentYear
futureAge = age + yearDiff;

if futureAge > 100:
    print('В',year,'году тебе будет',futureAge,'лет! Это маловероятно')
else:
    print('В',year,'году тебе будет',futureAge,'лет!')

input('\nНажмите Enter, чтобы выйти')

