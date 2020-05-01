import pirog as p
from pirog import *

p.make_pirog(3,5)
""" overcook """
# """Возвращает словарь с информацией о человеке"""

def make_pirog(flour, sugar):
    if flour > 7:
        print('Big')
    if sugar > 2:
        print('Think about your health')

make_pirog(8,3)