# дз Написать код для класса Calculator,
# у которого есть все методы,
# которые выполняют математические операции
# = сложение, вычитание, деление, умножение.

from Calc import Calculator

param_a = 0
param_b = 0
answer = 0

while answer not in range(1, 5):
    print(
        """
        Выберите математическую операцию для выполнения:
        1 - сложение
        2 - вычитание
        3 - умножение
        4 - деление
        """
    )
    try:
        answer = int(input("Ваш выбор: "))
    except ValueError:
        print("Выберите операцию из значений ниже")

Calc = Calculator(param_a, param_b)

param_a = Calc.get_params('first')
param_b = Calc.get_params('second')

if answer == 1:
    print(Calc.sum(param_a, param_b))
elif answer == 2:
    print(Calc.sub(param_a, param_b))
elif answer == 3:
    print(Calc.mul(param_a, param_b))
else:
    print(Calc.div(param_a, param_b))