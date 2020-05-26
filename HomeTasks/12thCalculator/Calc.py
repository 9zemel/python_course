"""
Калькулятор v1.0. Функциональные требования:
Операции могут выполняться только над целыми числами, как положительными, так и отрицательными
Величина переменных не имеет ограничений
В случае ошибочного ввода переменных пользователя ждет сообщение об ошибке
Недопустимые математические операции также вызывают ошибку
Пользователь вводит значения переменных после выбора математической операции
"""
param_a = 0
param_b = 0
answer = 0


class Calculator:
    def __init__(self, param_a, param_b):
        self.param_a = param_a
        self.param_b = param_b

    def get_params(self, order):
        self.order = order
        while True:
            try:
                return (int(input("Enter %s param: " % self.order)))
                pass
            except ValueError:
                print('Please enter a number: ')

    def sum(self, param_a, param_b):
        result = param_a + param_b
        return result

    def sub(self, param_a, param_b):
        # param_a = self.get_params('first')
        # param_b = self.get_params('second')
        result = param_a - param_b
        return result

    def mul(self, param_a, param_b):
        # param_a = self.get_params('first')
        # param_b = self.get_params('second')
        result = int(param_a) * int(param_b)
        return result

    def div(self, param_a, param_b):
        # param_a = self.get_params('first')
        # param_b = self.get_params('second')
        try:
            return param_a / param_b
            pass
        except ZeroDivisionError:
            return ("На ноль делить нельзя ")

