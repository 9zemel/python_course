import unittest
from simple_func import sum_function

class MyTestCase(unittest.TestCase):
    def test_sum(self):
        res = sum_function(2,3)
        self.assertEqual(res, 4)


if __name__ == '__main__':
    unittest.main()
