# Класс должен быть покрыт тестами,
# в котором тестируется его работа, если
# пользователь забивает 1.цифру 2.букву 3.Пустой символ
from unittest.mock import patch
import unittest
from Calc import Calculator

class SumTestCases(unittest.TestCase):
    def setUp(self):
        """
        Создание экземпляра класса Calculator
        """
        self.calc = Calculator(0, 0)

    def test_get_param(self):
        '''Валидация int input происходит в методе get_param
        тест проверяет мок на валидных данных, но не может проверить мок
        на ошибочных - будет зацикливание, таков мой код
        '''
        with unittest.mock.patch('builtins.input', return_value=2):
            self.assertEqual(self.calc.get_params("first"), 2)

    def test_sum_positive(self):
        self.assertEqual(self.calc.sum(1, 2), 3)

    def test_sum_negative_one(self):
        self.assertEqual(self.calc.sum(0, -29999), -29999)

    def test_sum_negative_both(self):
        self.assertEqual(self.calc.sum(-150000, -29999), -179999)

    def test_sum_empty_string(self):
        self.assertRaises(TypeError, sum, -150000, '')

    def test_sum_one_string_param(self):
        self.assertRaises(TypeError, self.calc.sum, 1500, 'fd')

    def test_sum_both_strings(self):
        self.assertRaises(TypeError, sum, 'ab', 'fd')

    def test_sum_large_numbers(self):
        self.assertEqual(self.calc.sum(99999999999999900009999999999999999999990000999999,
                                       9999999999999990000999999999999999999999000099999999999999999999900009999999999999999999990000999999),
                         9999999999999990000999999999999999999999000100000099999999999999800019999999999999999999980001999998)


class SubTestCases(unittest.TestCase):
    def setUp(self):
        """
        Создать опрос и проверить его методы
        """
        self.calc = Calculator(0, 0)

    def test_sub_positive(self):
        self.assertEqual(self.calc.sub(20, 2), 18)

    def test_sub_negative_one(self):
        self.assertEqual(self.calc.sub(0, -29999), 29999)

    def test_sub_negative_both(self):
        self.assertEqual(self.calc.sub(-150000, -29999), -120001)

    def test_sub_empty_string(self):
        self.assertRaises(TypeError, self.calc.sub, -150000, '')

    def test_sub_one_string_param(self):
        self.assertRaises(TypeError, self.calc.sub, 1500, 'fd')

    def test_sum_both_strings(self):
        self.assertRaises(TypeError, self.calc.sub, 'ab', 'fd')

    def test_sum_large_numbers(self):
        self.assertEqual(self.calc.sub(99999999999999900009999999999999999999990000999999,
                                       9999999999999990000999999999999999999999000099999999999999999999900009999999999999999999990000999999),
                         -9999999999999990000999999999999999999999000099999900000000000000000000000000000000000000000000000000)


class MulTestCases(unittest.TestCase):
    def setUp(self):
        """
        Создать опрос и проверить его методы
        """
        self.calc = Calculator(0, 0)

    def test_mul_positive(self):
        self.assertEqual(self.calc.mul(20, 2), 40)

    def test_mul_negative_one(self):
        self.assertEqual(self.calc.mul(1, -29999), -29999)

    def test_mul_negative_both(self):
        self.assertEqual(self.calc.mul(-150, -299), 44850)

    def test_mul_zero_param(self):
        self.assertEqual(self.calc.mul(-150, 0), 0)

    def test_mul_both_zero_param(self):
        self.assertEqual(self.calc.mul(0, 0), 0)

    def test_mul_empty_string(self):
        self.assertRaises(ValueError, self.calc.mul, -150000, '')

    def test_mul_one_string_param(self):
        self.assertRaises(ValueError, self.calc.mul,1500, 'fd')

    def test_mul_both_strings(self):
        self.assertRaises(ValueError, self.calc.mul,'ab', 'fd')

    def test_mul_large_numbers(self):
        self.assertEqual(self.calc.sub(99999999999999900009999999999999999999990000999999,
                                       99999999999999900009999999999000099999999990000999999), -99899999999999900109989999999000100000000000000000000)


class DivTestCases(unittest.TestCase):
    def setUp(self):
        """
        Создать опрос и проверить его методы
        """
        self.calc = Calculator(0, 0)

    def test_div_positive(self):
        self.assertEqual(self.calc.div(20, 2), 10)

    def test_div_negative_one(self):
        self.assertEqual(self.calc.div(15, -5), -3)

    def test_div_negative_both(self):
        self.assertEqual(self.calc.div(-15, -5), 3)

    def test_div_first_zero_param(self):
        self.assertEqual(self.calc.div(0, -3), 0)

    def test_div_empty_string(self):
        self.assertRaises(TypeError, self.calc.div,-150000, '')

    def test_div_one_string_param(self):
        self.assertRaises(TypeError, self.calc.div, 1500, 'fd')

    def test_div_both_strings(self):
        self.assertRaises(TypeError, self.calc.div, 'ab', 'fd')

    def test_div_one_zero_param(self):
        self.assertEqual(self.calc.div(10, 0), 'На ноль делить нельзя ')

    def test_mul_large_numbers(self):
        self.assertEqual(self.calc.div(99999999999999900009999999999999999999990000999999,
                                        9999999999999990000999999999999999999999000099999999999999999999900009999999999999999999990000999999),1e-50)


if __name__ == '__main__':
    unittest.main()
