import unittest

from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Тесты для 'name_function.py'"""

    def test_first_last_name(self):
        """ Правда ли имя John Sina работает в этой функции как надо"""
        formatted_name = get_formatted_name('john ', '    sina')
        self.assertEqual(formatted_name, "John Sina")

    def test_first_last_otch_name(self):
        """Работают ли такие имена, как John Sinovich Sina"""
        formatted_name = get_formatted_name('john ', ' sinovich', '    sina')
        self.assertEqual(formatted_name, "John Sinovich Sina")

    def test_empty_name_or_surname(self):
        """Тест можно ли сюда вбивать пустые строки"""
        formatted_name = get_formatted_name('', '', '  aaa')
        self.assertEqual(formatted_name, "Введите корректные данные")
