# Написать функцию, которая принимает строку на вход,
# и определяет, является ли строка палиндромом или нет
str = 'abcddcba'


def is_palindrom(str):
    length = len(str)
    if length > 1:
        for i in range(length):
            if str[i] != str[-i - 1]:
                print(str[i], 'is not equal to', str[-i - 1], '\nThe string is not a palindrom ')
                break
            print('The string is a palindrom')
            break
    else:
        print('The string is too short\n')


is_palindrom(str)
